# Напишите программу, которая принимает на вход координаты двух точек и находит расстояние между ними в 2D пространстве.

first_point = [int(input('x1 = ')), int(input('y1 = '))]
second_point = [int(input('x2 = ')), int(input('y2 = '))]
print(f'Заданы точки: ({first_point[0]};{first_point[1]}) и ({second_point[0]};{second_point[1]})')
distance = ((first_point[0] - second_point[0])*(first_point[0] - second_point[0]) + (first_point[1] - second_point[1])*(first_point[1] - second_point[1]))**0.5
print(f'Расстояние между точками: {distance}')