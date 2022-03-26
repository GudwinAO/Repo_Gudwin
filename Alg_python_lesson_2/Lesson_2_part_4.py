"""4. Найти сумму n элементов следующего ряда чисел: 1 -0.5 0.25 -0.125
...Количество элементов (n) вводится с клавиатуры."""

numbers_list = [1, -0.5, 0.25, 0.125]
n = int(input('Введите количество элементов: '))
i = 0
range_number = 1
result_sum = 0


while i <= len(numbers_list) and i < n:
    result_sum += range_number
    range_number /= -2
    i += 1

print(f'Сумма {result_sum}')