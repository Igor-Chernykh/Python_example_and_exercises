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

options = webdriver.ChromeOptions()
options.add_argument("--headless")
driver = webdriver.Chrome(options=options)
driver.implicitly_wait(10)


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
    book_list = driver.find_elements(By.CLASS_NAME, "buy-avaliable")
    print("найдено книг:", len(book_list))
    n = 0
    while n < 3:
        for elem in book_list:
            book_add = driver.find_element(By.XPATH, "//a[@class='btn buy-link btn-primary']")
            if elem.is_displayed():
                time.sleep(1)
                book_add.click()
                n = n + 1
                print("Добавлено", n)
    
def shop_card_del():
    cart = driver.find_element(By.XPATH, "/html/body/div[1]/div[5]/div[3]/div[1]/div[1]/div[2]/div/ul/li[6]/a/span[2]")
    cart.click()
    print("Переход в корзину")
    cart_book_list = driver.find_elements(By.CLASS_NAME, "product-padding-cart")
    print("книг в корзине:", len(cart_book_list))
    del_cart = driver.find_element(By.XPATH, "/html/body/div[1]/div[5]/div[2]/div/div/div/div/div/div/div/div[3]/div/div/div/div/div[1]/div/div/a")
    del_cart.click()
    print("очищаем корзину")
    cart_book_list = driver.find_elements(By.CLASS_NAME, "product-padding-cart")
    print("книг в корзине:", len(cart_book_list))



try:
    start()
    search()
    shop_cart_add()
    shop_card_del()

except Exception as ex:
    print(ex)

finally:
    driver.close()
    driver.quit()
