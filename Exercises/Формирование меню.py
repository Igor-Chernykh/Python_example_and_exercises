import random

pervoe = ["суп", "борщ", "окрошка", "солянка", "крем-суп"]
vtoroe = ["картошка", "котлеты", "отбивные", "макароны", "гречка"]
napitok = ["чай", "компот", "фанта", "кола", "пепси"]

r1 = random.choice(pervoe)
r2 = random.choice(vtoroe)
r3 = random.choice(napitok)

print("У нас в меню {}, {}, {}".format(r1, r2, r3))
