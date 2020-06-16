import requests


from flask import Flask
from time import time


# Указываем Flask что используется имя текущего файла
app = Flask(__name__)

# Через декораторы работает маршрутизация во Flask( аналог Django urls
@app.route('/')
def index():
    try:
        connection = requests.head(url='http://google.ru')
        return 'Привет, это начало Litrix!'
    except (requests.RequestException, ValueError):
        print('Сетевая ошибка')
        return False



if __name__ == '__main__':
# Запуск приложения без доп. опций
    app.run()
