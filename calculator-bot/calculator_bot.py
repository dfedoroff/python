from config import token
import telebot
from telebot import types
from datetime import datetime

bot = telebot.TeleBot(token)
val = ''
last_val = ''

keyboard = telebot.types.InlineKeyboardMarkup()
keyboard.row(telebot.types.InlineKeyboardButton('π', callback_data='cl'),
             telebot.types.InlineKeyboardButton('π―', callback_data='j'),
             telebot.types.InlineKeyboardButton('π', callback_data='<='),
             telebot.types.InlineKeyboardButton('β', callback_data='/'))
keyboard.row(telebot.types.InlineKeyboardButton('7', callback_data='7'),
             telebot.types.InlineKeyboardButton('8', callback_data='8'),
             telebot.types.InlineKeyboardButton('9', callback_data='9'),
             telebot.types.InlineKeyboardButton('β', callback_data='*'))
keyboard.row(telebot.types.InlineKeyboardButton('4', callback_data='4'),
             telebot.types.InlineKeyboardButton('5', callback_data='5'),
             telebot.types.InlineKeyboardButton('6', callback_data='6'),
             telebot.types.InlineKeyboardButton('β', callback_data='-'))
keyboard.row(telebot.types.InlineKeyboardButton('1', callback_data='1'),
             telebot.types.InlineKeyboardButton('2', callback_data='2'),
             telebot.types.InlineKeyboardButton('3', callback_data='3'),
             telebot.types.InlineKeyboardButton('β', callback_data='+'))
keyboard.row(telebot.types.InlineKeyboardButton('0', callback_data='0'),
             telebot.types.InlineKeyboardButton('π°', callback_data='='))
keyboard.row(telebot.types.InlineKeyboardButton('.', callback_data='.'),
             telebot.types.InlineKeyboardButton('(', callback_data='('),
             telebot.types.InlineKeyboardButton(')', callback_data=')'),
             telebot.types.InlineKeyboardButton('+/-', callback_data='+/-'))


@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    bot.send_message(message.chat.id,
                     text='ΠΡΠΈΠ²Π΅Ρ, {0.first_name}β\n'
                          'Π― ΡΡΠ°Π½Ρ ΡΠ²ΠΎΠΈΠΌ ΠΏΡΠΎΠ²ΠΎΠ΄Π½ΠΈΠΊΠΎΠΌ π€ οΈΠ² ΠΌΠΈΡ ππͺ¬π¦ ΠΎΠΏΠ΅ΡΠ°ΡΠΈΠΉ\n'
                          'Π½Π°Π΄ ΡΠ°ΡΠΈΠΎΠ½Π°Π»ΡΠ½ΡΠΌΠΈ ΠΈ ΠΊΠΎΠΌΠΏΠ»Π΅ΠΊΡΠ½ΡΠΌΠΈ ΡΠΈΡΠ»Π°ΠΌΠΈ.\n'
                          'Π’Π΅Π±Π΅ Π΄ΠΎΡΡΡΠΏΠ½Ρ ΡΠ»Π΅Π΄ΡΡΡΠΈΠ΅ ΠΊΠΎΠΌΠ°Π½Π΄Ρ:\n'
                          'π€ ΠΠ°ΠΏΡΡΠΊ Π±ΠΎΡΠ° π /start\n'
                          'π§? ΠΠ°ΠΏΡΡΠΊ ΠΊΠ°Π»ΡΠΊΡΠ»ΡΡΠΎΡΠ° π /calculator\n'
                          'π Π ΡΡΠΎ ΡΡΠΎ Π·Π° ΡΠΈΡΠ»Π° ΡΠ°ΠΊΠΈΠ΅? π /info'
                     .format(message.from_user, reply_markup=markup))


@bot.message_handler(commands=['info'])
def print_info(message):
    bot.send_message(message.chat.id,
                     text='Π Π°ΡΠΈΠΎΠ½Π°Π»ΡΠ½ΠΎΠ΅ ΡΠΈΡΠ»ΠΎ - ΡΡΠΎ ΡΠΈΡΠ»ΠΎ, ΠΊΠΎΡΠΎΡΠΎΠ΅ ΠΌΠΎΠΆΠ½ΠΎ ΠΏΡΠ΅Π΄ΡΡΠ°Π²ΠΈΡΡ ΠΊΠ°ΠΊ Π΄ΡΠΎΠ±Ρ. '
                          'ΠΠ°ΠΏΡΠΈΠΌΠ΅Ρ, 0.5 - ΡΠ°ΡΠΈΠΎΠ½Π°Π»ΡΠ½ΠΎΠ΅ ΡΠΈΡΠ»ΠΎ Ρ. ΠΊ. Π΅Π³ΠΎ ΠΌΠΎΠΆΠ½ΠΎ ΠΏΡΠ΅Π΄ΡΡΠ°Π²ΠΈΡΡ ΠΊΠ°ΠΊ 1/2.\n'
                          '\nΠΠΎΠΌΠΏΠ»Π΅ΠΊΡΠ½ΠΎΠ΅ ΡΠΈΡΠ»ΠΎ - ΡΡΠΎ Π΄Π²ΡΠΌΠ΅ΡΠ½ΠΎΠ΅ ΡΠΈΡΠ»ΠΎ, ΠΊΠΎΡΠΎΡΠΎΠ΅ ΠΈΠΌΠ΅Π΅Ρ Π²ΠΈΠ΄ (a + bj), Π³Π΄Π΅ '
                          'Π° ΠΈ b - Π΄Π΅ΠΉΡΡΠ²ΠΈΡΠ΅Π»ΡΠ½ΡΠ΅ ΡΠΈΡΠ»Π°, j - ΡΠ°ΠΊ Π½Π°Π·ΡΠ²Π°Π΅ΠΌΠ°Ρ ΠΌΠ½ΠΈΠΌΠ°Ρ Π΅Π΄ΠΈΠ½ΠΈΡΠ°. '
                          'ΠΠ°ΠΏΡΠΈΠΌΠ΅Ρ, 1.5 + 4.7j (j ΠΏΠΈΡΠΈΡΡΡ ΡΠ»ΠΈΡΠ½ΠΎ). ΠΠ°ΠΆΠ½ΠΎ ΠΏΠΎΠΌΠ½ΠΈΡΡ, ΡΡΠΎ ΡΡΠΎ '
                          'ΠΠΠΠΠΠ  Π§ΠΠ‘ΠΠ, Π° Π½Π΅ ΡΠ»ΠΎΠΆΠ΅Π½ΠΈΠ΅.\n')


@bot.message_handler(commands=['calculator'])
def get_message(message):
    global val
    if val == '':
        bot.send_message(message.from_user.id, '0',
                         reply_markup=keyboard)
    else:
        bot.send_message(message.from_user.id, val,
                         reply_markup=keyboard)


@bot.callback_query_handler(func=lambda call: True)
def callback_func(query):
    global val, last_val
    data = query.data
    if data == '+/-':
        if val[-5:] == '*(-1)':
            val = val[:len(val) - 5]
        else:
            val = val + '*(-1)'
    elif data == 'cl':
        val = ''
    elif data == '<=':
        if val != '':
            val = val[:len(val) - 1]
    elif data == '=':
        try:
            val = str(eval(val))
        except IndexError:
            val = 'ΠΡΠΈΠ±ΠΊΠ°!'
    else:
        val += data
    if (val != last_val and val != '') or ('0' != last_val and val == ''):
        if val == '':
            bot.edit_message_text(chat_id=query.message.chat.id,
                                  message_id=query.message.message_id, text='0', reply_markup=keyboard)
        else:
            bot.edit_message_text(chat_id=query.message.chat.id,
                                  message_id=query.message.message_id, text=val, reply_markup=keyboard)
    last_val = val
    if val == 'ΠΡΠΈΠ±ΠΊΠ°!':
        val = ''

    time = datetime.now().strftime('%d.%m.%y - %H:%M:%S')
    with open('log.txt', 'a') as file:
        file.writelines(f'{time} : {data}\n')


bot.polling(none_stop=False, interval=0)
