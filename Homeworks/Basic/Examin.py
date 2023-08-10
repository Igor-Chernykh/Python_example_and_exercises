"""
БИЛЕТ 10
1. программа просит ввести любую строку, вы вводите строку,
в которой есть буквы и цифры
После этого создаются 2 файла, в первом все буквы из строки,
во втором все цифры
"""

mas = input("Введите буквы и цифры:\n")
mas_letters = []
mas_nums = []

if mas.isalnum():
    for elem in mas:
        if elem.isalpha():
            mas_letters.append(elem)
        else:
            mas_nums.append(elem)
else:
    print("Введите ТОЛЬКО буквы и цифры")

with open("letters.txt", "w", encoding="utf-8") as letters:
    letters.write(str(mas_letters).replace("[", "").replace("]", "").replace("'", "").replace(",", "").replace(" ", ""))

with open("nums.txt", "w", encoding="utf-8") as nums:
    nums.write(str(mas_nums).replace("[", "").replace("]", "").replace("'", "").replace(",", "").replace(" ", ""))
