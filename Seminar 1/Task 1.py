# Напишите программу, которая принимает на вход цифру, обозначающую день недели, и проверяет, является ли этот день выходным.

day_number = int(input('Введите номер дня недели: '))
if 1 <= day_number <= 7:
    if day_number < 6:
        print('Будний день')
    else:
        print('Выходной')
else:
    print('Введённое значение не является номером дня недели')