# 2 Требуется найти в массиве A[1..N] самый близкий по величине
# элемент к заданному числу X. Пользователь в первой строке
# вводит натуральное число N – количество элементов в массиве. 
# В последующих строках записаны N целых чисел Ai. Последняя строка
# содержит число X

# Пример:

# 5
# 1 2 3 4 5
# 6
# -> 5
from random import randint


n = int(input("Введите кол-во элементов: "))
array = [randint(1, 50) for _ in range(n)]

print(array)

b = int(input())
m = min(array, key=lambda x: abs(x-b))
# m = array[0]

# for i in array: 
#     if abs(b - i) < abs(b - m):
#         m = i


print(m)



