# Задайте список из n чисел последовательности (1+1/n)^n и выведите на экран их сумму.
# Пример:
# Для n = 6: {1: 2, 2: 2,25, 3: 2,37, 4: 2,44, 5: 2,49, 6: 2,52}

def sum_terms(num):
    list_terms = []
    sum = 0
    for n in range(1, num + 1):
        list_terms.append(round((1+1/n)**n, 2))
        sum += list_terms[n-1]
    return sum

n = int(input('Задайте максимальное значение n: '))
print(f'Сумма первых {n} членов последовательности: {sum_terms(n)}')