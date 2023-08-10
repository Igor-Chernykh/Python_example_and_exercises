# 2*.написать функцию которая создает персонажа в игре
# в игре 3 класса *маг лучник воин
# 6 характеристик *сила выносливость ловкость харизма интеллект удача
# нужно задать какой у тебя *класс, *имя персонажа, *раса(эльф орк и тд)
# характеристики рандомятся,
# причем у воина 1и2 характеристика должны быть больше
# у лучника 3и4
# у мага 5и6
# сумма характеристик=30
# на выходе получается вот так:
#
# ваш персонаж: вальдемар воин орк
#
# сила         9
# выносливость 9
# ловкость     2
# харизма      3
# интеллект    2
# удача        5

def creation_charester():
    Name = choise_name()
    Race = choise_race()
    Class = choise_class()
    Stats = None
    return Name, Race, Class, Stats





def choise_name():
    name = input("Введите имя персонажа:\n")
    if name.isalpha() and name.istitle():
        return name
    else:
        print("Имя не соответствует требованиям")


def choise_race():
    race_list = ["Human", "Elf", "Dwarf", "Orc", "Troll", "Undead"]
    print("Доступные рассы:", race_list)
    race = input("Выберите рассу персонажа из доступных:\n")
    if race in race_list:
        return race
    else:
        print("Такой рассы нет в списке")


def choise_class():
    class_list = ["Warrior", "Mage", "Marksman"]
    print("Доступные классы:", class_list)
    char_class = input("Выберите класс персонажа из доступных:\n")
    if char_class in class_list:
        return char_class
    else:
        print("Такого класса нет в списке")
    stats = [strenght, stamina, agillity, har, intelligence, luck]


def create_stats():





Charester = creation_charester()
print(Charester)