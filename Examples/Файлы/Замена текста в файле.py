file = open("gubka.txt", "r", encoding="utf-8")
a = file.read().replace("Боб", "Чебурашка")

bob = open("bob.txt", "w+", encoding="utf-8")
bob.write(a)
file.close()
bob.close()
