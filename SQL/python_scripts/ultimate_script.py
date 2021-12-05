import os
from collections import Counter


def repo_root():
    return os.path.abspath(os.path.join(__file__, os.pardir))

def get_data():
    with open(os.path.join(repo_root(), '../access.log'), 'r') as log:
        log_file = log.readlines()
        request_method_list = []
        urls_list = []
        ips_list = []
        err4xx_stat_list = []
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
    err4xx_stat_list = err4xx_stat_list[0:5]

    return {
    'requests_amount': n,
    'requests_by_type': dict(Counter(request_method_list).most_common()),
    'top10_most_frequent': dict(Counter(urls_list).most_common(10)),
    'top5_5xx_err': dict(Counter(ips_list).most_common(5)),
    'top5_4xx_err': err4xx_stat_list
    }
