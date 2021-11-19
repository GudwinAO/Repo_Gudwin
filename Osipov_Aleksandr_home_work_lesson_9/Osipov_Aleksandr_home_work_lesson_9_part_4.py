"""Задача 4.
Реализуйте базовый класс Car.
у класса должны быть следующие атрибуты: speed, color, name, is_police(булево). А также методы:
go, stop, turn(direction), которые должны сообщать, что машина поехала, остановилась, повернула (куда);
опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar;
добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля;
для классов TownCar и WorkCar переопределите метод show_speed. При значении скорости свыше 60 (TownCar) и
40 (WorkCar) должно выводиться сообщение о превышении скорости.

Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам, выведите результат.
Вызовите методы и покажите результат."""


class Car:
    def __init__(self, speed, color, name, is_police=False):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police


    def go(self):
        return "Машина поехала"

    def stop(self):
        return "Машина остановилась"

    def turn(self, direction):
        return f"Машина повернула {direction}"

    def show_speed(self):
        return f"Текущая скорость {self.speed}"



class TownCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        if int(self.speed) > 40:
            return "Вы превысили скорость"
        else:
            return f"Текущая скорость {self.speed}"



class WorkCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        if int(self.speed) > 40:
            return "Вы превысили скорость"
        else:
            return f"Текущая скорость {self.speed}"



class SportCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        return f"Текущая скорость {self.speed}"


class PoliceCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        return f"Текущая скорость {self.speed}"


town_car_1 = TownCar(85, 'Красненькая', 'Дэу Матиз', False)
work_car_1 = WorkCar(75, 'Белая', 'Камаз', False)
sport_car_1 = SportCar(285, 'Желтый', 'Ламбаргуни', True)
police_car_1 = PoliceCar(65, 'Бело-синий', 'Форд Фокус', False)

print(town_car_1.speed)
print(town_car_1.name)
print(town_car_1.color)
print(town_car_1.is_police)
print(town_car_1.show_speed())
print(town_car_1.go())
print(town_car_1.stop())
print(town_car_1.turn('Влево'))

print(sport_car_1.speed)
print(sport_car_1.name)
print(sport_car_1.color)
print(sport_car_1.is_police)
print(sport_car_1.show_speed())
print(sport_car_1.go())
print(sport_car_1.stop())
print(sport_car_1.turn('Влево'))

print(police_car_1.speed)
print(police_car_1.name)
print(police_car_1.color)
print(police_car_1.is_police)
print(police_car_1.show_speed())
print(police_car_1.go())
print(police_car_1.stop())
print(police_car_1.turn('Вправо'))

print(work_car_1.speed)
print(work_car_1.name)
print(work_car_1.color)
print(work_car_1.is_police)
print(work_car_1.show_speed())
print(work_car_1.go())
print(work_car_1.stop())
print(work_car_1.turn('Назад'))
