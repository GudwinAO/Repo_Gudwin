# Домашнее задание. 2 часть.

""" а) Создать список, состоящий из кубов нечётных чисел от 1 до 1000 (куб X - третья степень числа X):
 Вычислить сумму тех чисел из этого списка, сумма цифр которых делится нацело на 7.
 Например, число «19 ^ 3 = 6859» будем включать в сумму, так как 6 + 8 + 5 + 9 = 28 – делится нацело на 7.
 Внимание: использовать только арифметические операции!
 б) К каждому элементу списка добавить 17 и заново вычислить сумму тех чисел из этого списка, сумма цифр которых делится нацело на 7*.
 * Решить задачу под пунктом b, не создавая новый список."""

# создаем наш список кубов нечетных чисел чисел. Список пуст, циклом добавим в него данные
numbers_list = []

# объявляем переменную - первое число
number = 1

# запускаем цикл по перебору чисел от 1 до 1000. Определяем нечетные, возводим в куб и добавляем в список
while (number <= 1000):
    tailing = number % 2
    if tailing != 0:
        result_number = number ** 3
        numbers_list.append(result_number)
        number += 1
    else:
        number += 1

# вычисляем длину получившегося списка для работы с циклом перебора.
length_list = len(numbers_list)

# объявляем переменную - позицию числа в списке для работы цикла.
position_number = 0

# запускаем цикл по перебору чисел, сложению составных чисел, делению без остатка на 7 и выведению результата.
while position_number < length_list:
    target_number = numbers_list[position_number]
    last_number = 0
    sum_number = 0

    while target_number != 0:
        last_number = target_number % 10
        sum_number += last_number
        target_number = target_number // 10
    target_number = numbers_list[position_number]
    tale_sum = sum_number % 7

    if tale_sum == 0:
        print('Искомая цифра по условию 1:', target_number)
        position_number += 1

    else:
        position_number += 1

# б) часть задачи. Добавляем к каждому значению внутри списка +17 без создания нового списка с помощью цикла.
position_number = 0
while position_number < length_list:
    numbers_list[position_number] = numbers_list[position_number] + 17
    position_number += 1

# значения в списке заменены - запускаем цикл аналогично условию а и выводим результат.
position_number = 0
while position_number < length_list:
    target_number = numbers_list[position_number]
    last_number = 0
    sum_number = 0

    while target_number != 0:
        last_number = target_number % 10
        sum_number += last_number
        target_number = target_number // 10
    target_number = numbers_list[position_number]
    tale_sum = sum_number % 7

    if tale_sum == 0:
        print('Искомая цифра по условию 2:', target_number)
        position_number += 1

    else:
        position_number += 1