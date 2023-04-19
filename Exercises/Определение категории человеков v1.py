try:
    age = int(input("Сколько тебе лет?\n"))
    sex = input("Какой пол(м/ж?)\n")
    if age < 18 and sex == "м":
        print("Ты школьник")
    elif age < 18 and sex == "ж":
        print("Ты школьница")
    elif 18 <= age <= 23 and sex == "м":
        print("Ты студент")
    elif 18 <= age <= 23 and sex == "ж":
        print("Ты студентка")
    elif 23 <= age < 75 and sex == "м":
        print("Ты работник")
    elif 23 <= age < 75 and sex == "ж":
        print("Ты работница")
    elif age >= 75 and sex == "м":
        print("Ты пенсионер")
    elif age >= 75 and sex == "ж":
        print("Ты пенсионерка")
    else:
        print("Данные введены неверно")
except:
    print("Введите корректные данные")
