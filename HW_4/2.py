# Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.
# "20" -> [2, 2, 5]

def find_prime_factors(n: int)->list:
    my_list = []
    i = 2
    while i <= n:
        if n % i == 0:
            my_list.append(i)
            n /= i
        else:
            i += 1
    return my_list

n = int(input('Задайте натуральное число: '))
print(f"Простые множители числа {n}: {find_prime_factors(n)}")
