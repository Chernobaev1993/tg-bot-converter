# Слишком много параметров
class TooManyValuesException(Exception):
    pass


# Слишком мало параметров
class NotEnoughValuesException(Exception):
    pass


# Нет такой валюты
class IncorrectValueNameException(Exception):
    pass


# Неверный ввод (иные ошибки)
class IncorrectInputException(Exception):
    pass


# Конвертация одинаковых валют
class ConvertException(Exception):
    pass
