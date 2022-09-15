# Задана натуральная степень k. Сформировать случайным образом список коэффициентов
# (значения от 0 до 100) многочлена и записать в файл многочлен степени k.
# Пример:
# k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0

from random import randint

def polynomial(k:int)->str:
    i = 1
    res = str(randint(0, 101))
    while i <= k:
        num = randint(0, 101)
        if num != 0:
            if i == 1:
                res = f'{str(num)}*x + {res}'
            else:
                res = f'{str(num)}*x**{i} + {res}'
        i += 1
    res = res + ' = 0'
    return res

k = int(input('Введите cтепень: '))
list = polynomial(k)
with open ('Степень .txt','w') as my_file:  # записывает в файл
    my_file.write(f'k = {k} => {list} \n')
with open ('Степень .txt','r') as my_file:  # выводит в консоле
    print(my_file.read())
