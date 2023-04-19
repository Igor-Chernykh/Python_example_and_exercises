colors = ["white", "black", "red", "blue", "pink", "grey"]
print(colors[3])    # Вывод элемента по номеру - 4

for i in range(len(colors)):    # Вывод всех элементов списка, работает через счетчик
    print("color", colors[i])

animals = ["кот", "пес", "попугай", "слон", "лошадь", "капибара"]
for i in range(len(animals)):
    print("У меня живет", animals[i])
