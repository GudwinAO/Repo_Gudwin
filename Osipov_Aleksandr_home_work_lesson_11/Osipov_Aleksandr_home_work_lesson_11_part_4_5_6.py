""" Задание 4.
Начните работу над проектом «Склад оргтехники».
Создайте класс, описывающий склад. А также класс «Оргтехника», который будет базовым для классов-наследников.
Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс). В базовом классе определите параметры,
общие для приведённых типов.
В классах-наследниках реализуйте параметры, уникальные для каждого типа оргтехники.

5. Продолжить работу над первым заданием. Разработайте методы, которые отвечают за приём оргтехники на склад и передачу
в определённое подразделение компании. Для хранения данных о наименовании и количестве единиц оргтехники,
а также других данных, можно использовать любую подходящую структуру (например, словарь).

6. Продолжить работу над вторым заданием. Реализуйте механизм валидации вводимых пользователем данных.
Например, для указания количества принтеров, отправленных на склад, нельзя использовать строковый тип данных.
Подсказка: постарайтесь реализовать в проекте «Склад оргтехники» максимум возможностей, изученных на уроках по ООП."""


my_store_central = []
my_store_region = []
my_store_town = []


class StoreOffice:


    def __init__(self, name, price, quantity, location):
        self.name = name
        self.price = price
        self.quantity = quantity
        self.location = location

        self.my_unit = {
                        'Модель устройства': self.name,
                        'Цена за ед': self.price,
                        'Количество': self.quantity,
                        'Локация': self.location

                         }
    def reception(self):

        global my_store_central
        global my_store_region
        global my_store_town

        try:
            name = input(f'Введите наименование ')
            price = int(input(f'Введите цену за ед '))
            quantity = int(input(f'Введите количество '))
            location = input('Введите расположение техники: '
                             '"c" - центральный склад, "r" - региональный, "t" - городской: ')

            self.my_unit = {
                        'Модель устройства': name,
                        'Цена за ед': price,
                        'Количество': quantity,
                        'Локация': location
                         }

            if location == 'c':
                my_store_central.append(self.my_unit)
                return f'Текущий список -\n {my_store_central}'
            elif location == 'r':
                my_store_region.append(self.my_unit)
                return f'Текущий список -\n {my_store_region}'
            elif location == 't':
                my_store_town.append(self.my_unit)
                return f'Текущий список -\n {my_store_town}'
            else:
                print('Склад выбран неверно, повторите ввод данных')
                self.reception()


        except ValueError:

            return f'Ошибка ввода данных'

class Printer(StoreOffice):

    @property
    def get_print(self):
        return f'данное устройство печатает'


class Scanner(StoreOffice):

    @property
    def get_scan(self):
        return f'данное устройтсво сканирует'


class Copier(StoreOffice):

    @property
    def get_copier(self):
        return f'данное устройство копирует'


unit_1 = Printer('hp', 2000, 5, 'c')
unit_2 = Scanner('Canon', 1200, 1, 'r')
unit_3 = Copier('Xerox', 1500, 1, 't')

print(unit_1.reception())
print(unit_2.reception())
print(unit_3.reception())

print(unit_1.get_print)
print(unit_2.get_scan)
print(unit_3.get_copier)



