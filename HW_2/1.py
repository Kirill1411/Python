# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.

# Пример:

# - 0,56 -> 11

x = input('Введите вещественное число: ')
result = 0
for i in range(len(x)):
    if x[i] == ',' or x[i] == '.':
        result = result
    else:
        result = result + int(x[i])
print(result)