import keyboard
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Firefox()                # открывается браузер
driver.get("https://stately-starship-cbb6ff.netlify.app/")

e1 = driver.find_element(By.ID, "d1")
print(e1.text)                              # получем текст из контейнера
e2 = driver.find_elements(By.TAG_NAME, "img")
for e in e2:                                # получаем адреса всех картинок
    print(e.get_attribute("src"))

find_link = driver.find_element(By.TAG_NAME, "a")
# find_link.click()                          # кликает на первую ссылку

find_input = driver.find_element(By.TAG_NAME, "input")
find_input.send_keys("Привет робот!")       # пишет в инпут
find_button = driver.find_element(By.TAG_NAME, "button")
find_button.click()


keyboard.press("Enter")                     # жмет по кнопке Энтер

time.sleep(3)                               # ждет 3 секунды
driver.close()
