# Напишите рекурсивную функцию sum(a,b), возвращающую
# сумму двух целых неотрицательных чисел. Из всех арифметических
# операций допускается только +1 и -1. Также нельзя использовать
# циклы.

# 2 2
# 4

num1 = int(input())
num2 = int(input())

def sum(a, b):
    if b == 0:
        return a
    return sum(a + 1, b - 1)

if num1 > -1 and num2 > -1:
    print(sum(num1, num2))
else:
    print("input non-negative numbers")

