# программа работает в фоновом режиме
# заходит на сайт IMDB
# в поиске ищет фильм, там есть *top cast
# нужно вывести на экран
# *название фильма
# *список актеров
# *рейтинг фильма

from selenium import webdriver
import time
from selenium.webdriver.common.by import By

options = webdriver.FirefoxOptions()
# options.add_argument("--headless")
driver = webdriver.Edge(options=options)

# film_name = input("Введите название фильма:\n")
film_name = "Top Gun"
try:
    driver.get("https://www.imdb.com/chart/top/")
    print("зашел на сайт")
    find_input = driver.find_element(By.ID, "suggestion-search")
    find_input.send_keys(film_name)
    time.sleep(2)
    search_button = driver.find_element(By.ID, "suggestion-search-button")
    search_button.click()
    print("Нашел фильм")

    film = driver.find_element(By.XPATH, "/html/body/div[2]/main/div[2]/div[3]/section/div/div[1]/section[2]/div[2]/ul/li[1]")
    film.click()
    top_cast = driver.find_element(By.ID, "title-cast-item")
    print(top_cast)
    top_cast.click()

    print("список фильмов", len(top_cast))








except Exception as ex:
    print(ex)

finally:
    time.sleep(15)
    driver.close()
    # driver.quit()
