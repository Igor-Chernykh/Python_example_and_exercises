# программа работает в фоновом режиме # заходит на сайт IMDB
# в поиске ищет фильм, там есть *top cast # нужно вывести на экран
# *название фильма # *список актеров # *рейтинг фильма

import time
from selenium import webdriver
from selenium.webdriver.common.by import By

options = webdriver.FirefoxOptions()
options.add_argument("--headless")
driver = webdriver.Firefox(options=options)
driver.implicitly_wait(10)


def film_find(film_name):
    driver.get("https://www.imdb.com/chart/top/")

    # находим инпут и пишем запрос
    find_input = driver.find_element(By.ID, "suggestion-search")
    find_input.send_keys(film_name)
    # находим и жмем кнопку
    search_button = driver.find_element(By.ID, "suggestion-search-button")
    time.sleep(2)
    search_button.click()
    # находим первый результат поиска
    film = driver.find_element(By.XPATH, "/html/body/div[2]/main/div[2]/div[3]/section"
                                         "/div/div[1]/section[2]/div["
                                         "2]/ul/li[1]/div[2]/div/a")
    # получаем полное название фильма
    name = film.text
    # переходим на страницу фильма
    film.click()
    return name


def casts_find():
    # находим всех актеров и составляем список
    cast = driver.find_elements(By.CLASS_NAME, "sc-bfec09a1-1")
    casts_list = []
    for elem in cast:
        casts_list.append(elem.text)
    return casts_list


def rating_find():
    # находим значение рейтинга фильма
    rate_find = driver.find_element(By.XPATH, "/html/body/div[2]/main/div/section[1]/section/div["
                                              "3]/section/section/div[3]/div[2]/div[2]/div[1]/div/div["
                                              "1]/a/span/div/div[2]/div[1]/span[1]")
    rating = rate_find.text
    return rating


try:
    print("Название фильма:", (film_find(input("Введите название фильма:\n"))))
    print("Рейтинг фильма", rating_find())
    print("Список актеров:", (casts_find()))

except Exception as ex:
    print(ex)

finally:
    driver.close()
    driver.quit()
