# Напишите программу, которая по заданному номеру четверти, 
# показывает диапазон возможных координат точек в этой четверти (x и y).

x = int(input('Введите номер четверти: '))

if x == 1:
    print ('координаты 1 четверти: по x = от 0 до бесконечности, по y = от 0 до бесконечности')
if x == 2:
    print ('координаты 2 четверти: по x = от 0 до -бесконечности, по y = от 0 до бесконечности')
if x == 3:
    print ('координаты 3 четверти: по x = от 0 до -бесконечности, по y = от 0 до -бесконечности')
if x == 4:
    print ('координаты 4 четверти: по x = от 0 до бесконечности, по y = от 0 до -бесконечности')