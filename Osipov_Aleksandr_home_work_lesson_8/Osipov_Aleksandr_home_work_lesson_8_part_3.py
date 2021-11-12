""" Задание 3. Написать декоратор для логирования типов позиционных аргументов функции, например:
def type_logger...
    ...


@type_logger
def calc_cube(x):
   return x ** 3

a = calc_cube(5)
5: <class 'int'>

Примечание: если аргументов несколько - выводить данные о каждом через запятую;
можете ли вы вывести тип значения функции? Сможете ли решить задачу для именованных аргументов? Сможете ли вы
замаскировать работу декоратора? Сможете ли вывести имя функции, например, в виде:

a = calc_cube(5)
calc_cube(5: <class 'int'>)
"""

from functools import wraps


def type_logger(function):
    @wraps(function)
    def wrapper(*args, **kwargs):

        for arg in args:
            z = f'a = {function.__name__}({arg})\n{function.__name__}({arg},{type(arg)})\n' \
                f'Результат функции = {function(arg)}'
            print(z)

        for kwarg in kwargs:
            z = f'a = {function.__name__}({kwarg})\n{function.__name__}({kwarg},{type(kwarg)})\n' \
                f'Результат функции = {function(kwarg)}'
            print(z)

    return wrapper


@type_logger
def calc_cube(*args):
    for arg in args:
        return arg ** 3


calc_cube(3, 5, 12)
