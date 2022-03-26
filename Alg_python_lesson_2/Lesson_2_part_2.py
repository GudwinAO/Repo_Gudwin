"""2. Посчитать четные и нечетные цифры введенного натурального числа.
Например, если введено число 34560, то у него 3 четные цифры (4, 6 и 0) и 2 нечетные (3 и 5)."""

while True:
    number = input('Введите число: ')

    even = 0
    odd = 0

    try:
        for f in number:
            i = int(f)
            if i % 2 == 0:
                even += 1
            else:
                odd += 1
    except ValueError:
        print('Неправильный ввод.')
        continue

    print(f'У числа {number}: четных цифр - {even}, нечетных - {odd} ')


