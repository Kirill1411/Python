#     Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.
#     Пример:
# - пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)

n = int(input('Введите число n: '))
factorial = (lambda a: 1 if a == 1 or a == 0 else a * factorial(a - 1))
list_1 = [factorial(i) for i in range(1, n + 1)]
print(list_1)