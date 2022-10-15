# Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.
# [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12
import random

def create_list(elems):
    elems = abs(int(elems))
    new_list = []
    for i in range(elems):
        new_list.append(random.randint(0, 10))
    return new_list

my_list = create_list(input('На сколько элементов создать список? '))
print(my_list)

sum = 0
odd_elems = []
for i in range(1,len(my_list),2):
    sum += my_list[i]
    odd_elems.append(my_list[i])
print(f'Элементы на нечётных позициях: {odd_elems}\nИх сумма: {sum}')
