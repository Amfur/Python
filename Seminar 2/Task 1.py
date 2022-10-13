def Sum_of_digits(num):
    sum = 0
    for char in num:
        if char != '.' and char != '-' and char != ',':
            sum += int(char)
    return sum

number = input('Введите вещественное число: ')
print(f'Сумма цифр введённого числа: {Sum_of_digits(number)}')