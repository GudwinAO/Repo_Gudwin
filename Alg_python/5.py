"""
5. Пользователь вводит две буквы. Определить, на каких местах алфавита они
стоят и сколько между ними находится букв.
"""

letter_1, letter_2 = [x.upper() for x in input('Введите две буквы, через пробел (A - Z): ').split()]

# генерируем алфавит
abc_list = [chr(i) for i in range(ord('A'), ord('Z') + 1)]

# вычисляем позиции введенных букв в данном списке
index_letter_1 = abc_list.index(letter_1) + 1
index_letter_2 = abc_list.index(letter_2) + 1

# проводим проверку позиции введенных букв друг к другу, в т.ч. при введении одинаковой буквы

letters_number = abs(index_letter_1 - index_letter_2) - 1

step = 1

if index_letter_1 == index_letter_2:
    letters_number = 0

elif index_letter_1 > index_letter_2:
    step = -1



print(f'Первая буква {letter_1}, находится на позиции: {index_letter_1}')
print(f'Вторая буква {letter_2}, находится на позиции: {index_letter_2}')

# выводим пользователю сообщение о буквах между введенными буквами и их количестве

print(
    f'Между ними находятся буквы {abc_list[abc_list.index(letter_1) + step:abc_list.index(letter_2):step]} '
    f'Всего букв в промежутке: {letters_number} букв'
    )

