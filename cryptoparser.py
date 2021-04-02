import requests
import time
from bs4 import BeautifulSoup
from basework import createbase, updatebase, insertbase
import config

URL = 'https://bitinfocharts.com/ru/markets/'


"""Модуль с парсингом возможен, как отдельный запуск так и запуск вместе с bot.py"""


def parse():
    """Парсинг"""
    response = requests.get(URL, headers=config.HEADERS)
    soup = BeautifulSoup(response.content, "html.parser")
    items = soup.find_all('tr', class_='ptr')
    names = []
    short_names = []
    cost = []
    for i in items:
        tds = i.find_all('td', attrs={"data-val": True})
        counter = 0
        for td in tds:
            if counter == 0:
                short_names.append(td['data-val'])
                names.append(td.find('span').find('a').text)
            elif counter == 1:
                cost.append(td.find('a').text)
            counter += 1
    # Работа с базой данных
    try:
        updatebase(names, short_names, cost)
    except:
        createbase()
        insertbase(names, short_names, cost)


def cycle_timer(timer):
    """Повтор парсинга с заданной задержкой"""
    while True:
        parse()
        time.sleep(timer)


if __name__ == "__main__":
    cycle_timer(config.delay)
