car_list = ["car1", "car2", "car3", "car4", "car5", "car6", "car7", "car8", "car9", "car10"]
choise = input("Найти авто - 1\nДобавить авто - 2\n")
if choise == "1":
    search = input("Поиск авто:\n")
    if car_list.count(search) > 0:
        print("Это авто под номером:", car_list.index(search))
    else:
        print("Авто не найдено")
elif choise == "2":
    new_car = input("Введлите марку авто\n")
    car_list.append(new_car)
    print("Авто добавлено", car_list)
