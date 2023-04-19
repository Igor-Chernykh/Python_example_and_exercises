# программа знает 4 марки автомобиля(какие хотите)
# программа спрашивает марку автомобиля,
# и пишет ссылку на оф сайт этой компании

car_brend_link = {
    "Volkswagen": "https://www.vw.com./en.html",
    "Porshe": "https://www.porsche.com/",
    "Nissan": "https://www.nissan-europe.com/",
    "Toyota": "https://www.toyota.com/",
    "Avtovaz": "https://www.lada.ru/"
}
response_car_brend = input("Type car brend for information\n")
if response_car_brend in car_brend_link:
    print("Information about car brend ", car_brend_link[response_car_brend])
