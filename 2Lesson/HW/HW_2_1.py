# 2. Петя и Катя – брат и сестра. Петя – студент, а Катя –школьница.
# Петя помогает Кате по математике. Он задумывает два
# натуральных числа X и Y (X,Y≤1000), а Катя должна их отгадать. 
# Для этого Петя делает две подсказки. Он называет сумму этих чисел S и их
# произведение P. Помогите Кате отгадать задуманные Петей числа.

# Пример:

# 4 4 -> 2 2
# 5 6 -> 2 3

s = int(input())
p = int(input())
num = 0
num1 = 0

for i in range(0,10):
    for j in range(0,10):
        if s == (i + j):
            num = i
            num1 = j
            if p == (i * j) and num == i and num1 == j:
                
                print(num, num1)
                break # тут нужна Ваша помощь! Не могу понять как остановить цикл чтобы он дальше не считал после вывода.
                

