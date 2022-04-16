"""
2. Выполнить логические побитовые операции «И», «ИЛИ» и др. над числами 5 и 6.
Выполнить над числом 5 побитовый сдвиг вправо и влево на два знака. Объяснить полученный результат.
"""

# вводим константы чисел

NUMBER_1 = 5
NUMBER_2 = 6

# "ИЛИ" оператор копирует бит, если тот присутствует в хотя бы в одномоперанде

bit_or = NUMBER_1 | NUMBER_2

# Исключительное "ИЛИ" оператор копирует бит только если бит присутствует в одном из операндов, но не в обоих сразу
bit_xor = NUMBER_1 ^ NUMBER_2

# "И" оператор, копирует бит в результат только если бит присутствует в обоих операндах
bit_and = NUMBER_1 & NUMBER_2

# Побитовое отрицание меняет биты на обратные, там где была единица становиться ноль и наоборот

bit_not_n1 = ~NUMBER_1
bit_not_n2 = ~NUMBER_2

# Побитовый сдвиг вправо. Значение левого операнда "сдвигается" вправо на количество бит указанных в правом операнде
bit_shift_right = NUMBER_1 >> 2

# Побитовый сдвиг влево. Значение левого операнда "сдвигается" влево на количество бит указанных в правом операнде
bit_shift_left = NUMBER_1 << 2

# Выводим данные для пользователя

print(f"""Побитовое «ИЛИ» (OR) для {bin(NUMBER_1)} и {bin(NUMBER_2)}: \
{bin(bit_or)} ({bit_or})""")

print(f"""Исключающее «ИЛИ» (XOR) для {bin(NUMBER_1)} и {bin(NUMBER_2)}: \
{bin(bit_xor)} ({bit_xor})""")

print(f"""Побитовое «И» (AND) для {bin(NUMBER_1)} и {bin(NUMBER_2)}: \
{bin(bit_and)} ({bit_and})""")

print(f"""Побитовое отрицание (NOT) для {bin(NUMBER_1)}: \
{bin(bit_not_n1)} ({bit_not_n1}) и для {bin(NUMBER_2)}: \
{bin(bit_not_n2)} ({bit_not_n2})""")

print(f"""Битовый сдвиг вправо для {bin(NUMBER_1)}: \
{bin(bit_shift_right)} ({bit_shift_right})""")

print(f"""Битовый сдвиг влево для {bin(NUMBER_1)}: \
{bin(bit_shift_left)} ({bit_shift_left})""")