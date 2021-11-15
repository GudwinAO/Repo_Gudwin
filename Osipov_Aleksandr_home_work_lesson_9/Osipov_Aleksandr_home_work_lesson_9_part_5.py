""" Задача 5.
Реализовать класс Stationery (канцелярская принадлежность).
определить в нём атрибут title (название) и метод draw (отрисовка). Метод выводит сообщение «Запуск отрисовки»;
создать три дочерних класса Pen (ручка), Pencil (карандаш), Handle (маркер);
в каждом классе реализовать переопределение метода draw. Для каждого класса метод должен выводить уникальное сообщение;
создать экземпляры классов и проверить, что выведет описанный метод для каждого экземпляра."""


class Stationery:
    def __init__(self, title):
        self.title = title

    def drawing(self):
        print('Я способ отрисовки родительского класса')


class Pen(Stationery):
    def __init__(self, title):
        super().__init__(title)

    def drawing(self):
        print('Я рисую как ручка')


class Pencil(Stationery):
    def __init__(self, title):
        super().__init__(title)

    def drawing(self):
        print('Я рисую как карандаш')


class Handle(Stationery):
    def __init__(self, title):
        super().__init__(title)

    def drawing(self):
        print('Я рисую как маркер')


pen_1 = Pen('ЭрикКраузе')
pencil_1 = Pencil('Кохинор')
handle_1 = Handle('Тайгер')
print(pen_1.title)
print(pen_1.drawing())
print(pencil_1.title)
print(pencil_1.drawing())
print(handle_1.title)
print(handle_1.drawing())
