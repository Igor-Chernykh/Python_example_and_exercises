# Пользователь вводит с клавиатуры числo X
# создается Х случайных чисел от 1 до 100,
# их все вывести на экран.
# Нужно посчитать отдельно сумму четных
# и сумму нечетных чисел

import random

sum_even = 0
sum_odd = 0
user_num = int(input("Введите количество генерируемых чисел\n"))

for i in range(user_num):
    num = random.randint(1, 100)
    print(num, end="  ")

    if num % 2 == 0:
        sum_even += num
    else:
        sum_odd += num

print("\nСумма четных {}, а сумма нечетных {}".format(sum_even, sum_odd))
