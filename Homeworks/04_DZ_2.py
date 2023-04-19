# программа для поликлиники для животных:
# есть списки name=[] age=[] animal=[]
# то есть как зовут, возраст и что за животное
# вначале пусть будет два пациента
# надо сделать в программе возможность добавлять
# пациентов и удалять

name = ["Рыжик", "Рекс"]
age = [3, 8]
animal = ["Кот", "Пес"]
act = input("Что вы хотите сделать?\n 1 - Добавить животное в списки\n 2 - Удалить животное из списков\n")
if act == "1":
    add_name = input("Введите кличку питомца:\n")
    add_age = input("Введите возраст питомца:\n")
    add_animal = input("Введите вид животного:\n")
    name.append(add_name)
    age.append(add_age)
    animal.append(add_animal)
    print(name, age, animal)
elif act == "2":
    del_pet = input("Кого из животных убрать из списка?\n")
    for i in range(len(name)):
        if del_pet == name[i]:
            print("Ваше животное {}, {} удалено из списка!".format(name[i], animal[i]), end=" ")
            name.remove(name[i])
            age.remove(age[i])
            animal.remove(animal[i])
else:
    print("Выберите корректное действие")
