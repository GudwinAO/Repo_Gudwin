"""4. Определить, какое число в массиве встречается чаще всего."""

import random

numbers_list = [random.randint(0, 99) for f in range(100)]
print(f'Массив чисел: {numbers_list}')

max_index = 0

for i in numbers_list:
    if numbers_list.count(max_index) < numbers_list.count(i):
        max_index = numbers_list.index(i)

print(f'Число {numbers_list[max_index]} встречается чаще всего -  {numbers_list.count(max_index)} раза')
