# Задайте последовательность чисел. Напишите программу, которая выведет список
# неповторяющихся элементов исходной последовательности.
# [1, 1, 2, 3, 4, 5, 5] -> [2, 3, 4]

from random import randint


my_list = [randint(1, 7) for i in range(7)]
list = []
print(my_list)
for i in range(len(my_list)):
    count = 0
    j = 0
    while j < len(my_list):
        if my_list[i] == my_list[j] and i != j:
            count = 1
            break
        else:
            j += 1
    if count == 0:
        list.append(my_list[i])
print(list)