"""Задание 1.
Написать генератор нечётных чисел от 1 до n (включительно), используя ключевое слово yield, например:
odd_to_15 = odd_nums(15)
next(odd_to_15)
1
next(odd_to_15)
3
...
next(odd_to_15)
15
next(odd_to_15)
...StopIteration..."""


# создаем генератор нечетных чисел от 0 до назначенного пользователем значения
def get_odd(number):
    for num in range(1, (number + 1), 2):
        yield num


print(list(get_odd(int(input('Введите число x для интервала 0 - x: ')))))
