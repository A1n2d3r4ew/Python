# Хакер Высилий получил доступ к классному журналу и
# хочет заменить все свои минимальные оценки на 
# максимальные. Напишите программу, которая заменяет 
# оценки Василия, но наоборот: все максимальные - на 
# минимальные.

# 5 -> 1 3 3 3 4

# 1 3 3 3 1

# 8 

# 5 4 2 2 4 2 2 5


def max_to_min(n_list):
    min_n = min(n_list)
    max_n = max(n_list)
    return [min_n if i == max_n else i for i in n_list]
print(*max_to_min([int(i) for i in input().split()]))