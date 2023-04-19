import random
import time

summa_hum = 0   # ход игрока
print("Your turn")
for i in range(3):
    k1 = random.randint(1, 6)
    print("Выпало", k1)
    summa_hum += k1
    time.sleep(0.5)
print("Total score", summa_hum)

summa_comp = 0  # ход компа
print("Comp turn")
for i in range(3):
    k2 = random.randint(1, 6)
    print("Выпало", k2)
    summa_comp += k2
    time.sleep(0.5)
print("Total score", summa_comp)

if (summa_hum > summa_comp) and (summa_hum != 18) or (summa_comp == 18):  # кто победил
    print("You win!")
elif summa_hum < summa_comp:
    print("Comp win!")
else:
    print("Draw")
