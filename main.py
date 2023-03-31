import time

import requests

# Задаем начальную цену и процентное изменение
start_price = None
percent_change = 0.01


# Функция для получения текущей цены
def get_price():
    response = requests.get('https://fapi.binance.com/fapi/v1/ticker/24hr', params={'symbol': 'ETHUSDT'})
    data = response.json()
    return float(data['lastPrice'])


# Функция для определения собственных движений цены ETH
def detect_movement(price):
    global start_price
    if start_price is None:
        start_price = price
    else:
        change = abs(price - start_price) / start_price
        if change >= percent_change:
            print(f'Price movement: {change * 100:.2f}% in the last 60 minutes')


# Бесконечный цикл для постоянного считывания цены и определения движения
while True:
    price = get_price()
    detect_movement(price)

    time.sleep(2)  # Задержка 60 секунд
