"""
1. создать класс kino()
при создании фильма нужно задать
*название *режиссер *страна
создать три фильма

2.в классе создать методы
выходит в кинотеатре
выходит на онлайн
переводится на какой-то язык

метод выводит на экран текст
 *название фильма
и что с ним происходит
продемонстрировать как методы работают
"""


class Kino:
    """Класс для предоставления данных о фильмах"""

    def __init__(self, name, director, country):
        self.name = name
        self.director = director
        self.country = country

    def cinema(self, kinoteatr_name):
        print(f"Фильм {self.name} показывают в кинотеатре {kinoteatr_name}")

    def online(self, online_kinoteatr_name):
        print("Фильм", self.name, "показывается в онлайн-кинотеатре", online_kinoteatr_name)

    def translate(self, language):
        print(f"Фильм {self.name} переводится на {language} язык")


film1 = Kino("Переводчик", "Гай Ричи", "Великобритания")
film2 = Kino("Брат 2", "Алексей Балабанов", "Россия")
film3 = Kino("Беглец", "Рик Роман Во", "США")

film1.cinema("Формула Кино")
film2.online("ivi")
film3.translate("русский")
