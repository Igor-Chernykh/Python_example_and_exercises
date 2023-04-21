# индекс находит только первое животное в списке
spisok = ["cat", "dog", "turtle", "parrot", "dog"]
otvet = input("поиск по названию\n")
if spisok.count(otvet) > 0:
    print("ваше животное под номером", spisok.index(otvet))
else:
    print("таких нет")
