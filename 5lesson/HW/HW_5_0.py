# Напишите программу, которая на вход принимает
# два числа А и В, и возводит число А в целую степень
# В с помощью рекурсии.

# А = 3; В = 5 -> 243 (3 в 5)

num = int(input())
deg = int(input())

def degree(a, b):
    if b == 1:
        return a
    return a * degree(a, b - 1)
    
print(degree(num, deg))