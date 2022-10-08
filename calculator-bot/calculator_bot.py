from config import token
import telebot
from telebot import types
from datetime import datetime

bot = telebot.TeleBot(token)
val = ''
last_val = ''

keyboard = telebot.types.InlineKeyboardMarkup()
keyboard.row(telebot.types.InlineKeyboardButton('🆑', callback_data='cl'),
             telebot.types.InlineKeyboardButton('🇯', callback_data='j'),
             telebot.types.InlineKeyboardButton('🔙', callback_data='<='),
             telebot.types.InlineKeyboardButton('➗', callback_data='/'))
keyboard.row(telebot.types.InlineKeyboardButton('7', callback_data='7'),
             telebot.types.InlineKeyboardButton('8', callback_data='8'),
             telebot.types.InlineKeyboardButton('9', callback_data='9'),
             telebot.types.InlineKeyboardButton('✖', callback_data='*'))
keyboard.row(telebot.types.InlineKeyboardButton('4', callback_data='4'),
             telebot.types.InlineKeyboardButton('5', callback_data='5'),
             telebot.types.InlineKeyboardButton('6', callback_data='6'),
             telebot.types.InlineKeyboardButton('➖', callback_data='-'))
keyboard.row(telebot.types.InlineKeyboardButton('1', callback_data='1'),
             telebot.types.InlineKeyboardButton('2', callback_data='2'),
             telebot.types.InlineKeyboardButton('3', callback_data='3'),
             telebot.types.InlineKeyboardButton('➕', callback_data='+'))
keyboard.row(telebot.types.InlineKeyboardButton('0', callback_data='0'),
             telebot.types.InlineKeyboardButton('🟰', callback_data='='))
keyboard.row(telebot.types.InlineKeyboardButton('.', callback_data='.'),
             telebot.types.InlineKeyboardButton('(', callback_data='('),
             telebot.types.InlineKeyboardButton(')', callback_data=')'),
             telebot.types.InlineKeyboardButton('+/-', callback_data='+/-'))


@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    bot.send_message(message.chat.id,
                     text='Привет, {0.first_name}❗\n'
                          'Я стану твоим проводником 🤖 ️в мир 🌈🪬🦄 операций\n'
                          'над рациональными и комплексными числами.\n'
                          'Тебе доступны следующие команды:\n'
                          '🤖 Запуск бота 👉 /start\n'
                          '🧮 Запуск калькулятора 👉 /calculator\n'
                          '📚 А что это за числа такие? 👉 /info'
                     .format(message.from_user, reply_markup=markup))


@bot.message_handler(commands=['info'])
def print_info(message):
    bot.send_message(message.chat.id,
                     text='Рациональное число - это число, которое можно представить как дробь. '
                          'Например, 0.5 - рациональное число т. к. его можно представить как 1/2.\n'
                          '\nКомплексное число - это двумерное число, которое имеет вид (a + bj), где '
                          'а и b - действительные числа, j - так называемая мнимая единица. '
                          'Например, 1.5 + 4.7j (j пишится слитно). Важно помнить, что это '
                          'ЕДИНОЕ  ЧИСЛО, а не сложение.\n')


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
            val = 'Ошибка!'
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
    if val == 'Ошибка!':
        val = ''

    time = datetime.now().strftime('%d.%m.%y - %H:%M:%S')
    with open('log.txt', 'a') as file:
        file.writelines(f'{time} : {data}\n')


bot.polling(none_stop=False, interval=0)
