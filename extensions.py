import requests
import json
from config import currencies


class Convertor:
    @staticmethod
    def get_price(message):
        data = message.text.split(' ')

        if len(data) != 3:
            raise CountValuesException('Неверное количество параметров')

        if not data[-1].isdigit():
            raise IncorrectInputException('Неверный ввод')

        first, second, amount = data
        first_c = currencies[first.lower()]
        second_c = currencies[second.lower()]

        if first_c == second_c:
            raise ConvertException('Попытка сконвериртировать одинаковые валюты')

        url = f'https://min-api.cryptocompare.com/data/price?fsym={first_c}&tsyms={second_c}'
        r = requests.get(url)
        rate = json.loads(r.content)[second_c]

        answer = float(amount) * rate
        text = f'За {amount} {first_c} ты получишь {round(answer, 1)} {second_c}'

        return text


# Неверное число параметров
class CountValuesException(Exception):
    pass


# Неверный ввод (иные ошибки)
class IncorrectInputException(Exception):
    pass


# Конвертация одинаковых валют
class ConvertException(Exception):
    pass

