# Задача 14: Требуется вывести все целые степени двойки
# (т.е. числа вида 2k), не превосходящие числа N.
# 50 -> 1, 2, 4, 8, 16, 32

num = int(input('введите число '))
for i in range(num):
    count = 2 ** i
    if count < num:
        print(count, end=', ')

