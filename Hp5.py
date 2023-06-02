# Напишите программу, которая на вход принимает два числа A и B, и возводит число
# А в целую степень B с помощью рекурсии.t
# *Пример:*
# A = 3; B = 5 -> 243 (3⁵)
#     A = 2; B = 3 -> 8

first_number = int(input('Введите первое число : '))
second_number = int(input('Введите вротое число : '))

def exponentiation(number_a, number_b):
    if number_b == 0:
        return 0
    return number_a * exponentiation(number_a,  number_b - 1)

print(exponentiation(first_number, second_number))

# Напишите рекурсивную функцию sum(a, b), возвращающую сумму двух целых неотрицательных чисел.
# Из всех арифметических операций допускаются только +1 и -1. Также нельзя использовать циклы.
# *Пример:*
# 2 2
#     4

first_number = int(input('Введите первое число : '))
second_number = int(input('Введите второе число : '))
def summ_numbers(number_a, number_b):
    if number_a == 0:
        return number_b
    return summ_numbers(number_a - 1, number_b + 1)

print(summ_numbers(first_number, second_number))