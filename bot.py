from bs4 import BeautifulSoup
import requests
import os
import threading
import telebot
from bs4 import BeautifulSoup
from basework import chekbase
from cryptoparser import parse, cycle_timer
import config


""" @Mthree3sel_bot 
телеграм бот для парсинга криптобиржи
"""

bot = telebot.TeleBot(config.token)


@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    """Обработка сообщения"""
    result = chekbase(message.text.lower())
    if result != []:
        bot.send_message(message.from_user.id, result)
    else:
        bot.send_message(message.from_user.id, 'Такой валюты не существует')


""" Обработка типа запуска """
if config.DEMON_THREAD == 1:
    timer = threading.Thread(target=cycle_timer, args=[config.delay])       # создание потока-демона для парсинга
    timer.start()
    bot.polling(none_stop=True, interval=0)
else:
    bot.polling(none_stop=True, interval=0)
    os.system('python cryptoparser.py')   # запуск парсера отдельно
