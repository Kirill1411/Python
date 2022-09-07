# Задайте список из k чисел последовательности (1 + 1\k)^k и выведите на экран их сумму.

num = int(input('Введите число последовательности: '))
list = []
sum = 0

for k in range(1, num+1):
    list.append(round(pow((1+1/k), k), 2))
print(list)
for k in list:
    sum = sum + k
print(sum)
