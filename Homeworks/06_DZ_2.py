# 2. пользователь должен ввести логин,пароль и подтвержение пароля
# пароль должен состоять минимум из 8 символов
# содержать букву и цифру
# программа проверяет пароль


# пользователь вводит логин
# пользователь вводит пароль
# вводит подтверждение пароля
# пароль проверяется на соответствие первому и наличию условий

# login = None
# password = None


def create_user(login):
    password = input("Vvedite parol\n")
    repeat_password = input("Vvedite parol povtorno\n")
    if proverka_sovpadeniya(password, repeat_password):
        finish(login)

def proverka_sovpadeniya(pass1, pass2):
    popitok = 0
    while pass1 != pass2 and popitok <= 3:
        print("paroli ne sovpadayut")
        popitok += 1
        pass1 = input("Vvedite parol\n")
        pass2 = input("Vvedite parol povtorno\n")

        if pass1 == pass2:
            print("paroli sovpadayut")
            proverka_trebovaniy(pass1)
        elif popitok == 3:
            print("zakonchilis popitki na segodnya")
        else:

        create_user(login)


def proverka_trebovaniy(password):
    pass
    # if password == 123:
    #     return


def finish(login):
    print("welcome", login)


create_user(input("Vvedite login\n"))
# finish(create_user())