1) <b>bash_script</b><br>
В результате работы скрипта в директории, где находится скрипт, будет создано 5 csv файлов с информацией, требуемой в ТЗ<br>
Запуск в терминале: <b>bash path/to/script /path/to/access.log</b><br>
*полученные csv файлы лучше смотреть с пробелом в качестве разделителя

2) <b>ultimate_script.py</b><br>
В результате работы скрипта в его рабочей директории будет создано 
5 csv файлов (и 5 json файлов при указании флага) с информацией, запрашиваемой в ТЗ. Чтобы дополнительно получить файлы в формате json, при запуске необходимо указать флаг <b>--json</b>. По умолчанию будет искать access.log в рабочей директории. Путь к файлу можно указать через флаг <b>--log_path</b><br>
Запуск в терминале: <b>python path/to/script --log_path=/path/to/log --json</b><br>
*полученные csv файлы лучше смотреть с запятой в качестве разделителя

Имена созданных файлов: 'requests_amount', 'requests_by_type', 'top10_most_frequent', 'top5_5xx_err', 'top5_4xx_err'
