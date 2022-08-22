"""3. В массиве случайных целых чисел поменять местами минимальный и
максимальный элементы."""

import random

numbers_list = [random.randint(0, 99) for i in range(100)]

print(f'Массив чисел до изменения: {numbers_list}')


max_number = numbers_list[0]
min_number = numbers_list[0]

for f in numbers_list:
    if f >= max_number:
        max_number = f
    elif f <= min_number:
        min_number = f

print(f'Позиция максимального числа в списке: {numbers_list.index(max_number)}\nПозиция минимального числа в списке: '
      f'{numbers_list.index(min_number)}')

min_index = numbers_list.index(min_number)
max_index = numbers_list.index(max_number)

numbers_list[min_index], numbers_list[max_index] = numbers_list[max_index], numbers_list[min_index]

print(f'Проведена замена. \nПозиция максимального числа в списке: {numbers_list.index(max_number)}\n'
      f'Позиция минимального числа в списке: {numbers_list.index(min_number)}\n{numbers_list}')
