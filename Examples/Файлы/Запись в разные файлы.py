def record_to_file(file):
    a = input("Введите имя\n")
    file.write(a)


file1 = open("aaa.txt", "w+", encoding="utf-8")     # открываем и создаем файлы
file2 = open("bbb.txt", "w+", encoding="utf-8")
file3 = open("ccc.txt", "w+", encoding="utf-8")

record_to_file(file1)
record_to_file(file2)
record_to_file(file3)

file1.close()
file2.close()
file3.close()
