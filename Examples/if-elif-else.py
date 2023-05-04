num = int(input("Введите число"))
if num > 0:
    if num > 10:
        print("Вы ввели число больше 10")
    else:
        print("Вы ввели число меньше 10 и больше 0")
else:
    print("Вы ввели число меньше 0")



num = input("Введите число")
A = "Yes" if num != "Test" else "No"
print(A)
