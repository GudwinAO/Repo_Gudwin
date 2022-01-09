"""Задание 1.
Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде строки формата «день-месяц-год».
В рамках класса реализовать два метода. Первый, с декоратором @classmethod.
Он должен извлекать число, месяц, год и преобразовывать их тип к типу «Число».
Второй, с декоратором @staticmethod, должен проводить валидацию числа, месяца и года (например, месяц — от 1 до 12).
Проверить работу полученной структуры на реальных данных."""


class Data:
    def __init__(self, day_month_year):
        self.data = day_month_year

    @classmethod
    def date_format(cls, day_mount_year):
        result_date = day_mount_year.split('.')
        if '.' not in day_mount_year or '/' in day_mount_year or len(result_date) < 3:
            return 'Дата введена не по форме. Используйте "." как разделитель'
        else:
            return int(result_date[0]), int(result_date[1]), int(result_date[2])

    @staticmethod
    def valid_date(day_mount_year):
        result_date = day_mount_year.split('.')
        if 1 <= int(result_date[0]) <= 31:
            if 1 <= int(result_date[1]) <= 12:
                if len(result_date[2]) == 4 and int(result_date[2]) < 2022:
                    return f'Дата корректна'
                else:
                    return f'Год {result_date[2]} введен неверно'
            else:
                return f'Месяц {result_date[1]} введен неверно'
        else:
            return f'День {result_date[0]} введен неверно'


a = input('Введите дату в формате "дд.мм.гггг": ')

data_1 = Data(a)

print(data_1.data)
print(Data.date_format(a))
print(Data.valid_date(a))
