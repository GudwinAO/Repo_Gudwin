""" 6. В программе генерируется случайное целое число от 0 до 100.
Пользователь должен его отгадать не более чем за 10 попыток.
После каждой неудачной попытки должно сообщаться больше или меньше введенное пользователем число,
чем то, что загадано. Если за 10 попыток число не отгадано, то вывести загаданное число."""

from os import urandom as _urandom


def random_number():
    random = int(int.from_bytes(_urandom(7), 'big')) >> 5
    list = [n for n in range(0, 101)]
    return list[random % 100]


secret_number = random_number()
i = 1
while i <= 10:
    print(f'Попытка №{i:2} из 10')
    user_number = int(input('Введите число от 1 до 100: '))
    if user_number == secret_number:
        print('Загаданное число угадано')
        break
    elif user_number > secret_number:
        print(f'Ваше число {user_number} больше загаданного')
    else:
        print(f'Ваше число {user_number} меньше загаданного')
    i += 1
if i > 10:
    print(f'Не угадано! Загаданное число {secret_number}')