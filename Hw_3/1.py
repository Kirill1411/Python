# Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.
# Пример:
# - [2, 3, 5, 9, 3] -> на нечётных индексы элементы 3 и 9, ответ: 12


from random import randint


list = [randint(0, 10) for i in range(5)]
print(list, end=' -> ')
end_sum = 0

for i in range(len(list)):
    if i % 2 != 0:
        end_sum += list[i]

print(end_sum)
