import telebot
from decouple import config
from telebot import types

bot = telebot.TeleBot(config("TOKEN_BOT"))


@bot.message_handler(commands=["start", "hello"])
def get_start_message(message):
    full_name = f"{message.from_user.first_name}"
    text = f"Здравствуйте"
    # bot.send_message(message.chat.id, text)
    bot.reply_to(message, text)


@bot.message_handler(content_types=["text"])
def get_message(message):
    mark_up = types.InlineKeyboardMarkup(row_width=2)
    if message.text.lower() == "услуги":
        text = "Выберите пожайлуста:"
        btn_1 = types.InlineKeyboardButton("Чистка зубов", callback_data="tooth_brushing")
        btn_2 = types.InlineKeyboardButton("Вживление имплантов", callback_data="implant")
        mark_up.add(btn_1, btn_2)
        bot.reply_to(message, text, reply_markup=mark_up)


@bot.callback_query_handler(func=lambda call: True)
def get_callback_data(call):
    print(call)
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    if call.data == "implant":
        reply_text = "Выберите какие импланты вы хотите себе вживить?: "
        btn1 = types.KeyboardButton("black")
        btn2 = types.KeyboardButton("blue")
        btn3 = types.KeyboardButton("green")
        markup.add(btn1, btn2, btn3)
        bot.send_message(call.message.chat.id, reply_text, reply_markup=markup)
    elif call.data == "tooth_brushing":
        reply_text = "Какую чистку зубов вы хотите?: "
        btn1 = types.KeyboardButton("button_1")
        btn2 = types.KeyboardButton("button_2")
        btn3 = types.KeyboardButton("button_3")
        markup.add(btn1, btn2, btn3)
        bot.send_message(call.message.chat.id, reply_text, reply_markup=markup)





























bot.polling()