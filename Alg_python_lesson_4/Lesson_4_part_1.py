"""Задание 1.
Проанализировать скорость и сложность одного - трёх любых алгоритмов,
разработанных в рамках домашнего задания первых трех уроков."""

# Алгоритм 1. Найти наиболее часто встречающийся элемент списка

import cProfile
import random


def get_max_number(a):
    numbers_list = [random.randint(0, 99) for f in range(a)]
    print(f'Анализируемый массив чисел {numbers_list}')
    max_index = 0
    for i in numbers_list:
        if numbers_list.count(max_index) < numbers_list.count(i):
            max_index = numbers_list.index(i)

    return numbers_list[max_index]


print(f'Число, встречающееся наиболее часто - {get_max_number(50)}')

cProfile.run('get_max_number(500)')
"""5295 function calls in 0.005 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.005    0.005 <string>:1(<module>)
        1    0.000    0.000    0.005    0.005 Lesson_4_part_1.py:11(get_max_number)
        1    0.000    0.000    0.001    0.001 Lesson_4_part_1.py:12(<listcomp>)
      500    0.000    0.000    0.000    0.000 random.py:239(_randbelow_with_getrandbits)
      500    0.000    0.000    0.001    0.000 random.py:292(randrange)
      500    0.000    0.000    0.001    0.000 random.py:366(randint)
     1500    0.000    0.000    0.000    0.000 {built-in method _operator.index}
        1    0.000    0.000    0.005    0.005 {built-in method builtins.exec}
        1    0.000    0.000    0.000    0.000 {built-in method builtins.print}
      500    0.000    0.000    0.000    0.000 {method 'bit_length' of 'int' objects}
     1000    0.003    0.000    0.003    0.000 {method 'count' of 'list' objects}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
      635    0.000    0.000    0.000    0.000 {method 'getrandbits' of '_random.Random' objects}
      154    0.000    0.000    0.000    0.000 {method 'index' of 'list' objects}"""
cProfile.run('get_max_number(10000)')

"""102835 function calls in 1.258 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    1.258    1.258 <string>:1(<module>)
        1    0.003    0.003    1.258    1.258 Lesson_4_part_1.py:11(get_max_number)
        1    0.002    0.002    0.016    0.016 Lesson_4_part_1.py:12(<listcomp>)
    10000    0.003    0.000    0.005    0.000 random.py:239(_randbelow_with_getrandbits)
    10000    0.006    0.000    0.012    0.000 random.py:292(randrange)
    10000    0.002    0.000    0.014    0.000 random.py:366(randint)
    30000    0.001    0.000    0.001    0.000 {built-in method _operator.index}
        1    0.000    0.000    1.258    1.258 {built-in method builtins.exec}
        1    0.006    0.006    0.006    0.006 {built-in method builtins.print}
    10000    0.000    0.000    0.000    0.000 {method 'bit_length' of 'int' objects}
    20000    1.232    0.000    1.232    0.000 {method 'count' of 'list' objects}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
    12808    0.001    0.000    0.001    0.000 {method 'getrandbits' of '_random.Random' objects}
       21    0.000    0.000    0.000    0.000 {method 'index' of 'list' objects}
"""
# при увеличении элементов списка в 20 раз - длительной выполнения алгоритма возрастает в 251 раз, количество
# вызовов функции возрастает в 19,4 раза.


