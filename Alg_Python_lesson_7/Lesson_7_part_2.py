
""" 2. Отсортируйте по возрастанию методом слияния одномерный вещественный массив, заданный случайными числами
на промежутке [0; 50). Выведите на экран исходный и отсортированный массивы."""

from random import uniform


def get_sort(array):

    if len(array) <= 1:
        return array

    elif len(array) == 2:
        if array[0] > array[1]:
            array[0], array[1] = array[1], array[0]
        return array

    left = get_sort(array[:len(array) // 2])
    right = get_sort(array[len(array) // 2:])
    i, j = 0, 0

    while len(left) > i and len(right) > j:
        if left[i] < right[j]:
            array[i + j] = left[i]
            i += 1
        else:
            array[i + j] = right[j]
            j += 1

    while len(left) > i:
        array[i + j] = left[i]
        i += 1
    while len(right) > j:
        array[i + j] = right[j]
        j += 1

    return array


lst = [round(uniform(1, 50, ), 2) for i in range(10)]

print(f' Исходный список веещственных чисел: \n {lst}')
print(f' Отсортированный по возрастанию список вещественных чисел: \n {get_sort(lst)}')
