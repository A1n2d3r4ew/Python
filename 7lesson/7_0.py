# У вас есть код который вы не можете менять (так часто бывает,
# когда код в глубине программы используется множество раз и вы
# не хотите ничего сломать):

# transformation = <???>

# values = [2,3,5,7,11,13,17,19,23,29]# or any another list

# transoormed_values = list(map(transformation, values))

# Единственный способ вашего взаимодействия с эти кодом - 
# посредством задания функции transformation.

# Однако вы поняли, что для вашей текущей задачи вам не нужно
# никак преобразовывать список значений, а нужно получить его
# как есть.

# Напишите такое лямбда-выражение transformation, чтобы transformed_vaiues
# получился копией vaiues.

# Input:
# values = [1,23,42,'asdfg']
# transoormed_values = list(map(transformation, values))
# if values == transoormed_values:
#     print('ok')
# else:
#     print('fail')

# Output:
# ok

# lambda x: x

values = [1,23,42,'asdfg']
transformation = lambda x: x
transoormed_values = list(map(transformation, values))

if values == transoormed_values:
    print('ok')
else:
    print('fail')
