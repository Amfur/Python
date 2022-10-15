# Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# Пример:
# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]

import random

def create_list(elems):
    elems = abs(int(elems))
    new_list = []
    for i in range(elems):
        new_list.append(random.randint(0,10))
    return new_list

size = input('На сколько элементов создать список? ')
my_list = create_list(size)
print(f'Созданный список:\n{my_list}')

def duos_prod(orig_list):
    prods_list = []
    if not(len(orig_list)%2):
        for i in range((len(orig_list)//2)):
            prods_list.append(orig_list[i] * orig_list[(-1)*(i+1)])
    else:
        for i in range((len(orig_list)//2)+1):
            prods_list.append(orig_list[i] * orig_list[(-1)*(i+1)])
    return prods_list

duos_list = duos_prod(my_list)
print(f'Произведения пар элементов:\n{duos_list}')