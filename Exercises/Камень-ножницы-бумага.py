import random
h = 0
c = 0
turn = ["k", "n", "b"]
win = ["kn", "nb", "bk"]
loose = ["kb", "nk", "bn"]
while True:
    hum = input("Ваш ход k-n-b \n")
    if hum =="stop":
        print("end game")
        break
    elif hum not in turn:
        print("переиграть")
        continue
    comp = random.choice(turn)
    result = hum+comp

    if result in win:
        h +=1
        print("Win!")
    elif result in loose:
        c +=1
        print("Looser!")
    else:
        print("Draw")
    print(hum,comp,result)
    print("Cчет ", h, ":", c)