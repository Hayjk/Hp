#Найдите сумму цифр трехзначного числа.

#*Пример:*

#123 -> 6 (1 + 2 + 3)
#100 -> 1 (1 + 0 + 0) |

#number = int(input('Введите число: '))
#summ = 0

#while number > 0:
#    count = number % 10
#    summ = summ + count
#    number = number // 10

#print(f'Сумма чисел = {summ}')

#Петя, Катя и Сережа делают из бумаги журавликов.
# Вместе они сделали S журавликов. Сколько журавликов сделал каждый ребенок,
# если известно, что Петя и Сережа сделали одинаковое количество журавликов,
# а Катя сделала в два раза больше журавликов, чем Петя и Сережа вместе?

#*Пример:*

#6 -> 1  4  1
#24 -> 4  16  4
#60 -> 10  40  10

#s = int(input('Колличество журавликов = '))
#s = s / 6
#petr = s
#sergey = s
#ekaterina = s * 4

#print(f'Петя - {petr}, Катя - {ekaterina}, Срежа - {sergey}')

#Вы пользуетесь общественным транспортом?
# Вероятно, вы расплачивались за проезд и получали билет с номером.
# Счастливым билетом называют такой билет с шестизначным номером, где сумма первых трех
# цифр равна сумме последних трех. Т.е. билет с номером 385916 – счастливый,
# т.к. 3+8+5=9+1+6. Вам требуется написать программу, которая проверяет счастливость билета.

#*Пример:*

#385916 -> yes
#123456 -> no

#number = (input('Введите номер: '))

#firstNumbers = number[:3]
#lastNumbers = number[3:]
#firstSumm = 0
#lastSumm = 0

#while int(firstNumbers) > 0:
#    count = int(firstNumbers) % 10
#    firstSumm = firstSumm + count
#    firstNumbers = int(firstNumbers) // 10

#while int(lastNumbers) > 0:
#    count = int(lastNumbers) % 10
#   lastSumm = lastSumm + count
#    lastNumbers = int(lastNumbers) // 10

#if firstSumm == lastSumm:
#    print('Yes')
#else:
#    print('No')

#Требуется определить, можно ли от шоколадки размером n × m
# долек отломить k долек, если разрешается сделать один разлом по прямой между
# дольками (то есть разломить шоколадку на два прямоугольника).

#*Пример:*

#3 2 4 -> yes
#3 2 1 -> no

#n = int(input('Длинна шоколадки = '))
#m = int(input('Ширина шоколадки = '))
#k = int(input('Сколько долек нужно отломить = '))

#if k % n == 0 or k % m == 0 and (m * n) - k >0:
#    print('Yes')
#else:
#    print('No')