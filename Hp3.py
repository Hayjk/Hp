# Требуется вычислить, сколько раз встречается некоторое число X в массиве
# A[1..N]. Пользователь в первой строке вводит натуральное число N – количество элементов в массиве.
# В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X
# *Пример:*
# 5
# 1 2 3 4 5
# 3
# -> 1

from random import randint

lenth_list = int(input('Введите длину списка : '))

number = []
for i in range(1):
    number.append(int(input('Ведите число которое хотите проверить : ')))

my_list = []
for j in range(lenth_list):
    my_list.append(randint(1, lenth_list))

count = 0
for k in range(len(my_list)):
    if my_list[k] == number[i]:
        count += 1

print(f'Исходный список : {my_list}')
print(f'Цифра {number} встречается {count} раз')

# Требуется найти в массиве A[1..N] самый близкий по величине элемент к заданному числу X.
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве. В последующих
# # строках записаны N целых чисел Ai. Последняя строка содержит число X
# *Пример:*
# 5
# 1 2 3 4 5
# 6
# -> 5

lenth_list = int(input('Введите длину списка : '))
my_list = []
for i in range(lenth_list):
    my_list.append(randint(1, lenth_list))
print(f'Исходный список : {my_list}')

number = []
for j in range(1):
    number.append(int(input('Введите число : ')))

max_value = 0
min_value = lenth_list + 1
for i in range(len(my_list)):
    if my_list[i] > max_value:
        max_value = my_list[i]
    elif my_list[i] < min_value:
        min_value = my_list[i]

for j in range(len(number)):
    if number[j] > max_value:
        print(f'Ближайшее значение к числу {number} : {max_value}')
    elif number[j] < min_value:
        print(f'Ближайшее значение к числу {number} : {min_value}')
    elif min_value < number[j] < max_value:
        for i in range(len(my_list)):
            if number[j] == my_list[i]:
                print(f'Ближайшее значение к числу {number} : {my_list[i]}')
    else:
        print(f'Числа {number} в списке нет')

#  В настольной игре Скрабл (Scrabble) каждая буква имеет определенную ценность.
# В случае с английским алфавитом очки распределяются так:A, E, I, O, U, L, N, S, T, R – 1 очко; D, G – 2 очка;
# B, C, M, P – 3 очка; F, H, V, W, Y – 4 очка; K – 5 очков; J, X – 8 очков; Q, Z – 10 очков.
# А русские буквы оцениваются так: А, В, Е, И, Н, О, Р, С, Т – 1 очко; Д, К, Л, М, П, У – 2 очка;
# Б, Г, Ё, Ь, Я – 3 очка; Й, Ы – 4 очка; Ж, З, Х, Ц, Ч – 5 очков; Ш, Э, Ю – 8 очков;
# Ф, Щ, Ъ – 10 очков. Напишите программу, которая вычисляет стоимость введенного пользователем слова.
# Будем считать, что на вход подается только одно слово, которое содержит либо только английские, либо только русские буквы.
# *Пример:*
# ноутбук
# 12

dictionary = {1: 'AEIOULNSTRАВЕИНОРСТ',
              2: 'DGДКЛМПУ',
              3: 'BCMPБГЁЬЯ',
              4: 'FHVWYЙЫ',
              5: 'KЖЗХЦЧ',
              8: 'JXШЭЮ',
              10: 'QZФЩЪ'}

word = input('Введите слово : ').upper()
summ = 0

for letter in word:
    for key, value in dictionary.items():
        if letter in value:
            summ += key

print(f'Слово {word} стоит {summ} очков')
