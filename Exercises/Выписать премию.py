import random

peoples = ["name1", "name2", "name3", "name4", "name5"]
x = input("Введите количество людей\n")
y = input("Введите сумму премии\n")


def f1(x, y):
    for i in range(x):
        r1 = []
    k = 0
    while k < x:
        r1 = random.choice(peoples)
        k += 1
        print("Выплатить {} рублей для".format(y, r1))


f1(x, y)
