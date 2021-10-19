# Домашнее задание. 3 часть.

"""Реализовать склонение слова «процент» во фразе «N процентов».
Вывести эту фразу на экран отдельной строкой для каждого из чисел в интервале от 1 до 100."""

# 1,десятичные порядки, оканчивающиеся на 1 - 'процент'
# 2,3,4, десятичные порядки, оканчивающиеся на 2 - 'процента'
# 5,6,7,8,9,0 и десятичные порядки, оканчивающиеся на 5,6,7,8,9,0 - 'процентов'
# исключения - 11,12,13,14 'процентов'

# создаем переменную - наш список числового выражения  проценто от 1 до 100
percents = list(range(1, 101))
select_number = 0

# запускаем цикл перебора нашего списка значений и присваиваем склонение по описанным выше правилам
while select_number < 100:
    target_percent = percents[select_number]
    remain = target_percent % 10

    if remain == 0 or remain == 5 or remain == 6 or remain == 7 or remain == 8 or remain == 9:
        print(target_percent, ' процентов')
        select_number += 1

    elif target_percent == 11 or target_percent == 12 or target_percent == 13 or target_percent == 14:
        print(target_percent, ' процентов')
        select_number += 1

    elif remain == 1 and target_percent != 11:
        print(target_percent, ' процент')
        select_number += 1

    elif remain == 2 or remain == 3 or remain == 4 or target_percent != 12 or target_percent != 13 or target_percent != 14:
        print(target_percent, ' процента')
        select_number += 1