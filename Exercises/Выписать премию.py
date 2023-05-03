import random

peoples = ["name1", "name2", "name3", "name4", "name5"]
x = input("Введите количество людей\n")
y = input("Введите сумму премии\n")
lucky = []

def f1():
    for i in range(x):
        r1 = random.choice(peoples)
        lucky.append(r1)


def f2(x, y):
    if len(lucky) == len(set(lucky)):
        print("ok")
    for i in lucky:
        print(i, "выписать премию", y, "рублей")
    pass

f1()
