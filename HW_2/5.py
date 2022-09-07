# Реализуйте алгоритм перемешивания списка.

from random import randint


def get_list() -> list:
    my_list = []
    for i in range(10):
        my_list.append(randint(1, 100))
    print(my_list)
    return my_list


def mix_list(set_list: list):
    for i in range(len(set_list)):
        r = randint(0, len(set_list)-1)
        t = set_list[i]
        set_list[i] = set_list[r]
        set_list[r] = t
    print(set_list)


new_list = get_list()
mix_list(new_list)