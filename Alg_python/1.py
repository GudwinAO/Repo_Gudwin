"""
1. Найти сумму и произведение цифр трехзначного числа, которое вводит пользователь.
"""
number = input('Введите целое трехзначное число: ')

if len(number) != 3:
    print('Ошибка. Необходимо ввести трехзначное число')
    number = input('Введите целое трехзначное число: ')


# Решаем без использования цикла. Находим все составные части трехзначного числа
number_3 = int(number) % 10
number_2 = (int(number) // 10) % 10
number_1 = int(number) // 100

result_1 = number_1+number_2+number_3
result_2 = number_1*number_2*number_3

print(f"Сумма чисел вашего числа равно: {result_1} , произведение чисел вашего числа равно: {result_2} ")






