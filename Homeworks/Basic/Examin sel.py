"""
3. программа заходит на ютуб
    находит смешные видео про котов, заходит на видео и ставит лайк
"""
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

options = webdriver.FirefoxOptions()
# options.add_argument("--headless")
driver = webdriver.Firefox(options=options)
driver.implicitly_wait(10)

try:
    driver.get("https://www.youtube.com/")
    print("заходим на сайт...")
    find_input = driver.find_element(By.NAME, "search_query")
    find_input.send_keys("смешные видео про котов")
    time.sleep(2)
    find_button = driver.find_element(By.ID, "search-icon-legacy")
    print("ищем видосы шерстяных")
    find_button.click()
    time.sleep(5)
    video = driver.find_element(By.XPATH, "//a[@class = 'yt-simple-endpoint style-scope ytd-video-renderer']")
    video.click()
    time.sleep(3)
    like = driver.find_element(By.XPATH, "/html/body/ytd-app/div[1]/ytd-page-manager/ytd-watch-flexy/div[5]/div["
                                         "1]/div/div[2]/ytd-watch-metadata/div/div[2]/div["
                                         "2]/div/div/ytd-menu-renderer/div["
                                         "1]/ytd-segmented-like-dislike-button-renderer/yt-smartimation/div/div["
                                         "1]/ytd-toggle-button-renderer/yt-button-shape/button/yt-touch-feedback"
                                         "-shape/div/div[2]")
    like.click()
    print("Лайк поставлен!")
    time.sleep(10)

except Exception as ex:
    print(ex)
finally:
    driver.close()
    driver.quit()
