# Напишите программу, удаляющую из текста все слова, содержащие ""абв"".

st1 = 'Привет, Мир! Мы очабв любим Пайтонабв! тебя!'

res = list(filter(lambda x: 'абв' not in x, st1.split()))
print(' '.join(res))

