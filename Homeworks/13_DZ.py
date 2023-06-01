# 1.
# посоветуй фильм -- бот заходит на сайт imdb , находит либо топ фильмов либо новинки,
# берет список фильмов и выдает случайный
# 2.
# новости -- бот заходит на новостной ресурс, находит новости за сегодня, список заголовков.
# И читает все заголовки

import os
import playsound
from gtts import gTTS
import speech_recognition as sp
import time
import random
from selenium import webdriver
from selenium.webdriver.common.by import By

options = webdriver.FirefoxOptions()
options.add_argument("--headless")


def listen():
    rec = sp.Recognizer()
    print("Скажите команду")
    with sp.Microphone() as source:
        audio = rec.listen(source)
    try:
        msg = rec.recognize_google(audio, language="ru")
        vibor(msg)
    except sp.RequestError:
        print("ошибка гугла")
    except sp.WaitTimeoutError:
        print("Прошло время ожидания")
    except sp.UnknownValueError:
        print("не могу распознать")


def vibor(msg):
    msg = msg.lower()
    if "привет" in msg:
        otvet("здравствуйте")
    elif "пока" in msg:
        otvet("до свидания")
        os.abort()
    elif "анекдот" in msg:
        otvet(find_anek())
    elif "погода" in msg:
        otvet(find_weather())
    elif "посоветуй фильм" in msg:
        otvet(find_film())
    elif "новости" in msg:
        otvet(find_news())
    else:
        otvet(msg)


def find_anek():
    driver = webdriver.Firefox(options=options)
    driver.implicitly_wait(10)
    driver.get("https://www.anekdot.ru")
    page = driver.find_element(By.XPATH, "/html/body/div[2]/div[4]/div[1]/div/div[31]/a[2]")
    page.click()
    time.sleep(2)
    spisok = driver.find_elements(By.CLASS_NAME, "text")
    anek = random.choice(spisok)
    a = anek.text
    return a
    driver.close()


def find_weather():
    driver = webdriver.Firefox(options=options)
    driver.implicitly_wait(10)
    driver.get("https://www.yandex.ru/pogoda/")
    weather = driver.find_element(By.CLASS_NAME, "fact__temp-wrap")
    a = weather.text
    return a
    driver.close()


def find_film():
    driver = webdriver.Firefox(options=options)
    driver.implicitly_wait(10)
    driver.get("https://www.imdb.com/chart/top")
    spisok = driver.find_elements(By.TAG_NAME, "tr")
    film = random.choice(spisok)
    a = (film.text).partition(".")[2]
    return a
    driver.close()


def find_news():
    driver = webdriver.Firefox(options=options)
    driver.implicitly_wait(10)
    driver.get("https://ria.ru/")
    news_list = driver.find_elements(By.CLASS_NAME, "cell-list__list")
    print("Найденно новостей:", len(news_list))
    news = []
    for i in news_list:
        n = i.text
        news.append(n)
        print(n)
    a = str(news)
    return a
    driver.close()


def otvet(msg):
    print(msg)
    voice = gTTS(msg, lang="ru")
    fname = "1.mp3"
    voice.save(fname)
    playsound.playsound(fname)
    os.remove(fname)
    pass


while True:
    listen()
