import telebot
from config import TOKEN, currencies
import extensions

bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=['start'])
def get_start(message):
    text = 'Приветствую! Этот бот - конвертер валют.'
    bot.send_message(message.chat.id, text)
    get_help(message)


@bot.message_handler(commands=['help'])
def get_help(message):
    text = 'Для того, чтобы конвертировать валюту введи команду в следующем формате:' \
           '\n<имя валюты> <в какую валюту перевести> <количество>\n' \
           '\nНапример: доллар евро 5\n' \
           '\n/values - список валют' \
           '\n/help - помощь'
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
        txt = extensions.Convertor().get_price(message)
    except extensions.CountValuesException as e:
        bot.reply_to(message, f'Ошибка пользователя\n{e}')
    except extensions.ConvertException as e:
        bot.reply_to(message, f'Ошибка пользователя\n{e}')
    except extensions.IncorrectInputException as e:
        bot.reply_to(message, f'Ошибка пользователя\n{e}')
    except Exception as e:
        bot.reply_to(message, f'Не удалось обработать команду\n{e}')
    else:
        bot.send_message(message.chat.id, txt)


bot.polling(none_stop=True)
