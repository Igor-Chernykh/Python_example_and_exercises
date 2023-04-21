# находит все индексы элементов списка

spisok = ["cat", "dog", "turtle", "parrot", "dog"]
otvet = input("поиск\n")
for i in range(len(spisok)):
    if otvet == spisok[i]:
        print("ваше животное под номером", i)
