# Задайте список из N элементов, заполненных числами из промежутка [-N, N]. Найдите произведение элементов на введенных пользователем позициях.

N = abs(int(input('Задайте размер списка: ')))
count = N
interval = []
elem = None
while count != 0:
    elem = int(input(f'Осталось ввести: {count}\nВведите значение от {-N} до {N}: '))
    if -N <= elem <= N:
        interval.append(elem)
        count -= 1
print(interval)
if len(interval) != 0:
    count = abs(int(input('Введите количество множителей: ')))
    prod = 1
    indexes = []
    while count != 0 and len(interval) != 0:
        elem = int(input(f'Осталось ввести: {count}\nВведите позицию элемента: '))
        if elem in range(len(interval)) and elem >= 0:
            indexes.append(elem)
            prod *= interval[elem]
            count -= 1
    print(indexes)
    print(f'Произведение элементов на введённых позициях: {prod}')
else:
    print('Задан пустой список. Расчёт произведения невозможен')