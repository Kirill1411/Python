# Даны два файла, в каждом из которых находится запись многочлена.
# Задача - сформировать файл, содержащий сумму многочленов.

from pathlib import Path
import sympy


def get_coeff(my_poly: str):
    x = sympy.Symbol('x')
    my_poly = sympy.polys.polytools.poly_from_expr(my_poly)[0]
    a = []
    a = my_poly.all_coeffs()
    return a


path_1 = Path('file1.txt')
with open(path_1) as file_1:
    my_poly1 = file_1.read()
    a = get_coeff(my_poly1)
print(a)

path_2 = Path('file2.txt')
with open(path_2) as file_2:
    my_poly2 = file_2.read()
    b = get_coeff(my_poly2)
print(b)

c = abs(len(a) - len(b))
m = max(len(a), len(b))
res = []
if len(a) > len(b):
    for i in range(0, c):
        res.append(a[i])
    for i in range(0, m-1):
        res.append(a[i+c]+b[i])
else:
    for i in range(0, c):
        res.append(b[i])
    for i in range(0, m-1):
        res.append(a[i]+b[i+c])
print(res)

num = ''
for i in range(len(res)):
    if m > 2:
        num = num + f'{res[i]}*x**{m} + '
        m -= 1
    elif m == 2:
        num = num + f'{res[i]}*x + '
        m -= 1
    else:
        num = num + f'{res[i]}'

print(num)

with open('polynom.txt', 'w') as my_file:
    my_file.write(num)