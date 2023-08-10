# из дз (задание с расписанием)
# сделать чтобы это расписание записывалось в файл
# *день недели
# *предметы

import random


def create_timetable(lesson_list, lesson_count):
    return random.sample(lesson_list, lesson_count)


def get_lessons_and_count(class_number):
    basic_school_lessons = ["subj1", "subj2", "subj3", "subj4"]
    middle_school_lessons = basic_school_lessons + ["subj5", "subj6", "subj7", "subj8"]
    high_school_lessons = middle_school_lessons + ["subj9", "subj10", "subj11", "subj12"]

    if 1 <= class_number <= 4:
        return basic_school_lessons, 3
    elif 5 <= class_number <= 8:
        return middle_school_lessons, 4
    elif 9 <= class_number <= 11:
        return high_school_lessons, 5
    else:
        print("Введите верное значение")
        return [], None


user_choise = int(input("Для какого класса составить расписание?\n"))
print("расписание для", user_choise, "класса:\n")


with open("07_DZ_1.txt", "a+", encoding="utf-8") as file:
    for i in range(1, 6):
        lesson_list, lesson_count = get_lessons_and_count(user_choise)
        timetable = str(("День", i, create_timetable(lesson_list, lesson_count))).replace("(", "").replace(")", "")+ "\n"
        file.write(timetable)

