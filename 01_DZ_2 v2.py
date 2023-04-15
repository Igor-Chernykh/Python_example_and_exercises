# программа знает 4 марки автомобиля(какие хотите)
# программа спрашивает марку автомобиля,
# и пишет ссылку на оф сайт этой компании

Volkswagen = "https://www.vw.com./en.html"
Porshe = "https://www.porsche.com/"
Nissan = "https://www.nissan-europe.com/"
Toyota = "https://www.toyota.com/"
Avtovaz = "https://www.lada.ru/"

response_car_brend = input("Введите марку авто \n")
if response_car_brend == "Volkswagen":
    print("Сайт бренда ", Volkswagen)
elif response_car_brend == "Porshe":
    print("Сайт бренда ", Porshe)
elif response_car_brend == "Nissan":
    print("Сайт бренда ", Nissan)
elif response_car_brend == "Toyota":
    print("Сайт бренда ", Toyota)
elif response_car_brend == "Avtovaz":
    print("Сайт бренда ", Avtovaz)
else:
    print("Такой бренд не найден")
