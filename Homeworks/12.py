# в магазине продается 10 продуктов (список).
# для каждого продукта нужно сделать массив dict
# указать *имя* *цена за кг* *вес*
# вы набираете корзину, указываете какие продукты покупаете и сколько.
# в итоге видите вашу корзину и стоимость всего

kartofel = {"name": "картофель", "price": "22", "weight": ""}
ogurci = {"name": "огурцы", "price": "120", "weight": ""}
shampinioni = {"name": "шампиньоны", "price": "215", "weight": ""}
kurica = {"name": "курица", "price": "200", "weight": ""}
kolbasa = {"name": "колбаса", "price": "290", "weight": ""}
moloko = {"name": "молоко", "price": "80", "weight": ""}
sir = {"name": "сыр", "price": "480", "weight": ""}
tomati = {"name": "томаты", "price": "250", "weight": ""}
kapusta = {"name": "капуста", "price": "100", "weight": ""}
mintai = {"name": "минтай", "price": "538", "weight": ""}
goods = [kartofel, ogurci, shampinioni, kurica, kolbasa,
         moloko, sir, tomati, kapusta, mintai]


goods_name = "шампиньоны"
# goods_name = input("Введите название товара:\n")


while True:
    goods_name = input("Введите название товара что б добавить в корзину,"
                       "или 'завершить' что б сформировать список:\n")
    if goods_name in [elem["name"] for elem in goods]:  # проверяем что название товара есть в списке
        print(f"{goods_name} найден в списке")

        for i in goods:
            if goods_name in i.values():
                kg_price = int(i.get("price"))          # получаем значение цены за кило
                weight = int(input("Введите вес товара, кг:\n"))
                goods_price = weight * kg_price
                print(f"{goods_name}, {weight} кг, цена {goods_price}")
                print("Добавлено в корзину")
    elif goods_name == "завершить":
        print("запись в файл...")
        print("Список создан!")
        break

    else:
         print(f"{goods_name} не найден")
