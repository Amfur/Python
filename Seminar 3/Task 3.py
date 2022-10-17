# Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.
# Пример:
# [1.1, 1.2, 3.1, 5, 10.01] => 0.19

import random

def float_list (size):
    size = abs(int(size))
    new_list = []
    for i in range(size):
        new_list.append(random.randint(0, 10) + round(random.random(), 2))
    return new_list

my_list = float_list(input('Размер списка: '))
print(my_list)

int_elem = None
diff = None
max = 0
min = 1
if len(my_list):
    for i in my_list:
        int_elem = int(i)
        diff = i - int_elem
        if diff > max:
            max = diff
        if diff < min:
            min = diff
    print(f'Разность: {round(max-min, 2)}')
else:
    print('Задан пустой список')