# в магазине продается 10 продуктов (список).
# для каждого продукта нужно сделать массив dict
# указать *имя* *цена за кг* *вес*
# вы набираете корзину, указываете какие продукты покупаете и сколько.
# в итоге видите вашу корзину и стоимость всего

kartofel = {"name": "картофель", "price": "22", "weight": "1"}
ogurci = {"name": "огурцы", "price": "120", "weight": "1"}
shampinioni = {"name": "шампиньоны", "price": "215", "weight": "1"}
kurica = {"name": "курица", "price": "200", "weight": "1"}
kolbasa = {"name": "колбаса", "price": "290", "weight": "1"}
moloko = {"name": "молоко", "price": "80", "weight": "1"}
sir = {"name": "сыр", "price": "480", "weight": "1"}
tomati = {"name": "томаты", "price": "250", "weight": "1"}
kapusta = {"name": "капуста", "price": "100", "weight": "1"}
mintai = {"name": "минтай", "price": "538", "weight": "1"}
goods = [kartofel, ogurci, shampinioni, kurica, kolbasa,
         moloko, sir, tomati, kapusta, mintai]

n = 0
total_price = 0
file = open("12_DZ.txt", "w")
file.close()

while True:
    with open("12_DZ.txt", "a+", encoding="utf-8") as file:
        goods_name = input("Введите название товара что б добавить в корзину,"
                           "или 'завершить' что б сформировать список:\n")
        if goods_name in [elem["name"] for elem in goods]:  # проверяем что название товара есть в словаре
            # print(f"{goods_name} найден в списке")
            for i in goods:
                if goods_name in i.values():
                    kg_price = float(i.get("price"))  # получаем значение цены за кило
                    weight = float(input("Введите вес товара, кг:\n"))
                    goods_price = weight * kg_price
                    n = n + 1
                    total_price = total_price + goods_price
                    print(f"{goods_name}, {weight} кг, цена {goods_price}")
                    shop_cart = str((n, ".", goods_name, weight, "кг", "цена", goods_price)).replace(
                        "(", "").replace(")", "").replace(",", "").replace("'", "") + "\n"
                    file.write(shop_cart)
                    print("Добавлено в корзину")
        elif goods_name == "завершить":
            print("запись в файл...")
            itog = str(("Итого:", total_price, "руб")).replace("(", "").replace(")", "").replace(
                ",", "").replace("'", "")
            file.write(itog)
            print("Список создан!")
            break

        else:
            print(f"{goods_name} не найден")
