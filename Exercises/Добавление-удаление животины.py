spisok = ["cat", "dog", "turtle", "parrot"]
otvet = input("1 - добавить 2 - удалить\n")
if otvet == "1":
    new = input("напишите животное\n")
    spisok.append(new)
    print(spisok)
elif otvet == "2":
    new = input("кого удалять?\n")
    try:
        spisok.remove(new)
    except:
        print("нет такого")
    print(spisok)
