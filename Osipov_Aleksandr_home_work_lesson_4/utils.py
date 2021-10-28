# импортируем необходимую нам библиотеку
import requests

# задаем константы
URL = 'http://www.cbr.ru/scripts/XML_daily.asp'
VALUE = 'Value'
DATE = 'Date'

""" задаем функцию - c входными переменными - валюта, объем конвертируемой валюты, объем рублей для конвертации. 
На выходе функция выводит в консоль курс заданной валюты на дату, количество рублей в заданном лоте валюты на дату
и количество валюты в заданном лоте рублей на дату """


def currency_rates(coin, lot, lot_rub):
    content = requests.get(URL).text
    coin_search = content.find(coin)
    date_search = content.find(DATE)
    date = content[date_search + len(DATE) + 2:date_search + len(DATE) + 12]

    if coin_search != -1:
        value_search = content.find(VALUE, coin_search)
        if value_search > coin_search:
            curse = content[value_search + len(VALUE) + 1: value_search + len(VALUE) + 8]
            for x in range(len(curse)):
                if curse[x] in ',':
                    curse_ft = float((curse[:x] + curse[x + 1:])) / 10000
                    print(f'Курс {coin} на {date} составляет:  {curse_ft}')
                    money_lot = curse_ft * lot
                    print(f'{lot} {coin} по курсу на {date} - это {money_lot} рублей')
                    money_rub = lot_rub / curse_ft
                    print(f'{lot_rub} рублей по курсу на {date}- это {money_rub} {coin}')

        else:
            print('Курс не найден')
    else:
        print('Не найдена валюта. Проверьте верность введения индекса валюты!')
        currency_rates(str.upper(input('Введите название валюты в стиле EUR, USD , AUD: ')),
                       float(input('Введите количество валюты для конвертации в рубли: ')),
                       float(input('Введите количество рублей для конвертации в выбранную валюту: ')))
