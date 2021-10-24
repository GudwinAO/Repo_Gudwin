""" Задание 4. * (вместо задачи 3)
Написать функцию thesaurus_adv(), принимающую в качестве аргументов строки в формате «Имя Фамилия»
и возвращающую словарь, в котором ключи — первые буквы фамилий, а значения — словари, реализованные по схеме предыдущего
задания и содержащие записи, в которых фамилия начинается с соответствующей буквы. Например:
thesaurus_adv("Иван Сергеев", "Инна Серова", "Петр Алексеев", "Илья Иванов", "Анна Савельева")
{
    "А": {
        "П": ["Петр Алексеев"]
    },
    "С": {
        "И": ["Иван Сергеев", "Инна Серова"],
        "А": ["Анна Савельева"]
    }
}
Как поступить, если потребуется сортировка по ключам? """


def thesaurus(*name):

    list_soname_name = str.split(*name)
    list_name = []
    list_soname = []
    pos = 0
    for pos in range(0, len(list_soname_name)):
        if pos % 2 == 0:
            list_name.append(list_soname_name[pos])
        else:
            list_soname.append(list_soname_name[pos])

    print(list_name)
    print(list_soname)

    dictionary_soname = {}

    for name in list_soname:
        name = name.capitalize()
        key = name[0]
        if key not in dictionary_soname:
            dictionary_soname[key] = []
        dictionary_soname[key].append(name)

    print(dictionary_soname)

thesaurus(str(input('Введите данные сотрудников - Имя: ')))
