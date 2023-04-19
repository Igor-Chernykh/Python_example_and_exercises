import random

count = 0
num = 0
while num < 6:
    count += 1
    num = random.randint(1, 6)
    print("Выпало", num)
print("Количество бросков", count)
