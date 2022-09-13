# Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент,
# второй и предпоследний и т.д.
# Пример:
# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]

from random import randint


list = [randint(1,5) for i in range(int(input('Введите длину списка: ')))]
# list = [2, 3, 4, 5, 6] # Проверка на пример.
mix_list = []
for i in range((len(list)+1)//2):
    mix_list.append(list[i] * list[(len(list))-i-1])

print(list, end=' => ')
print(mix_list)
