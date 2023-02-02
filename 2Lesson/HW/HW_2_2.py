# Требуется вывести все целые степени двойки (т.е. числа вида 2k), не превосходящие числа N.

# Пример:

# 10 -> 1 2 4 8
#
number = int(input())
degree = 1

while degree < number:
    print(degree)
    degree *= 2
