f1 = open("books.txt", "r", encoding="utf-8")
book = []
autor = []
for line in f1:             # читать файл по линиям через цикл
    star = line.find("*")   # ищем разделить между автором и книгой
    b = line[:star]         # срез линии от 0 до *
    a = line[star+1:-1]     # срез линии от * до предпоследнего символа(в конце строки есть еще \n)
    autor.append(a)         # добавить в массив авторов
    book.append(b)          # добавить в книжек


f1.close()
print(book)
print(autor)
