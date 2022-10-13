# Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.
# Пример:
# пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)

def Set_of_prods(finish_num):
    prod = 1
    prods = []
    for num in range(1, finish_num + 1):
        prod *= num
        prods.append(prod)
    return(prods)

N = int(input('Введите число N: '))
print(f'Набор произведений чисел от 1 до {N}: {Set_of_prods(N)}')