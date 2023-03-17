import telebot
from config import TOKEN, currencies
import extensions

bot = telebot.TeleBot(TOKEN)


# Запуск при старте
@bot.message_handler(commands=['start'])
def get_start(message):
    text = 'Приветствую! Этот бот - конвертер валют.'
    bot.send_message(message.chat.id, text)
    get_help(message)


# Помощь, дополнительно вызывается при старте
@bot.message_handler(commands=['help'])
def get_help(message):
    text = 'Для того, чтобы конвертировать валюту введи команду в следующем формате:' \
           '\n<имя валюты> <в какую валюту перевести> <количество>\n' \
           '\nНапример: доллар евро 5\n' \
           '\n/values - список валют' \
           '\n/help - помощь'
    bot.send_message(message.chat.id, text)


# Обработчик-помощник для того, чтобы посмотреть доступные валюты
@bot.message_handler(commands=['values'])
def values_help(message):
    text = 'Доступные валюты:'
    for key in currencies.keys():
        text = '\n* '.join((text, key, ))
    bot.send_message(message.chat.id, text)


# Основной обработчик для конвертации. Вызывает статический метод из класса Convertor.
# Ловит исключения
@bot.message_handler(content_types=['text'])
def convert(message):
    try:
        txt = extensions.Convertor().get_price(message)
    except extensions.CountValuesException as e:
        bot.reply_to(message, f'Ошибка пользователя\n{e}')
    except extensions.ConvertException as e:
        bot.reply_to(message, f'Ошибка пользователя\n{e}')
    except extensions.IncorrectValueNameException as e:
        bot.reply_to(message, f'Ошибка пользователя\n{e}')
    except extensions.IncorrectAmountException as e:
        bot.reply_to(message, f'Ошибка пользователя\n{e}')
    except Exception as e:
        bot.reply_to(message, f'Не удалось обработать команду\n{e}')
    else:
        bot.send_message(message.chat.id, txt)


bot.polling(none_stop=True)
