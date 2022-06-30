"""
Задание 4.
Написать скрипт, который выводит статистику для заданной папки в виде словаря,
в котором ключи — верхняя граница размера файла (пусть будет кратна 10), а значения —
общее количество файлов (в том числе и в подпапках), размер которых не превышает этой границы,
но больше предыдущей (начинаем с 0), например:
    {
      100: 15,
      1000: 3,
      10000: 7,
      100000: 2
    }
Тут 15 файлов размером не более 100 байт; 3 файла больше 100 и не больше 1000 байт...
Подсказка: размер файла можно получить из атрибута .st_size объекта os.stat.
5. * (вместо 4) Написать скрипт, который выводит статистику для заданной папки в виде словаря,
в котором ключи те же, а значения — кортежи вида (<files_quantity>, [<files_extensions_list>]), например:
  {
      100: (15, ['txt']),
      1000: (3, ['py', 'txt']),
      10000: (7, ['html', 'css']),
      100000: (2, ['png', 'jpg'])
    }
Сохраните результаты в файл <folder_name>_summary.json в той же папке, где запустили скрипт.
"""

from os import stat, path, walk

folder = r'C:\Program Files (x86)'
list_500 = []
list_5000 = []
list_25000 = []
list_50000 = []
list_50000_ = []


def get_size(x):
    if x <= 500:
        list_500.append(x)
    elif 500 < x <= 5000:
        list_5000.append(x)
    elif 5000 < x <= 25000:
        list_25000.append(x)
    elif 25000 < x <= 50000:
        list_50000.append(x)
    elif x >= 50000:
        list_50000_.append(x)


for roots, dirs, files in walk(folder):
    try:

        for file in files:
            file_root = path.join(roots, file)
            print(file_root)
            size_file = stat(path.join(file_root)).st_size
            get_size(size_file)
    except FileNotFoundError:
        print('Часть файлов не читаема')
        continue


dir_size = {
    '500': len(list_500),
    '5000': len(list_5000),
    '25000': len(list_25000),
    '50000': len(list_50000),
    '>50000': len(list_50000_)
}
print(f'Тут {len(list_500)} файлов до 500 байт, {len(list_5000)} файлов до 5 000 байт, {len(list_25000)} файлов до '
      f'25 000 байт, {len(list_50000)} файлов до 50 000 байт, {len(list_50000_)} более 50 000 байт \n', dir_size)
