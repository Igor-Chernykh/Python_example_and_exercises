# формируется список из чисел
#  от 1 до 10 по порядку
# затем каждое четное число заменяется
# на $


mas = [i for i in range(1, 11)]
print(mas)
for i in range(len(mas)):
    if mas[i] % 2 == 0:
        mas[i] = "$"
print(mas)
