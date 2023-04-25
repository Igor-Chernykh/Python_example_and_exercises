login = input("dcxvb")
password = input("dfg")
povtor_password = input("dfsghn")

if login:
    try:
        popitok = 0
        while password != povtor_password and popitok <= 3:
            popitok += 1
            print("paroli ne sovpadayut")
            password = input("Vvedite parol\n")
            povtor_password = input("Vvedite parol povtorno\n")

        if password == povtor_password:
            print("paroli sovpadayut")
            try:



        else popitok == 3:
                print("zakonchilis popitki na segodnya")

    except:
        print("Login not OK!")



if len(password) <= 8 and