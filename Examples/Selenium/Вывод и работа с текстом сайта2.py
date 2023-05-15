заходим на сайт
находим там 2й div
пишет самое длинное слово из этого текста

from selenium import webdriver
import time
from selenium.webdriver.common.by import By

driver = webdriver.Firefox()                # открывается браузер
driver.get("https://stately-starship-cbb6ff.netlify.app/")
