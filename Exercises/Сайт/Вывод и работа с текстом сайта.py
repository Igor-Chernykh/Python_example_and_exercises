# заходим на сайт
# находим там 3й div
# выводим на экран оттуда весь текст
# пишем сколько раз в тексте встречается "Сквидвард"


from selenium import webdriver
import time
from selenium.webdriver.common.by import By

driver = webdriver.Firefox()                # открывается браузер
driver.get("https://stately-starship-cbb6ff.netlify.app/")