
# создаем наш словарь перевода английских числительных
numbers = dict(zero='ноль', one='один', two='два', three='три', four='четыре', five='пять', six='шесть', seven='семь',
               eight='восемь', nine='девять', ten='десять')

# создаем функцию, проверяющую формат введения слова для перевода и выводящую перевод с нужным форматом
def num_translate_adv(i):
    if str.istitle(numb_translate[0]) != False:
        print(str.title(numbers.get(i)))
    else:
        print(numbers.get(i))

# запускаем цикл, предлагающий пользователю прописать цифру для перевода
while True:
    numb_translate = input('Введите число от 0 до 10 на английском прописью: ')
    # используем промежуточную переменную для корректной работы функции при разных регистрах введения
    _numb_translate = str.lower(numb_translate)
    translate = num_translate_adv(_numb_translate)