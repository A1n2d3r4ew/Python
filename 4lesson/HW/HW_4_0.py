# Даны два неупорядочнных набора целых чисел (может быть с повторениями).
# Выдать без повторений в порядке возврастания все те числа, которые
# встречаются в обоих наборах. Пользователь вводит 2 числа. n-кол-во 
# элементов первого множества.m-кол-во элементов второго множества.
# Затем пользователь вводит сами элементы множеств.

# 11  6   
# 2 4 6 8 10 12 10 8 6 4 2
# 3 6 9 12 15 18

# 6 12

# string = set(list(input()))

# print(string)

n = int(input("Input: "))
m = int(input("Input: "))
# [int(i) for i in input().split()]
n_list = list()
m_list = list()

for i in range(n):
    x = int(input())
    n_list.append(x)
print(*n_list)

for i in range(m):
    x = int(input())
    m_list.append(x)
print(*m_list)

print(*sorted(set(n_list).intersection(m_list)))