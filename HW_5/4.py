# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.

from pathlib import Path
import itertools


def rle_1(text):
    for item, same in itertools.groupby(text):
        count = sum(1 for _ in same)
        yield item if count == 1 else str(count) + item


my_path = Path('input.txt')
with open(my_path, 'r') as input_text:
    input_text = input_text.read()
a = ''.join(rle_1(input_text))
print(a)

with open('output.txt', 'w') as output_file:
    output_file.write(a)