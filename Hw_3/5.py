# Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
# Пример:
# для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]



x = int(input('Введите число Фибоначчи: '))


def fib(n):
    if (n == 0):
        return 0
    elif (n == 1 or n == 2):
        return 1
    else:
        return fib(n- 1) + fib(n-2)


def negafib(n):
    if (n == 0):
        return 0
    elif (n == -1):
        return 1
    else:
        return (negafib(n+2) - negafib(n+1))


for i in range(-x, 0):
    print(negafib(i), end=' ')

for i in range(x + 1):
    print(fib(i), end=' ')
