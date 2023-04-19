# задаем список из 30 элем случайных (от 10 до 50)
# находим первый  макс (самое большое число)
# второй макс и третий макс
# максимумы не должны повторяться

import random
from heapq import nlargest
mas = []
for i in range(30):
    r = random.randint(10, 50)
    mas.append(r)
print(mas)
mas.sort()
mas2 = set(mas)
max_res = nlargest(3, mas2)
print(max_res)

