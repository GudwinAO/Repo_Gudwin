""" 3. Сформировать из введенного числа обратное по порядку входящих в него цифр и вывести на экран.
Например, если введено число 3486, то надо вывести число 6843."""


def reverse(x):
    y = -1
    str_result = ''
    for i in range(len(x)):
        str_result += x[y]
        y -= 1
    return str_result


def reverse_2(x):
    str_result = ''
    if len(x) == 0:
        return str_result
    else:
        str_result += x[-1] + reverse_2(x[:-1])
        return str_result


number = input('Введите строку: ')

print(f'Строка {number} в обратном порядке: {reverse_2(number)}')








