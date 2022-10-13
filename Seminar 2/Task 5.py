# Реализуйте алгоритм перемешивания списка.

elems = abs(int(input('Задайте размер списка: ')))
my_list = []
for i in range(elems):
    my_list.append(input(f'Элемент с индексом {i}: '))
print(f'Заданный список: {my_list}')
my_set = set(my_list)
my_list = list(my_set)
print(f'Перемешанный список: {my_list}')