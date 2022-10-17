# Напишите программу, которая будет преобразовывать десятичное число в двоичное.
# Пример:
# 45 -> 101101
# 3 -> 11
# 2 -> 10

def dec_to_bin(num):
    num = int(num)
    if num < 0:
        num = abs(num)
        frac = 0
        bin = ''
        while num != 0:
            frac = num % 2
            bin = str(frac) + bin
            num //= 2
        bin = '-' + bin
    else:
        frac = 0
        bin = ''
        while num != 0:
            frac = num % 2
            bin = str(frac) + bin
            num //= 2
    return bin

binary = dec_to_bin(input('Введите число: '))
print(f'Его двоичная запись: {binary}')