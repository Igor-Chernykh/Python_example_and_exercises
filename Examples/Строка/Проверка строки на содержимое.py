pin = input("Введите пин-код\n")
if pin.isdigit() and len(pin) == 4:
    print("Корректный ПИН!")
else:
    print("Введите ПИН снова!\n")