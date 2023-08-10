# Пользователь вводит с клавиатуры три числа.
# В зависимости от выбора пользователя программа выводит
# на экран сумму трёх чисел или произведение трёх чисел.

first_num = int(input("Введите первое число "))
second_num = int(input("Введите второе число "))
third_num = int(input("Введите третье число "))
operation = input("Выберите операцию: сложить или умножить?\n")
if operation == "сложить":
    print("Результат сложения", first_num+second_num+third_num)
elif operation == "умножить":
    print("Результат умножения", first_num*second_num*third_num)
else:
    print("Неизвестный оператор")
