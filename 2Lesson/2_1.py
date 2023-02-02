# Дано натуральное число А > 1.Определите, каким по
# счету числом Фибоначчи оно является, то есть выведите
# такое число n, что Ф(n)=A.Если А не является числом 
# Фибоначчи, выведите число -1.

num = int(input())
fibonachi_1 = 0
fibonachi_2 = 1
count = 2

while count <= num:
    if num == fibonachi_2:
        print(count)
        break
    fibonachi_1, fibonachi_2 = fibonachi_2, fibonachi_1 + fibonachi_2
    count += 1
else:
    print(-1)
