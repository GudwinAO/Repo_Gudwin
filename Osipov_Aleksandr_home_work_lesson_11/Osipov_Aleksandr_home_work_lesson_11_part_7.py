"""Задание 7.
Реализовать проект «Операции с комплексными числами». Создайте класс «Комплексное число».
Реализуйте перегрузку методов сложения и умножения комплексных чисел. Проверьте работу проекта.
Для этого создаёте экземпляры класса (комплексные числа), выполните сложение и умножение созданных экземпляров.
Проверьте корректность полученного результата."""


class ComplexNumber:
    def __init__(self, a, b):
        self.a = a
        self.b = b
        self.z = f'{a} + {b} * i'

    def __add__(self, other):
        return f'z = {self.a + other.a} + {self.b + other.b} * i'

    def __mul__(self, other):
        return f'z = {self.a * other.a - (self.b * other.b)} + {self.a*other.b + self.b * other.a} * i'


z_1 = ComplexNumber(12, 5)
z_2 = ComplexNumber(4, 8)
print(z_1.z)
print(z_2.z)
print(z_1 + z_2)
print(z_1 * z_2)
