num1 = int(input("Введите первое число\n"))
num2 = int(input("Введите второе число\n"))
operator = input("Chto delat? +-*/ \n")


def calculatons(a, act, b):
    if act == "+":
        return a + b
    elif act == "-":
        return a - b
    elif act == "*":
        return a * b
    elif act == "/":
        return a / b
    else:
        print("Неизвестный оператор. Повторите ввод\n")


result = calculatons(num1, operator, num2)
print("Результат вычислений: ", result)
