""" Задание 5.
Реализовать функцию get_jokes(), возвращающую n шуток, сформированных из трех случайных слов,
взятых из трёх списков (по одному из каждого):
nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]
Например:
get_jokes(2)
["лес завтра зеленый", "город вчера веселый"]
Документировать код функции.
Сможете ли вы добавить еще один аргумент — флаг, разрешающий или запрещающий повторы слов в шутках
(когда каждое слово можно использовать только в одной шутке)? Сможете ли вы сделать аргументы именованными? """

# импортируем библиотеку random для генерации случайных чисел и позиций список
import random

# создаем наши списки для генерации шуток
nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]


# создаем функцию с 2 аргументами, второй из которых - именованный (при отсутствии аргумента-значение "да")
def get_jokes(number, replay='да'):
    # список, в который будут падать наши шутки
    joke_list = []

    # ветвление с целью определить состояние флага "replay", а также понять - есть ли уникальные слова в словаре.
    if replay == 'да':
        for i in range(0, number):
            word_1 = nouns[random.randint(0, len(nouns) - 1)]
            word_2 = adverbs[random.randint(0, len(adverbs) - 1)]
            word_3 = adjectives[random.randint(0, len(adjectives) - 1)]
            joke_n = f"{word_1} {word_2} {word_3}"
            joke_list.append(joke_n)
        print(joke_list)

    # если пользователь определяет необходимость использования только уникальных слов - смотрим длинну списков
    elif replay == 'нет' and number <= len(nouns) and number <= len(adverbs) and number <= len(adjectives):
        for i in range(0, number):
            position_1 = int(random.uniform(0, len(nouns) - 1))
            position_2 = int(random.uniform(0, len(adverbs) - 1))
            position_3 = int(random.uniform(0, len(adjectives) - 1))
            word_1 = nouns[position_1]
            word_2 = adverbs[position_2]
            word_3 = adjectives[position_3]
            joke_n = f"{word_1} {word_2} {word_3}"
            # убираем каждое использованное слово из списка
            nouns.pop(position_1)
            adverbs.pop(position_2)
            adjectives.pop(position_3)
            joke_list.append(joke_n)
        print(joke_list)

    # если пользователь при аргументе повтора слов "нет" выбирает число шуток, большее чем уникальное число слов
    elif replay == 'нет' and number > len(nouns) or number > len(adverbs) or number > len(adjectives):
        print('Произошла ошибка. В списке не хватает уникальных слов, задайте меньшее значение')
        get_jokes((int(input('Сколько шуток нашутить?  '))),
                  (str.lower(input('Повтор слов - да или нет '))))

    # если пользователь ошибается при написании "да" или "нет". При это регистр значения не имеет
    else:
        print('Вы ошиблись в введении аргумента. Попробуйте еще раз')
        get_jokes((int(input('Сколько шуток нашутить?  '))),
                  (str.lower(input('Повтор слов - да или нет '))))


# вызываем функцию и передаем аргументы - число шуток и повтор слов в шутках
get_jokes((int(input('Сколько шуток нашутить?  '))), (str.lower(input('Повтор слов - да или нет '))))
