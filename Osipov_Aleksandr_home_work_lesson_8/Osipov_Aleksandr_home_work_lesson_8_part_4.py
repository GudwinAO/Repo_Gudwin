""" Задание 4. Написать декоратор с аргументом-функцией (callback), позволяющий валидировать входные значения функции
и выбрасывать исключение ValueError, если что-то не так, например:
def val_checker...
    ...


@val_checker(lambda x: x > 0)
def calc_cube(x):
   return x ** 3


 a = calc_cube(5)
125
 a = calc_cube(-5)
Traceback (most recent call last):
  ...
    raise ValueError(msg)
ValueError: wrong val -5

Примечание: сможете ли вы замаскировать работу декоратора?
"""

from functools import wraps


def val_checker(func):
    @wraps(func)
    def wrapper(call_back):

        if call_back >= 0:
            result = f"""a = {func.__name__} ({call_back})\n {func(call_back)}"""
            return result
        else:
            print(f'a = {func.__name__} ({call_back})')
            raise ValueError

    return wrapper


@val_checker
def calc_cube(x):
    return x ** 3


print(calc_cube(int(input('Введите число без дробной части: '))))
