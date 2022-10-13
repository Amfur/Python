# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
# Пример:
# 6782 -> 23
# 0,56 -> 11

def sum_of_digits(num):
    sum = 0
    for char in num:
        if char != '.' and char != '-' and char != ',':
            sum += int(char)
    return sum

number = input('Введите вещественное число: ')
print(f'Сумма цифр введённого числа: {sum_of_digits(number)}')