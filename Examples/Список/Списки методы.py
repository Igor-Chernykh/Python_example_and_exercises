mas = [1, 2, 3, 4, 5]
mas.append(12)  # добавление в конец списка
print(mas)

mas.pop()   # удаление последнего элемента в списке
print(mas)

mas.pop(1)  # удаление по номеру элемента
print(mas)

mas2 = [6, 7, 8]
mas.extend(mas2)    # расширяет список на список добавляет в конец
print(mas)

mas.remove(4)   # удаление элемента по значению
print(mas)

sp = [1, 1, 1, 2, 2, 3]
print(sp.count(3))   # считает количество элементов в списке

m1 = max(mas)   # поиск максимального
m2 = min(mas)   # поиск минимального
print(m1, m2)

mas.reverse()   # развернуть список
print(mas)

mas.sort()      # сортировка от меньшего к большему
print(mas)
