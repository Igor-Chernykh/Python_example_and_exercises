# Регистрация нового пользователя
# у него есть логин и пароль
# (имя и пароль переменные глобальные,потому что они важные,
# они нам потом везде нужны)
# две функции, первая регает - спрашивает лог, пароль и записывает
# вторая делает проверку - 1и2 пасс совпадает
# и защита от ботов, проверку можно проводить 3 раза


login = ""
password = ""
popit = 0

def registr():
    global login
    login = input("Vvedite login\n")
    paroli()
    pass

def paroli():
    p1 = input("Vvedite parol\n")
    p2 = input("Vvedite parol povtorno\n")
    proverka(p1, p2)
    pass


def proverka(x, y):
    global password, popit
    if x == y:
        print("paroli sovpadayut")
        password = x
        finish()
    elif popit == 3:
        print("zakonchilis popitki na segodnya")
    else:
        print("paroli ne sovpadayut")
        popit += 1
        paroli()
    pass


def finish():
    print("welcome", login)


registr()
