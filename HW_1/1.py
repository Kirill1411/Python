# Напишите программу, которая принимает на вход цифру, обозначающую день недели, и проверяет, является ли этот день выходным.

from enum import Flag
from sys import flags

a = int(input('Ведите цисло: '))
bool = False

if a == 6 or a == 7:
    bool = True
print (bool)
