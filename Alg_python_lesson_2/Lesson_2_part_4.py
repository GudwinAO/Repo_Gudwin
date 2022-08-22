"""4. Найти сумму n элементов следующего ряда чисел: 1 -0.5 0.25 -0.125
...Количество элементов (n) вводится с клавиатуры."""

""" numbers_list = [1, -0.5, 0.25, 0.125]
n = int(input('Введите количество элементов: '))
i = 0
range_number = 1
result_sum = 0

while i <= len(numbers_list) and i < n:
    result_sum += range_number
    range_number /= -2
    i += 1

print(f'Сумма {result_sum}') """

y = [1, -0.5, 0.25, 0.125, 0.75, 1.0, 2.5, 55, 148, 1000, 1.1, 3.8]


def sum_numbers(x):
    i = 0
    result_sum = 0
    if x > len(y):
        print(f'Вы ввели число, превышающее длину списка чисел. Длина списка чисел - {len (y)}  ')
    else:
        while x > 0:
            result_sum += y[i]
            i += 1
            x += -1
            sum_numbers(x)
    return result_sum


print(sum_numbers(int(input('Введите число элементов списка для сложения: '))))
