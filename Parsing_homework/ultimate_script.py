import argparse
import csv
import os
from collections import Counter
import json


def repo_root():
    return os.path.abspath(os.path.join(__file__, os.pardir))


def decent_report(data, filename, headers=None):
    with open(filename + '.csv', 'w') as csv_file:
        writer = csv.writer(csv_file)
        if headers is not None:
            writer.writerow(headers)
        for key in data:
            writer.writerow((key, data[key]))

    if is_json:
        with open(filename + '.json', 'w') as json_file:
            json.dump(data, json_file)


pars = argparse.ArgumentParser()
pars.add_argument("--json", action="store_true")
pars.add_argument("--log_path", default='access.log')
flag_values = pars.parse_args()
is_json = flag_values.json
log_path = flag_values.log_path
with open(log_path, 'r') as log:
    log_file = log.readlines()
    request_method_list = list()
    urls_list = list()
    ips_list = list()
    err4xx_stat_list = list()
    n = 0
    for line in log_file:
        n = n + 1
        request_method = line.split(' ')[5].split('"')[-1]
        url = line.split(' ')[6]
        status_code = line.split(' ')[8]
        if len(request_method) < 5:
            request_method_list.append(request_method)
        urls_list.append(url)
        if status_code[0] == '5':
            ips_list.append(line.split(' ')[0])
        elif status_code[0] == '4':
            err4xx_stat_list.append([url, status_code, len(url), line.split(' ')[0]])

err4xx_stat_list.sort(key=lambda i: i[2], reverse=True)
err4xx_stat_list = err4xx_stat_list[0:4]
decent_report(data={'Number of requests': n}, filename='requests_amount')
decent_report(data=dict(Counter(request_method_list).most_common()), headers=['Request method', 'Number of requests'],
              filename='requests_by_type')
decent_report(data=dict(Counter(urls_list).most_common(10)),
              headers=['Url', 'Requests amount'], filename='top10_most_frequent')
decent_report(data=dict(Counter(ips_list).most_common(5)),
              headers=['IP', 'Number of requests'], filename='top5_5xx_err')
with open('top5_4xx_err.csv', 'w') as csv_output:
    writer = csv.writer(csv_output)
    writer.writerow(['Url', 'Status code', 'Url size', 'IP'])
    for line in err4xx_stat_list:
        writer.writerow(line)

if is_json:
    err4_json = {
        'Url': [i[0] for i in err4xx_stat_list],
        'Status code': [i[1] for i in err4xx_stat_list],
        'Url size': [i[2] for i in err4xx_stat_list],
        'IP': [i[3] for i in err4xx_stat_list],
    }
    with open('top5_4xx_err.json', 'w') as outlet:
        json.dump(err4_json, outlet)
