""" 9. Среди натуральных чисел, которые были введены,
найти наибольшее по сумме цифр. Вывести на экран это число и сумму его цифр."""

list_numbers = [i for i in input('Введите числа через пробел: ').split()]


def get_sum_numbers(number):
    sum_numbers = 0
    for f in number:
        sum_numbers += int(f)
    return sum_numbers


max_sum = 0

max_number = 0

for i in list_numbers:
    if get_sum_numbers(i) > max_sum:
        max_number = i
        max_sum = get_sum_numbers(i)

print(f'У введенного из чисел- {max_number} была наибольшая сумма цифр - {max_sum}')
