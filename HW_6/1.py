# Напишите программу, которая принимает на вход число N и
# выдаёт последовательность из N членов.

# *Пример:*
# - Для N = 5: 1, -3, 9, -27, 81
#  1*-3, *-3, * -3

number = int(input('Ввелите число N: '))
x = -3
# res = list(map(lambda res: x**(res), [i for i in range(number)]))

# print(res)
print(list(map(lambda res: x**(res), [i for i in range(number)])))