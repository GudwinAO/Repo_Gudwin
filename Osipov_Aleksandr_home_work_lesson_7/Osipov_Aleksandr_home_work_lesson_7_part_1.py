""" Задание 1.
Написать скрипт, создающий стартер (заготовку) для проекта со следующей структурой папок:
|--my_project
   |settings
   |mainapp
   |--adminapp
   |authapp
Примечание: подумайте о ситуации, когда некоторые папки уже есть на диске (как быть?); как лучше хранить конфигурацию
этого стартера, чтобы в будущем можно было менять имена папок под конкретный проект; можно ли будет при этом расширять
конфигурацию и хранить данные о вложенных папках и файлах (добавлять детали)?

2. * (вместо 1) Написать скрипт, создающий из config.yaml стартер для проекта со следующей структурой:
|--my_project
   |settings
   |  |--index.html
   |  |--dev.py
   |  |--prod.py
   |mainapp
   |  |--index.html
   |  |--models.py
   |  |--views.py
   |  |--templates
   |     |mainapp
   |        |--base.html
   |        |--index.html
   |authapp
   |  |--index.html
   |  |--models.py
   |  |--views.py
   |  |--templates
   |     |authapp
   |        |--base.html
   |        |--index.html
Примечание: структуру файла config.yaml придумайте сами, его можно создать в любом текстовом редакторе «руками»
(не программно); предусмотреть возможные исключительные ситуации, библиотеки использовать нельзя."""

from os import path, makedirs

with open('Dir_configure', 'r', encoding='utf-8') as f:
    try:
        for line in f:
            if "-" not in line:
                parent_dir = line.strip()
            else:
                child_dir = line[1:].strip()
                if not path.isdir(line.strip()):
                    dir_cat = path.join(parent_dir, child_dir)
                    makedirs(dir_cat)
        f.close()
    except FileExistsError:
        print("Необходимые директории уже созданы")
    f.close()

""" после работы с проектом и добавления файлов или папок в проект можно обойти все методом os.walk и передать все
данные в рабочий файл Dir_configure """
