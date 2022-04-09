"""5. В массиве найти максимальный отрицательный элемент. Вывести на
экран его значение и позицию в массиве."""

import random

numbers_list = [random.randint(-99, 99) for _ in range(100)]
print(f'Массив чисел: {numbers_list}')

min_index = 0

for i in numbers_list:
    if numbers_list[min_index] > i:
        min_index = numbers_list.index(i)

if numbers_list[min_index] >= 0:
    print(f'В массиве нет отрицательных элементов')
else:
    print(f'В массиве минимальный отрицательный элемент: {numbers_list[min_index]}.',
          f'Находится в массиве на позиции {min_index}')
