""" Задача 3.
Реализовать базовый класс Worker (работник).
определить атрибуты: name, surname, position (должность), income (доход);
последний атрибут должен быть защищённым и ссылаться на словарь, содержащий элементы: оклад и премия, например,
{"wage": wage, "bonus": bonus};
создать класс Position (должность) на базе класса Worker;
в классе Position реализовать методы получения полного имени сотрудника (get_full_name) и
дохода с учётом премии (get_total_income);
проверить работу примера на реальных данных: создать экземпляры класса Position, передать данные, проверить значения
атрибутов, вызвать методы экземпляров."""

dict_income = {
    'стажер': {"Оклад": 50000,
               "Бонус": 25000},
    'директор': {"Оклад": 150000,
                 "Бонус": 200000}
}


class Worker:

    def __init__(self, name, surname, position, _income):
        self.name = name
        self.surname = surname
        self.position = str.lower(position)
        self._income = _income


class Position(Worker):

    def __init__(self, name, surname, position, _income=None):
        super().__init__(name, surname, position, _income)
        if _income is None:
            self._income = dict_income[self.position]


    def get_full_name(self):
        result = f'{self.name} {self.surname}'
        return result

    def get_total_income(self):
        result = self._income
        return result


worker_1 = Position("Георгий", "Рыбаков", "стажер")
worker_2 = Position("Иван", "Рыбоедов", "директор")
worker_3 = Position("Стив", "Джобс", "учредитель", 10000000)

print(worker_1.name)
print(worker_1.surname)
print(worker_1.position)
print(worker_1.get_full_name())
print(worker_1.get_total_income())
print('\n')
print(worker_2.name)
print(worker_2.surname)
print(worker_2.position)
print(worker_2.get_full_name())
print(worker_2.get_total_income())
print('\n')
print(worker_3.name)
print(worker_3.surname)
print(worker_3.position)
print(worker_3.get_full_name())
print(worker_3.get_total_income())
