""" Задание 2. Реализовать проект расчёта суммарного расхода ткани на производство одежды.
Основная сущность (класс) этого проекта — одежда, которая может иметь определённое название.
К типам одежды в этом проекте относятся пальто и костюм. У этих типов одежды существуют параметры: размер (для пальто)
и рост (для костюма). Это могут быть обычные числа: V и H, соответственно.
Для определения расхода ткани по каждому типу одежды использовать формулы: для пальто (V/6.5 + 0.5),
для костюма(2*H + 0.3). Проверить работу этих методов на реальных данных.
Выполнить общий подсчёт расхода ткани. Проверить на практике полученные на этом уроке знания.
Реализовать абстрактные классы для основных классов проекта и проверить работу декоратора @property.
"""

# абстрактный класс "Одежда"


class Clothes:

    def __init__(self, param):
        self.param = param

    @property
    def expense_ct(self):
        result = (self.param / 6.5) + 0.5
        return result

    @property
    def expense_sq(self):
        result = 2 * self.param + 0.3
        return result

    def __add__(self, other):
        return self.expense_ct + other.expense_sq


class Coat(Clothes):
    def __init__(self, param):
        super().__init__(param)

    def __str__(self):
        return f'Объем ткани на пальто {self.expense_ct}'


class Suit(Clothes):
    def __init__(self, param):
        super().__init__(param)

    def __str__(self):
        return f'Объем ткани на костюм {self.expense_sq}'


coat_1 = Coat(38)
suit_1 = Suit(1.70)
print(coat_1.expense_ct)
print(suit_1.expense_sq)
print(coat_1 + suit_1)
