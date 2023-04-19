# Программа *игра в кости*
# первый игрок бросает два кубика(1-6) пока не выпадут
# одинаковые числа(например 5 5)
# потом второй игрок делает то же самое
# выиграл тот у кого числа на кубиках больше

import random

num1 = random.randint(1, 6)
num2 = random.randint(1, 6)
while num1 != num2:
    num1 = random.randint(1, 6)
    num2 = random.randint(1, 6)
print("У первого игрока выпала сумма ", num1 + num2)

num3 = random.randint(1, 6)
num4 = random.randint(1, 6)
while num3 != num4:
    num3 = random.randint(1, 6)
    num4 = random.randint(1, 6)
print("У второго игрока выпала сумма ", num3 + num4)

if num1 > num3:
    print("Первый игрок победил!")
elif num1 < num3:
    print("Второй игрок победил!")
else:
    print("Ничья!")
