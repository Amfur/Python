# Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.
# Пример:
# [1.1, 1.2, 3.1, 5, 10.01] => 0.19

import random

def float_list (size):
    size = abs(int(size))
    new_list = []
    for i in range(size):
        new_list.append(round(random.randint(0, 10) + random.random(), 2))
    return new_list

my_list = float_list(input('Размер списка: '))
print(my_list)

frac = None
max = 0
max_el = None
min = 1
min_el = None
if len(my_list):
    for i in my_list:
        frac = i - int(i)
        if frac > max:
            max = frac
            max_el = i
        if frac < min:
            min = frac
            min_el = i
    print(f'Максимальная дробная часть: {max_el}\nМинимсальная дробная часть: {min_el}\nРазность дробных частей: {round(max-min, 2)}')
else:
    print('Задан пустой список')