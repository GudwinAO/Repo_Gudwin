""" 1. Отсортируйте по убыванию методом "пузырька" одномерный целочисленный массив, заданный случайными числами на
промежутке [-100; 100). Выведите на экран исходный и отсортированный массивы. Сортировка должна быть реализована в виде
функции. По возможности доработайте алгоритм (сделайте его умнее)."""

from random import randint


def get_bubble_sort(lst):
    n = 1

    while n < len(lst):
        need_sort = True

        for i in range(len(lst) - n):

            if lst[i] > lst[i + 1]:
                lst[i], lst[i + 1] = lst[i + 1], lst[i]
                need_sort = False


        if need_sort == True:
            break

        n += 1

    return lst


number_list = [randint(-100, 100) for i in range(50)]

print(f'Исходный список чисел:\n {number_list}')
print(f'Список после пузырьковой сортировки: \n {get_bubble_sort(number_list)}')




