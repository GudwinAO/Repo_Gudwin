"""1. Написать программу, которая будет складывать, вычитать, умножать или делить два числа. Числа и знак операции
вводятся пользователем. После выполнения вычисления программа не должна завершаться, а должна запрашивать новые данные
для вычислений. Завершение программы должно выполняться при вводе символа '0' в качестве знака операции.
Если пользователь вводит неверный знак (не '0', '+', '-', '*', '/'),
то программа должна сообщать ему об ошибке и снова запрашивать знак операции.
Также сообщать пользователю о невозможности деления на ноль, если он ввел 0 в качестве делителя."""

while True:
    try:
        number_1, operation, number_2 = [i for i in input
        ('Введите число 1, операцию (+ - * / или 0), число 2 - через пробел :').split()
                                         ]
    except ValueError:
        print('Неправильный ввод.')
        continue

    number_1 = int(number_1)
    number_2 = int(number_2)

    if operation == '0':
        print('Цикл рассчета завершен')
        break
    elif operation == '+':
        print(f'{number_1} {operation} {number_2} = {number_1 + number_2}')
    elif operation == '-':
        print(f'{number_1} {operation} {number_2} = {number_1 - number_2}')
    elif operation == '*':
        print(f'{number_1} {operation} {number_2} = {number_1 * number_2}')
    elif operation == '/':
        try:
            print(f'{number_1} {operation} {number_2} = {number_1 / number_2}')
        except ZeroDivisionError:
            print('Ошибка. Деление на ноль')
