"""     Настройка запуска парсера
DEMON_THREAD = 1 - запуск парсера потоком-демоном
DEMON_THREAD = 2 - запуск парсера отдельной программой

токен бота(token) и юзер агент для парсинга необходимо задать ('User-Agent')
"""
DEMON_THREAD = 1
token = '1391702566:AAEtnktxNK5Q-chPNK3CIZFlhvevtH8m5lQ'
HEADERS = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36 Edg/89.0.774.57'
    }
delay = 300   # Задержка в секундах
