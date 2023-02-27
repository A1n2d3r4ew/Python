# Дано натуральное число N и последовательность 
# из N элементов. Требуется вывести эту последовательность
# в обратном порядке.

# 2 -> 3 4
# 4 3 

def rev_num(num):
    if num == 0:
        return ""
    nums = input()
    return rev_num(num - 1) + f"{nums} "


print(rev_num(int(input())))