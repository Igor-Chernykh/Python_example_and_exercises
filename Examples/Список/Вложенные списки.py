a = [1, 2, 3, 4]
b = [x for x in a]

c = [[1, 2], [3, 4], [5, 6]]
d = [x for xs in a for x in xs]

d = []
for xs in a:
   for x in xs:
       b.append(x)

new_list = [lst_item for lst_item in lst]
читаете это так: для каждого lst_item in lst добавьте lst_item к new_list

flattened_list = [item for sublist in nested_list for item in sublist]
читаете это так: добавьте каждый item из каждого sublist из nested_list

a = [[1,2],[3,4],[5,6]] - матрица 3х2

row1    1   2
row2    3   4
row3    5   6

b = [element for row in matrix for element in row]
Первый цикл for перебирает строки внутри матрицы, [1,2],[3,4],[5,6]т.е.
Второй цикл for перебирает каждый элемент в списке из 2 элементов.



[leaf for branch in tree for leaf in branch]
for branch in tree:
    for leaf in branch:
        yield leaf

[atom for galaxy in universe for star_system in galaxy for planet in star_system
for continent in planet for ecosystem in continent for forest in ecosystem
for tree in forest for branch in tree for leaf in branch for vein in leaf
for fibre in vein for cell in fibre for molecule in cell for atom in molecule]


