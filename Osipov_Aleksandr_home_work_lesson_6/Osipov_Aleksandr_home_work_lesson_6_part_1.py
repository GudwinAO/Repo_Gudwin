""" Задание 1.
Не используя библиотеки для парсинга, распарсить (получить определённые данные) файл логов web-сервера nginx_logs.txt
(https://github.com/elastic/examples/raw/master/Common%20Data%20Formats/nginx_logs/nginx_logs) —
получить список кортежей вида: (<remote_addr>, <request_type>, <requested_resource>). Например:

[
...
('141.138.90.60', 'GET', '/downloads/product_2'),
('141.138.90.60', 'GET', '/downloads/product_2'),
('173.255.199.22', 'GET', '/downloads/product_2'),
...
]

Примечание: код должен работать даже с файлами, размер которых превышает объем ОЗУ компьютера.

2. * (вместо 1) Найти IP адрес спамера и количество отправленных им запросов по данным файла логов
из предыдущего задания.
Примечания: спамер — это клиент, отправивший больше всех запросов; код должен работать даже
с файлами, размер которых превышает объем ОЗУ компьютера. """

from os import path

DIR = 'C:/Users/TEST OS/PycharmProjects/MyProject/Repo_Gudwin/Osipov_Aleksandr_home_work_lesson_6'
FILE_NAME = 'nginx_logs.txt'
FILE = path.join(DIR, FILE_NAME)

with open(FILE, 'r', encoding='utf-8') as f:
    for line in f:
        list_line = line.replace('"', ' ', 2).split()
        result = (list_line[0], list_line[5], list_line[6])
        print(result, end='\n')
