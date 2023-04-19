otvet = input("Нравится активный отдых?\n")
if otvet == "да":
    otvet2 = input("Поедешь на дачу?\n")
    if otvet2 == "да":
        print("Едете на дачу!")
    else:
        print("Катаетесь на самокате!")
else:
    otvet3 = input("Смотрите кино?\n")
    if otvet3 == "да":
        print("Вы идете в кинотеатр.")
    else:
        print("Вы идете в музей.")
