import os
from collections import Counter


def repo_root():
    return os.path.abspath(os.path.join(__file__, os.pardir))


def requests_by_type_dict(log_strings):
    request_method_list = []
    for line in log_strings:
        request_method = line.split(' ')[5].split('"')[-1]
        if len(request_method) < 5:
            request_method_list.append(request_method)
    return dict(Counter(request_method_list).most_common())


def top_most_frequent_dict(log_strings, items_amount):
    urls_list = []
    for line in log_strings:
        url = line.split(' ')[6]
        urls_list.append(url)

    return dict(Counter(urls_list).most_common(items_amount))


def top_5xx_err_dict(log_strings, items_amount):
    ips_list = []
    for line in log_strings:
        status_code = line.split(' ')[8]
        if status_code[0] == '5':
            ips_list.append(line.split(' ')[0])

    return dict(Counter(ips_list).most_common(items_amount))


def top_4xx_err_list(log_strings, items_amount):
    err4xx_stat_list = []
    for line in log_strings:
        status_code = line.split(' ')[8]
        url = line.split(' ')[6]
        if status_code[0] == '4':
            err4xx_stat_list.append([url, status_code, len(url), line.split(' ')[0]])

    err4xx_stat_list.sort(key=lambda i: i[2], reverse=True)
    err4xx_stat_list = err4xx_stat_list[0:items_amount]
    return err4xx_stat_list


def get_data():
    with open(os.path.join(repo_root(), '../access.log'), 'r') as log:
        log_file = log.readlines()

    return {
    'requests_amount': len(log_file),
    'requests_by_type': requests_by_type_dict(log_file),
    'top10_most_frequent': top_most_frequent_dict(log_file, 10),
    'top5_5xx_err': top_5xx_err_dict(log_file, 5),
    'top5_4xx_err': top_4xx_err_list(log_file, 5)
    }
