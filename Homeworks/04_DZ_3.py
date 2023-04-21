# задаем список из 30 элем случайных (от 10 до 50)
# находим первый  макс (самое большое число)
# второй макс и третий макс
# максимумы не должны повторяться

import random
# Первый способ
mas = [random.randint(10, 50) for i in range(30)]
print(mas)
mas = list(set(mas))
mas.sort()
for i in range(-3, 0):
    print(mas[i])

# Второй способ
from heapq import nlargest
max_res = nlargest(3, mas)
print(max_res)
