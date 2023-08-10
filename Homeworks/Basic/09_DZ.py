# зайти на сайт https://citaty.info/
# нажать *случайная цитата
# нужно показать на экране в print() саму цитату и автора


from selenium import webdriver
import time
from selenium.webdriver.common.by import By

options = webdriver.FirefoxOptions()
options.add_argument("--headless")
driver = webdriver.Firefox(options=options)

try:
    driver.get("https://citaty.info/")
    driver.implicitly_wait(5)
    page = driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/div/div[2]/div[2]/div/ul/li[4]/a")
    page.click()
    time.sleep(2)
    quote = driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/div/div/div/main/div/div/div/div/div[2]/article/div[1]/div[1]")
    print("Цитата:\n", quote.text)
    author = driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/div/div/div/main/div/div/div/div/div[2]/article/div[1]/div[2]/div/div/a")
    print("Автор:\n", author.text)
except Exception as ex:
    print(ex)

finally:
    driver.close()
    driver.quit()
