# Дана последовательность чисел. Получить список уникальных элементов заданной последовательности.
# Пример:

# [1, 2, 3, 5, 1, 5, 3, 10] => [2, 10]

test_1 = [1, 2, 3, 5, 1, 5, 3, 10]
test = [x for x in test_1 if test_1.count(x) == 1]
print(test)
print([x for x in test_1 if test_1.count(x) == 1])