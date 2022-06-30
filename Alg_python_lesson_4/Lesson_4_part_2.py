"""Задание 2.
Написать два алгоритма нахождения i-го по счёту простого числа.
Первый - использовать алгоритм решето Эратосфена. Второй - без использования "решета".
Проанализировать скорость и сложность алгоритмов."""

import cProfile
import timeit


def get_numbers_eratosfen(index):
    if index < 600:
        last_index = (index // 20)*150
    elif index < 600000:
        last_index = (index // 20) * 300
    else:
        last_index = (index // 20) * 500

    sieve = [i for i in range(last_index)]

    sieve[1] = 0

    for i in range(2, last_index):
        if sieve[i] != 0:
            j = i * 2
            while j < last_index:
                sieve[j] = 0
                j += i

    sieve_simple_num = [i for i in sieve if i != 0]

    print(f'Ваше простое число - {sieve_simple_num[index-1]}')


timeit.main(get_numbers_eratosfen(100))

timeit.main(get_numbers_eratosfen(500))

timeit.main(get_numbers_eratosfen(1000))

timeit.main(get_numbers_eratosfen(10000))

print('-'*100)

cProfile.run('get_numbers_eratosfen(100)')

cProfile.run('get_numbers_eratosfen(500)')

cProfile.run('get_numbers_eratosfen(1000)')

cProfile.run('get_numbers_eratosfen(10000)')

print('-'*100)


# Вариант без решета

def find_simple_numbers(index):
    num = 3
    simple_nums = [2]
    nums = [2]
    while True:
        if len(simple_nums) == index:
            print(f'Ваше {index} простое число = {simple_nums[index-1]}')
            break
        else:
            for i in nums:
                if num % i == 0:
                    nums.append(num)
                    break
            else:
                nums.append(num)
                simple_nums.append(num)
        num += 1


timeit.main(find_simple_numbers(100))

timeit.main(find_simple_numbers(500))

timeit.main(find_simple_numbers(1000))

timeit.main(find_simple_numbers(10000))

print('-'*100)

cProfile.run('find_simple_numbers(100)')

cProfile.run('find_simple_numbers(500)')

cProfile.run('find_simple_numbers(1000)')

cProfile.run('find_simple_numbers(10000)')

# Итог - значительно более эффективным вариантом работы является 1 вариант с использованием решета.
# При анализе 10 000 чисел разница 14,8 секунд без решета против 0,031 - с решетом

"""Результата работы программы:
Ваше простое число - 541
50000000 loops, best of 5: 6.23 nsec per loop
Ваше простое число - 3571
50000000 loops, best of 5: 7.06 nsec per loop
Ваше простое число - 7919
50000000 loops, best of 5: 6.48 nsec per loop
Ваше простое число - 104729
50000000 loops, best of 5: 6.19 nsec per loop
----------------------------------------------------------------------------------------------------
Ваше простое число - 541
         7 function calls in 0.000 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.000    0.000 <string>:1(<module>)
        1    0.000    0.000    0.000    0.000 Lesson_4_part_2.py:10(get_numbers_eratosfen)
        1    0.000    0.000    0.000    0.000 Lesson_4_part_2.py:18(<listcomp>)
        1    0.000    0.000    0.000    0.000 Lesson_4_part_2.py:29(<listcomp>)
        1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
        1    0.000    0.000    0.000    0.000 {built-in method builtins.print}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}


Ваше простое число - 3571
         7 function calls in 0.001 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.001    0.001 <string>:1(<module>)
        1    0.000    0.000    0.001    0.001 Lesson_4_part_2.py:10(get_numbers_eratosfen)
        1    0.000    0.000    0.000    0.000 Lesson_4_part_2.py:18(<listcomp>)
        1    0.000    0.000    0.000    0.000 Lesson_4_part_2.py:29(<listcomp>)
        1    0.000    0.000    0.001    0.001 {built-in method builtins.exec}
        1    0.000    0.000    0.000    0.000 {built-in method builtins.print}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}


Ваше простое число - 7919
         7 function calls in 0.003 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.003    0.003 <string>:1(<module>)
        1    0.002    0.002    0.003    0.003 Lesson_4_part_2.py:10(get_numbers_eratosfen)
        1    0.000    0.000    0.000    0.000 Lesson_4_part_2.py:18(<listcomp>)
        1    0.000    0.000    0.000    0.000 Lesson_4_part_2.py:29(<listcomp>)
        1    0.000    0.000    0.003    0.003 {built-in method builtins.exec}
        1    0.000    0.000    0.000    0.000 {built-in method builtins.print}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}


Ваше простое число - 104729
         7 function calls in 0.031 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.031    0.031 <string>:1(<module>)
        1    0.025    0.025    0.030    0.030 Lesson_4_part_2.py:10(get_numbers_eratosfen)
        1    0.003    0.003    0.003    0.003 Lesson_4_part_2.py:18(<listcomp>)
        1    0.003    0.003    0.003    0.003 Lesson_4_part_2.py:29(<listcomp>)
        1    0.000    0.000    0.031    0.031 {built-in method builtins.exec}
        1    0.000    0.000    0.000    0.000 {built-in method builtins.print}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}


----------------------------------------------------------------------------------------------------
Ваше 100 простое число = 541
50000000 loops, best of 5: 6.14 nsec per loop
Ваше 500 простое число = 3571
50000000 loops, best of 5: 6.44 nsec per loop
Ваше 1000 простое число = 7919
50000000 loops, best of 5: 6.41 nsec per loop
Ваше 10000 простое число = 104729
50000000 loops, best of 5: 6.08 nsec per loop
----------------------------------------------------------------------------------------------------
Ваше 100 простое число = 541
         1183 function calls in 0.001 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.001    0.001 <string>:1(<module>)
        1    0.001    0.001    0.001    0.001 Lesson_4_part_2.py:57(find_simple_numbers)
        1    0.000    0.000    0.001    0.001 {built-in method builtins.exec}
      540    0.000    0.000    0.000    0.000 {built-in method builtins.len}
        1    0.000    0.000    0.000    0.000 {built-in method builtins.print}
      638    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}


Ваше 500 простое число = 3571
         7643 function calls in 0.025 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.025    0.025 <string>:1(<module>)
        1    0.024    0.024    0.025    0.025 Lesson_4_part_2.py:57(find_simple_numbers)
        1    0.000    0.000    0.025    0.025 {built-in method builtins.exec}
     3570    0.000    0.000    0.000    0.000 {built-in method builtins.len}
        1    0.000    0.000    0.000    0.000 {built-in method builtins.print}
     4068    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}


Ваше 1000 простое число = 7919
         16839 function calls in 0.109 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.109    0.109 <string>:1(<module>)
        1    0.108    0.108    0.109    0.109 Lesson_4_part_2.py:57(find_simple_numbers)
        1    0.000    0.000    0.109    0.109 {built-in method builtins.exec}
     7918    0.000    0.000    0.000    0.000 {built-in method builtins.len}
        1    0.000    0.000    0.000    0.000 {built-in method builtins.print}
     8916    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}


Ваше 10000 простое число = 104729
         219459 function calls in 14.806 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000   14.806   14.806 <string>:1(<module>)
        1   14.795   14.795   14.806   14.806 Lesson_4_part_2.py:57(find_simple_numbers)
        1    0.000    0.000   14.806   14.806 {built-in method builtins.exec}
   104728    0.005    0.000    0.005    0.000 {built-in method builtins.len}
        1    0.000    0.000    0.000    0.000 {built-in method builtins.print}
   114726    0.006    0.000    0.006    0.000 {method 'append' of 'list' objects}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}


"""
