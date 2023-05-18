import random
from selenium import webdriver      # импортируем веб-драйвер
import time

user_agents_list = [            # список юзер агентов
    "hello_world",
    "best_of_the best",
    "some_user_agent"
]

# options
options = webdriver.FirefoxOptions()    # создание объекта опций
# options.add_argument("user-agent=HelloWorld")  # добавление аргумента
options.add_argument(f"user-agent={random.choice(user_agents_list)}")   # рандомный выбор юзер-агента
driver = webdriver.Firefox(options=options)      # настройки браузера


# driver.get("")      # открывается сайт в инете
# ime.sleep(5)        # задержка времени
# driver.refresh()    # обновить страницу
# find_element("")    # найти один элемент
# find_elements("")   # найти все эл-ты и получить список
# .click()            # клик по элементу
# .send_keys()        # написать на сайте если возможно
# time.sleep()        # задержка по времени
# .text               # достать текст из элемента
# .get_attribute()    # достать атрибут элемента


try:
    driver.get(url="https://www.instagram.com")     # получить данные
    time.sleep(5)           # задержка времени
    driver.refresh()        # обновить страницу
    time.sleep(2)
    driver.get_screenshot_as_file("1.png")  # получить скриншот
    driver.save_screenshot("2.png")
    time.sleep(2)

except Exception as ex:     # обработать исключения
    print(ex)
finally:
    driver.close()      # закрыть драйвер
    driver.quit()
