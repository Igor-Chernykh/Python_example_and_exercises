a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]

"""Цикл for"""
for elem in a:
    if elem < 5:
        print(elem)

"""лямбда-функции"""
print(list(filter(lambda elem: elem < 5, a)))

"""списковое включение"""
print([elem for elem in a if elem < 5])
