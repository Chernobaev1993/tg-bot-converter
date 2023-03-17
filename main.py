import telebot
import requests
import json
import tgbotExc

TOKEN = "6279223852:AAGwSLJrPbJIEM2ScSafVKyNEDZ5TkNjljk"
bot = telebot.TeleBot(TOKEN)

currencies = {
    'доллар': 'USD',
    'евро': 'EUR',
    'рубль': 'RUB',
    'биткоин': 'BTC'
}


@bot.message_handler(commands=['start'])
def get_start(message):
    text = 'Приветствую! Этот бот - конвертер валют.'
    bot.send_message(message.chat.id, text)
    get_commands(message)


@bot.message_handler(commands=['commands'])
def get_commands(message):
    text = 'Список доступных команд:\n'\
           '\n* /help - помощь' \
           '\n* /values - список валют '
    bot.send_message(message.chat.id, text)


@bot.message_handler(commands=['help'])
def get_help(message):
    text = 'Для того, чтобы конвертировать валюту введи команду в следующем формате:' \
           '\n<имя валюты> <в какую валюту перевести> <количество>\n' \
           '\nНапример: доллар евро 5\n' \
           '\n/values - список валют'
    bot.send_message(message.chat.id, text)


@bot.message_handler(commands=['values'])  # Обработчик-помощник для того, чтобы посмотреть доступные валюты
def values_help(message):
    text = 'Доступные валюты:'
    for key in currencies.keys():
        text = '\n* '.join((text, key, ))
    bot.send_message(message.chat.id, text)


@bot.message_handler(content_types=['text'])  # Основной обработчик для конвертации
def convert(message):
    try:
        data = message.text.split(' ')
        if len(data) < 3 or not data[-1].isdigit():
            bot.reply_to(message, 'Неправильный ввод, попробуй еще раз')
            get_help(message)
        else:
            first, second, amount = data
            first_c = currencies[first.lower()]
            second_c = currencies[second.lower()]

            url = f'https://min-api.cryptocompare.com/data/price?fsym={first_c}&tsyms={second_c}'
            r = requests.get(url)
            rate = json.loads(r.content)[second_c]

            answer = float(amount) * rate
            text = f'За {amount} {first_c} ты получишь {round(answer, 1)} {second_c}'
            bot.send_message(message.chat.id, text)
    except Exception:
        bot.reply_to(message, 'Неправильный ввод, попробуй еще раз')
        get_help(message)


bot.polling(none_stop=True)
