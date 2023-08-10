"""
Задание 1
Выведите на экран надпись Nothing will work unless you do.
на разных строках. Пример вывода:
    Nothing
    will work
    unless you do.
"""

print(" Nothing\n", "will work\n", "unless you do\n")


"""
Задание 2
Выведите на экран надпись " Anyone who stops learning is old,
whether at twenty or eighty" Henry Ford на разных строках. 
Пример вывода:
“Anyone who 
    stops
        learning is old,
            whether at twenty or eighty”.
                                    Henry Ford
"""
# сделать через табуляцию и экранировать символ
print(" Anyone who\n", "    stops\n", "       learning is old,\n", "          whether at twenty or eighty.\n", "                                Henry Ford")


"""
Задание 3
Пользователь вводит с клавиатуры два числа. Необходимо 
найти сумму чисел, разницу чисел, произведение числе. 
Результат вычислений вывести на экран.
"""

first_num = int(input("Введите первое число\n"))            # сделать один вызов функции
second_num = int(input("Введите второе число\n"))
print("Сумма", first_num+second_num)
print("Разница", first_num-second_num)
print("Произведение", first_num*second_num)


"""
Задание 4
Пользователь вводит с клавиатуры два числа. 
Первое число — это значение, второе число процент, 
который необходимо посчитать. Например, мы ввели с клавиатуры 50 и 10.
Требуется вывести на экран 10 процентов от 50.
Результат: 5
"""

first_num = int(input("Введите первое число\n"))        # исправить нейминг, применить округление
second_num = int(input("Введите процент\n"))
print(f"{second_num} процент/ов от числа {first_num} составляет/ют {first_num/100 * second_num}")

"""
Задание 5
Напишите программу, вычисляющую площадь прямоугольника. 
Пользователь с клавиатуры вводит ширину и высоту прямоугольника.
"""
# сделать с нецелыми числами, применить округление
rectangle_width = int(input("Введите ширину прямоугольника\n"))
rectangle_height = int(input("Введите высоту прямоугольника\n"))
print(f"Площадь прямогульника равна {rectangle_width*rectangle_height}")
