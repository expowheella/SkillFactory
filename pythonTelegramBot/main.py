import telebot
from config import exchanger, TOKEN
from utils import ConvertionException, CryptoConverter, UserDB

bot = telebot.TeleBot(TOKEN)

# создаем базу данных пользователей
db = UserDB()

# поддержка нескольких пользователей
vals = {1: ('EUR', 'USD')}

"""
# объявляем обработчик сообщений, в скобках указываем, на какие сообщения реагировать.
# в данном случае - на все
@bot.message_handler()
def echo_test(message: telebot.types.Message):
    bot.send_message(message.chat.id, 'hello')
"""

''' \n - знак переноса строки '''


# объявляем обработчик сообщений (message_handler), в скобках указываем, на какие команды реагировать.
@bot.message_handler(commands=['start', 'help'])
def help(message: telebot.types.Message):
    text = r'''/set - выберите валютную пару для конвертации и укажите количество'''

    bot.send_message(message.chat.id, text)  # бот отвечает пользователю сообщением text


"""
# объявляем обработчик сообщений, в скобках указываем, на какие команды реагировать.
@bot.message_handler(commands=['values'])
def values(message: telebot.types.Message):
    text = 'Доступные валюты:'
    for key in exchanger.keys():  # keys() возвращает ключи словаря
        text = '\n'.join((text, key,))
    bot.reply_to(message, text)
"""


# объявляем обработчик сообщений, в скобках указываем тип контента, на который реагировать.
# @bot.message_handler(content_types=['text', ])
# def convert(message: telebot.types.Message):
#     try:
#         # биткоин, доллар, 1
#         values = message.text.split(' ')  # вводим три слова через пробел
#         # values = list(map(str.lower, values))  # меняем регистр символов на прописные буквы
#
#         # exchanger[quote] - ключ, exchanger[base] - значение в словаре exchanger
#         quote, base, amount = values
#         total_base = CryptoConverter.convert(values)
#     except ConvertionException as e:
#         bot.reply_to(message, f'Ошибка пользователя. \n{e}')
#     # except Exception as e:
#     #     bot.reply_to(message, f'Не удалось обработать команду\n{e}')
#     else:
#         text = f'Цена {amount} {quote} в {base} - {total_base}'
#         bot.send_message(message.chat.id, text)


@bot.message_handler(commands=['set', ])
def set_message(message: telebot.types.Message):
    markup = telebot.types.InlineKeyboardMarkup()
    for vol, form in exchanger.items():
        button = telebot.types.InlineKeyboardButton(text=vol.capitalize() + ' в Доллар',
                                                    callback_data=f'val1 {form}')  # val1 EUR
        # callback_data - это то, что возращает бот при нажатии на кнопку

        markup.add(button)

    bot.send_message(message.chat.id, text='Выберите валюту, из которой конвертировать', reply_markup=markup)

    # markup = telebot.types.InlineKeyboardMarkup()
    # for vol, form in exchanger.items():
    #     button = telebot.types.InlineKeyboardButton(text=vol.capitalize(), callback_data=f'val2 {form}')
    #     markup.add(button)
    #
    # bot.send_message(message.chat.id, text='Выберите валюту, в которую конвертировать', reply_markup=markup)


#  данный блок возвращает нам команду после нажатия кнопки в телеграм -> callback_data=f'val1 {form}' -> val1 USD
@bot.callback_query_handler(func=lambda call: True)
def handle_query(call):
    print('call.data:' + call.data)
    t, st = call.data.split()  # t = val1, st = USD
    print(t)
    print(st)
    user_id = call.message.chat.id

    if t == "val1":
        db.change_from(user_id, st)

    if t == "val2":
        db.change_to(user_id, st)

    print(user_id)  # идентификатор диалогов

    pair = db.get_pair(user_id)
    bot.answer_callback_query(callback_query_id=call.id,
                              show_alert=True, text=f'Теперь конвертируем из {pair[0]} в {pair[1]}')


@bot.message_handler(content_types=['text', ])
def convert(message: telebot.types.Message):
    pair = db.get_pair(message.chat.id)
    values = [*pair, message.text.strip()]
    print(message.chat.id)
    print(values)
    try:
        total_base = CryptoConverter.convert(values)

    except ConvertionException as e:
        bot.reply_to(message, f'Ошибка пользователя. \n{e}')
    except Exception as e:
        bot.reply_to(message, f'Не удалось обработать команду\n{e}')
    else:
        text = f'Цена {values[2]} {values[0]} в {values[1]} -- {total_base}{vals[1][1]}'
        bot.send_message(message.chat.id, text)


# @bot.callback_query_handler(func=lambda call: True)
# def handle_query(call):
#     print(call.data)

# запускаем бот
bot.polling(none_stop=True, interval=0)
