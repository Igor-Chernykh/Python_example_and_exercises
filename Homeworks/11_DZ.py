# зайти на сайт-магазин книг(по своему выбору)
# и написать программу, которая делает тесты, как на уроке
# -зайти на сайт, убрать ненужное
# -поиск
# -в корзину
# -зайти в корзину
# -удалить из корзины

import time
from selenium import webdriver
from selenium.webdriver.common.by import By

options = webdriver.FirefoxOptions()
# options.add_argument("--headless")
driver = webdriver.Firefox(options=options)
driver.implicitly_wait(10)

driver.get("https://www.labirint.ru/")
def start():
    driver.get("https://www.labirint.ru/")
    print("Зашли на сайт")
    coockie_but = driver.find_element(By.CLASS_NAME, "cookie-policy__button")
    time.sleep(3)
    coockie_but.click()


def search():
    search_field = driver.find_element(By.ID, "search-field")
    search_field.send_keys("История в деталях")
    time.sleep(2)
    print("Поиск книжек")
    search_but = driver.find_element(By.CLASS_NAME, "b-header-b-search-e-btn")
    search_but.click()
    books = driver.find_elements(By.CLASS_NAME, "product")
    print("Найдено результатов:", len(books))

def shop_cart_add():
    print("тестируем добавление в корзину...")
    book_list = driver.find_elements(By.CLASS_NAME, "rows1")
    print("найдено книг:", len(book_list))
    for elem in book_list:
        print(elem.text)
    #     book_add = driver.find_element(By.CLASS_NAME,
        # book_add = driver.find_element(By.CLASS_NAME, "btn-primary") #btn buy-link btn-primary
        # time.sleep(1)
        # book_add.click()
        # print(elem.text)

    # cards = driver.find_elements(By.CLASS_NAME, "")
    # for i in range(5):
    #     add = card[i].find_element(By.CLASS_NAME, "")
    #     add.location_once_scrolled_into_view
    #     add.click()




try:
    start()
    # search()
    shop_cart_add()
    pass

except Exception as ex:
    print(ex)

finally:
    time.sleep(40)
    driver.close()
    driver.quit()
