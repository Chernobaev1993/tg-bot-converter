import requests
import json
from config import currencies


class Convertor:
    @staticmethod
    def get_price(message):
        data = message.text.split(' ')  # Разбиваем сообщение от пользователя в список

        # Проверяем длину списка
        if len(data) != 3:
            raise CountValuesException('Неверное количество параметров')

        # Проверяем, что третье значение - число
        if not data[2].isdigit():
            raise IncorrectAmountException('Неверно введено количество валюты')

        first, second, amount = data

        # Проверяем корректность имени валют
        if first.lower() not in currencies.keys():
            raise IncorrectValueNameException(f'Неверное имя валюты {first}')
        elif second.lower() not in currencies.keys():
            raise IncorrectValueNameException(f'Неверное имя валюты {second}')

        first_c = currencies[first.lower()]
        second_c = currencies[second.lower()]

        # Проверка на попытку сконвертировать одинаковые валюты
        if first_c == second_c:
            raise ConvertException('Попытка сконвериртировать одинаковые валюты')

        # Получаем объект класса Response с помощью API
        url = f'https://min-api.cryptocompare.com/data/price?fsym={first_c}&tsyms={second_c}'
        r = requests.get(url)

        # Преобразуем ответ с помощью json в тип данных dict и сразу вытащим оттуда нужное нам значение
        rate = json.loads(r.content)[second_c]

        # Посчитаем и выведем ответ
        answer = float(amount) * rate
        text = f'За {amount} {first_c} ты получишь {round(answer, 1)} {second_c}'

        return text


# Неверное число параметров
class CountValuesException(Exception):
    pass


# Неверный ввод (иные ошибки)
class IncorrectAmountException(Exception):
    pass


# Конвертация одинаковых валют
class ConvertException(Exception):
    pass


class IncorrectValueNameException(Exception):
    pass
