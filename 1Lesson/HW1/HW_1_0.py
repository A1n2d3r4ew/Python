# Найдите сумму цифр трехзначного числа.

n = int(input("Введите трех значное число: "))

# if (n < 100 or n > 999):
#     print("Число не трехзначное")
# else:
#     print((n // 100) + (n // 10 % 10) + (n % 10))
resalt = 0
while (n != 0):
    resalt = resalt + n % 10
    n = n // 10
print(resalt)