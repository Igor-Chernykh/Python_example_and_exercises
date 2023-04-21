# находит все индексы элементов списка

spisok = ["cat", "dog", "turtle", "parrot", "dog"]
otvet = input("поиск\n")
k = 0
for i in range(len(spisok)):
    if otvet == spisok[i]:
        # можно делать проверки меньше-больше и т.д.
        print("ваше животное под номером", i)
        k += 1
if k == 0:
    print("таких нет")
