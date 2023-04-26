# 2. пользователь должен ввести логин,пароль и подтвержение пароля
# пароль должен состоять минимум из 8 символов
# содержать букву и цифру
# программа проверяет пароль
# пользователь вводит логин
# пользователь вводит пароль
# вводит подтверждение пароля
# пароль проверяется на соответствие первому и наличию условий


def get_user_password_one_time():
    password = input("Введите пароль\n")
    povtor_password = input("Введите пароль повторно\n")
    return password, povtor_password


def get_password_repeat():
    pass1, pass2 = get_user_password_one_time()
    popitok = 0
    while pass1 != pass2 and popitok < 3:
        popitok += 1
        print("Пароли не совпадают")
        pass1, pass2 = get_user_password_one_time()
    return pass1, pass2


def check_passwords(pass1, pass2):
    if pass1 == pass2:
        print("Пароли совпадают")
        if len(pass1) >= 8 and pass1.isalnum():
            print("Пароль соответствует требованиям")
            return True
        else:
            print("Пароль не соответствует требованиям")
            return False
    else:
        print("Закончились попытки на сегодня")
        return False


login = input("Введите логин\n")
if login:
    pass1, pass2 = get_password_repeat()
    if check_passwords(pass1, pass2) == True:
        print("Пользователь ", login, " зарегистрирован!")

    else:
        print("Регистрация неудачна")
