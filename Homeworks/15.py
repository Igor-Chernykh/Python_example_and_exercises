"""
Написать игру «Быки и коровы». Программа «загадывает» четырёхзначное
число и играющий должен угадать его.
После ввода пользователем числа программа сообщает,
сколько цифр числа угадано (быки) и сколько цифр угадано
и стоит на нужном месте (коровы).
После отгадывания числа на экран необходимо вывести количество
сделанных пользователем попыток.

Если не понятны правила игры *быки и коровы* посмотрите в интернете.
"""

import random
mas = [random.randint(0, 9) for i in range(4)]
print(mas)

num = input("Введите 4-х значное число:")
if num.isdigit() and len(num) == 4:
    num = list(num)
    print(num)
    pass
else:
    print("Число не 4-х значное. Введите правильно")

