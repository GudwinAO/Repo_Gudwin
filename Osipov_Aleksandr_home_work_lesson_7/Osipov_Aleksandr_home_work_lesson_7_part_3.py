""" Задание 3.
Создать структуру файлов и папок, как написано в задании 2
(при помощи скрипта или «руками» в проводнике). Написать скрипт,
который собирает все шаблоны в одну папку templates, например:
|--my_project
   ...
  |--templates
   |   |mainapp
   |   |  |--base.html
   |   |  |--index.html
   |   |authapp
   |      |--base.html
   |      |--index.html
Примечание: исходные файлы необходимо оставить; обратите внимание,
что html-файлы расположены в родительских папках (они играют роль пространств имён);
предусмотреть возможные исключительные ситуации;
это реальная задача, которая решена, например, во фреймворке django.
"""

from os import path, mkdir, walk
from shutil import copytree

FOLDER = 'my_project'
NAME_DIR = 'templates'

if not path.isdir(NAME_DIR):
    mkdir(NAME_DIR)

for roots, dirs, files in walk(FOLDER):
    try:

        for file in files:
            if ".html" in file:
                dir_root = path.dirname(roots)
                copytree(dir_root, NAME_DIR, dirs_exist_ok=True)

    except FileNotFoundError:
        print('Часть файлов не читаема')
        continue












