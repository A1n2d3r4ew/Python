# Петя, Катя и Сережа делают из бумаги журавликов. Вместе они сделали
# S журавликов. Сколько журавликов сделал каждый ребенок, если известно,
# что Петя и Сережа сделали одинаковое количество журавликов, а Катя
# сделала в два раза больше журавликов, чем Петя и Сережа вместе?

s = int(input("Введите число журавликов: "))
x = int(s / 3)
pet = int(x / 2)
ser = int(x / 2)
kat = int(x * 2)
print(f"Петя сделал: {pet}")
print(f"Сережа сделал: {ser}")
print(f"Катя сделала: {kat}")