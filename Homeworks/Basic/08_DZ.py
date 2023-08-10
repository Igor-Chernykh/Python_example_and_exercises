# программа делает следующее:
# заходит на сайт ютуба
# сделать запрос *смешные видео про котов*
# и кликает мышкой на поиск


from selenium import webdriver
import time
from selenium.webdriver.common.by import By

driver = webdriver.Firefox()               
driver.get("https://www.youtube.com/")

time.sleep(2)

find_input = driver.find_element(By.NAME, "search_query")
find_input.send_keys("смешные видео про котов")
time.sleep(2)
find_button = driver.find_element(By.ID, "search-icon-legacy")
find_button.click()

time.sleep(5)
driver.close()
