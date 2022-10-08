# Напишите программу для проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.

bool_values = ['000', '100', '010', '110', '001', '101', '011', '111']
vars_xyz = [False, False, False]
index = 0
letter = 0
result = None
while index < len(bool_values):
    while letter < len(bool_values[index]):
        vars_xyz[letter] = bool(int(bool_values[index][letter]))
        letter += 1
    result = not(vars_xyz[0] or vars_xyz[1] or vars_xyz[2]) == (not vars_xyz[0] and not vars_xyz[1] and not vars_xyz[2])
    print (f'X = {vars_xyz[0]}; Y = {vars_xyz[1]}; Z = {vars_xyz[2]}\n'
    f'Результат выражения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z равен: {result}\n')
    letter = 0
    index += 1