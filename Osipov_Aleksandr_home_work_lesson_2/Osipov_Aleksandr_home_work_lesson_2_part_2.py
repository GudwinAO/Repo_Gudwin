# Домашнее задание. Часть 2

"""Дан список:
['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']
Необходимо его обработать — обособить каждое целое число (вещественные не трогаем) кавычками
(добавить кавычку до и кавычку после элемента списка, являющегося числом)
и дополнить нулём до двух целочисленных разрядов:
['в', '"', '05', '"', 'часов', '"', '17', '"', 'минут', 'температура', 'воздуха', 'была', '"', '+05', '"', 'градусов']
Сформировать из обработанного списка строку:
в "05" часов "17" минут температура воздуха была "+05" градусов
Подумать, какое условие записать, чтобы выявить числа среди элементов списка?
Как модифицировать это условие для чисел со знаком?
Примечание: если обособление чисел кавычками не будет получаться - можете вернуться к его реализации позже.
Главное: дополнить числа до двух разрядов нулём!"""


# задаем данные нашего списка
all_list = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']

# запускаем функцию для перебора массива на предмет знаков чисел и возвращаем значение, если находим
def search_sign(x):
    if x[0] in '+-':
        return x[0]

# задаем вводную переменную для перебора массива
posit = 0

# запускаем цикл перебора массива до момента превышения длины
while posit < len(all_list):

    # создаем переменную для запуска функции перебора цикла и поиска знака
    result_func = search_sign(all_list[posit])

    # ветвление - если число в составе списка или возврат функции +/- плюс срез за знаком-число, выполняем добавление 0
    if all_list[posit].isdigit() or (result_func and all_list[posit][1:].isdigit()):
        if result_func:
            all_list[posit] = result_func + all_list[posit][1:].zfill(2)
        else:
            all_list[posit] = all_list[posit].zfill(2)

        # добавляем слева и справа (+2) от числа списка  кавычки. и переходим на следующий элемент массива
        all_list.insert(posit, '"')
        all_list.insert(posit + 2, '"')
        posit += 2

    posit += 1
# выводим измененный массив
print(all_list)

# переводим массив в строку
str_list: str = ' '.join(all_list)

# выводим результат
print(str_list)
