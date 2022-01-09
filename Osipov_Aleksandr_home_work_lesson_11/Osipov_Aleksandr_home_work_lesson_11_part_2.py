""" Задание 2. Создайте собственный класс-исключение, обрабатывающий ситуацию деления на ноль.
Проверьте его работу на данных, вводимых пользователем. При вводе нуля в качестве делителя программа должна
корректно обработать эту ситуацию и не завершиться с ошибкой."""


class ZeroDivision:
    @staticmethod
    def get_er(*args):
        for arg in args:
            try:
                result = int(arg[0]) / int(arg[1])
                return f'Результат деления {result}'
            except ZeroDivisionError:
                return 'Вы использовали "0" как делитель. Будьте внимательней'




int_numbers = input('Введите 2 числа через ","/ 1 число - делимое, второе - делитель:')
target_numbers = int_numbers.split(',')

print(ZeroDivision.get_er(target_numbers))
