# Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
# Пример:
# для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]

from audioop import reverse

num = abs(int(input('Введите число: ')))
pos_list = [0, 1]
neg_list = [0, 1]
for i in range(2, num+1):
    pos_list.append(pos_list[i-1] + pos_list[i-2])
    neg_list.append(neg_list[i-2] - neg_list[i-1])
neg_list.reverse()
del neg_list[-1]
negafibo = neg_list + pos_list
print(negafibo)