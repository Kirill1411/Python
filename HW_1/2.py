# Напишите программу для проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.

print('x y z    ¬(X ⋁ Y ⋁ Z)    ¬X ⋀ ¬Y ⋀ ¬Z')
for x in range(0, 2):
    for y in range(0, 2):
        for z in range(0, 2):
            array1 = not (x or y or z)
            array2 = not x and not y and not z
            print(x, y, z, '     ', array1, '        ', array2)
if array1 == array2:
    print('Утверждение (¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z) истинно')
else:
    print('Утверждение (¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z) ложно')