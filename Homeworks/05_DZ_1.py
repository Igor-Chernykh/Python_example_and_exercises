# 1.существует 3 списка со школьными предметами
# ['чтение','пение','рисование','математика'] 1-4класс
# [здесь 8 предметов]5-8класс
# [здесь 12 предметов]9-11класс

# написать функцию которая создает расписание на 5 дней
# нужно указать *номер класса
# для 1го списка 3 урока в день
# для 2го 4 урока в день
# для 3го 5 уроков в день
# уроки выбираются случайно
# .choice(spisok) <-случайный выбор из списка библиотеке random

import random

les4 = ["subj1", "subj2", "subj3", "subj4"]

les8 = ["subj1", "subj2", "subj3", "subj4",
        "subj5", "subj6", "subj7", "subj8"]

les11 = ["subj1", "subj2", "subj3", "subj4", "subj5", "subj6",
         "subj7", "subj8", "subj9", "subj10", "subj11", "subj12"]

DAY_PER_WEEK = 5
les_p_day4 = 3
les_p_day8 = 4
les_p_day11 = 5


def user_choise():
    if choise == "1":
        timetable(les_p_day4, les4)
    elif choise == "2":
        timetable(les_p_day8, les8)
    elif choise == "3":
        timetable(les_p_day11, les11)
    else:
        print("Введите верное значение")

def timetable(les_p_day, les):
    for i in range(1, 6):
        day_les = random.sample(les, les_p_day)
        print("День", i, day_les)


choise = input("Для каких классов составить расписание?\n 1 - 1-4 класс\n 2 - 5-8 класс\n 3 - 9-11 класс\n")
user_choise()

# tue_les = timetable(я не знаю что тут писать)
# print(tue_les)
# wed_les = timetable(les_p_day, les)
# print(wed_les)
# thu_les = timetable(les_p_day, les)
# print(thu_les)
# fri_les = timetable(les_p_day, les)
# print(fri_les)






# def timetable(les_p_day, les):
#    def rasp_dnya(les_p_day, les):
#         day_les = random.sample(les, les_p_day)
#         print(day_les)
#         return day_les
#     mon_les = rasp_dnya()
#     print(mon_les)
