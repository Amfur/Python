# Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.
# [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12
import random
amouth_nums = abs(int(input('Сколько чисел поместить в список? ')))
my_list = []
for i in range(amouth_nums):
    my_list.append(random.randint(0, 10))
print(my_list)
sum = 0
odd_elems = []
for i in range(1,len(my_list),2):
    sum += my_list[i]
    odd_elems.append(my_list[i])
print(f'Элементы на нечётных позициях: {odd_elems}\nИх сумма: {sum}')
