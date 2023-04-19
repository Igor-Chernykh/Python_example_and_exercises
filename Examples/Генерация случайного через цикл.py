import random
import time

for i in range(5):  # i - счетчик который считает до значения в скобках
                    # можно указать переменную в которой содержится число
                    # цикл будет крутиться сколько указано в переменной
    num = random.randint(1, 100)
    print(num)
    time.sleep(1)
