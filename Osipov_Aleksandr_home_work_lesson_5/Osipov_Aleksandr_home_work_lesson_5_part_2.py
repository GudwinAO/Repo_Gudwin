"""Задание 2.
* (вместо 1) Решить задачу генерации нечётных чисел от 1 до n (включительно), не используя ключевое слово yield."""

# создаем List Comprehensions используя рэндж с шагом 2
list_numb = [i for i in range(1, int(input('Введите число: ')) + 1, 2)]
print(list_numb)
