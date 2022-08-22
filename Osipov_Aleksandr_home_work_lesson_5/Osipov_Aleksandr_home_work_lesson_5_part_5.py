""" Задание 5.
Подумайте, как можно сделать оптимизацию кода по памяти, по скорости.
Представлен список чисел. Определить элементы списка, не имеющие повторений.
Сформировать из этих элементов список с сохранением порядка их следования в исходном списке, например:
src = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
result = [23, 1, 3, 10, 4, 11]
Подсказка: напишите сначала решение «в лоб». Потом подумайте об оптимизации."""

import sys
from time import perf_counter

src = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]

# создаем List Comprehensions с перебором списка на предмет элементов, имеющих повторение не более 1 раза
start = perf_counter()
result = [num for num in src if src.count(num) == 1]
print('1 вариант решения:\n', result, '\n Время выполнения:\n', perf_counter() - start,
      '\n Байт памяти занято:\n ', sys.getsizeof(result))
print('--' * 20)

start = perf_counter()
result_2 = []


def get_count(x):
    for num in x:
        if src.count(num) == 1:
            result_2.append(num)


get_count(src)

print('Второй вариант решения:\n', result_2, '\n Время выполнения:\n', perf_counter() - start,
      '\n Байт памяти занято:\n ', sys.getsizeof(result_2))
