# 1. На столе лежат n монеток. Некоторые из них лежат вверх решкой,
#  а некоторые – гербом. Определите минимальное число
# монеток, которые нужно перевернуть, чтобы все монетки
# были повернуты вверх одной и той же стороной. Выведите минимальное
# количество монет, которые нужно перевернуть
# Пример:

# 5 -> 1 0 1 1 0
# 2
#
coins = int(input())
coins_emblem = 0
coins_tails =int(0)

for i in range(coins):
    emb_tai = int(input())
    if emb_tai == 0:
        coins_tails += 1

print(f"Нужно перевернуть {coins_tails} монеты")