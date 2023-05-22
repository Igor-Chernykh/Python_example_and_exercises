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
options.add_argument("--headless")
driver = webdriver.Firefox(options=options)
driver.implicitly_wait(10)

driver.get("")

try:
    pass

except Exception as ex:
    print(ex)

finally:
    driver.close()
    driver.quit()
