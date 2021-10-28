"""Написать функцию currency_rates(), принимающую в качестве аргумента код валюты (например, USD, EUR, GBP, ...)
и возвращающую курс этой валюты по отношению к рублю. Использовать библиотеку requests.
В качестве API можно использовать http://www.cbr.ru/scripts/XML_daily.asp.
Рекомендация: выполнить предварительно запрос к API в обычном браузере, посмотреть содержимое ответа.
Можно ли, используя только методы класса str, решить поставленную задачу?
Функция должна возвращать результат числового типа, например float.
Подумайте: есть ли смысл для работы с денежными величинами использовать вместо float тип Decimal?
Сильно ли усложняется код функции при этом? Если в качестве аргумента передали код валюты, которого нет в ответе,
вернуть None. Можно ли сделать работу функции не зависящей от того, в каком регистре был передан аргумент?
В качестве примера выведите курсы доллара и евро.

3. * (вместо 2) Доработать функцию currency_rates():
теперь она должна возвращать кроме курса дату, которая передаётся в ответе сервера.
Дата должна быть в виде объекта date. Подумайте, как извлечь дату из ответа, какой тип данных лучше использовать
в ответе функции?

4. Написать свой модуль utils и перенести в него функцию currency_rates() из предыдущего задания.
Создать скрипт, в котором импортировать этот модуль и выполнить несколько вызовов функции currency_rates().
Убедиться, что ничего лишнего не происходит.

5. * (вместо 4) Доработать скрипт из предыдущего задания: теперь он должен работать и из консоли. Например:
> python task_4_5.py USD
75.18, 2020-09-05"""

import requests

URL = 'http://www.cbr.ru/scripts/XML_daily.asp'
VALUE = 'Value'
DATE = 'Date'


def currency_rates(coin, lot, lot_rub):
    content = requests.get(URL).text
    coin_search = content.find(coin)
    date_search = content.find(DATE)
    date = content[date_search+len(DATE)+2:date_search+len(DATE)+12]

    if coin_search != -1:
        value_search = content.find(VALUE, coin_search)
        if value_search > coin_search:
            curse = content[value_search + len(VALUE) + 1: value_search + len(VALUE) + 8]
            for x in range(len(curse)):
                if curse[x] in ',':
                    curse_ft = float((curse[:x] + curse[x + 1:]))/10000
                    print(f'Курс {coin} на {date} составляет:  {curse_ft}')
                    money_lot = curse_ft*lot
                    print(f'{lot} {coin} по курсу на {date} - это {money_lot} рублей')
                    money_rub = lot_rub/curse_ft
                    print(f'{lot_rub} рублей по курсу на {date}- это {money_rub} {coin}')

        else:
            print('Курс не найден')
    else:
        print('Не найдена валюта. Проверьте верность введения индекса валюты!')
        currency_rates(str.upper(input('Введите название валюты в стиле EUR, USD , AUD: ')))


currency_rates(str.upper(input('Введите название валюты в стиле EUR, USD , AUD: ')),
               float(input('Введите количество валюты для конвертации в рубли: ')),
               float(input('Введите количество рублей для конвертации в выбранную валюту: ')))
