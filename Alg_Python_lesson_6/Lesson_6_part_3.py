import random
import sys

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

# количество ссылок на переменные
print(sys.getrefcount(min_index))
print(sys.getrefcount(numbers_list))

# размеры пустого списка и number_list
print(sys.getsizeof([]))
print(sys.getsizeof(numbers_list))

