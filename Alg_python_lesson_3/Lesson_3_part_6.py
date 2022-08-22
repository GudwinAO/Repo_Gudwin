"""6. В одномерном массиве найти сумму элементов, находящихся между
минимальным и максимальным элементами. Сами минимальный и максимальный
элементы в сумму не включать."""

import random

numbers_list = [random.randint(0, 99) for f in range(10)]

print(f'Массив чисел: {numbers_list}')

min_index = 0
max_index = 0
step = 1
result_sum = 0
count_numbers = 0

for i in numbers_list:
    if numbers_list[min_index] > i:
        min_index = numbers_list.index(i)
    elif numbers_list[max_index] < i:
        max_index = numbers_list.index(i)

if max_index - min_index < 0:
    step = -1

for i in numbers_list[min_index + step:max_index:step]:
    result_sum += i
    count_numbers += 1


print(
        f'Сумма элементов между минимальным ({numbers_list[min_index]})',
        f' и максимальным ({numbers_list[max_index]}) элементами: {result_sum}\n'
        f'Всего числе между искомыми: {count_numbers}'
        )
