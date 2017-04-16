# coding=utf-8

import telebot
import urllib, json
import emoji

token = open(".token").read().replace("\n", "")
bot = telebot.TeleBot(token)

markup_cat = telebot.types.InlineKeyboardMarkup()

markup_initial = telebot.types.ReplyKeyboardMarkup()
markup_initial.add(telebot.types.KeyboardButton('/categorias'))

# bot.send_message(chat_id, "Choose one letter:", reply_markup=markup)


api_url = "http://tg-list.online/api/"
def get_json_data(api, endpoint):
    return json.loads(urllib.urlopen(api + endpoint + ".json").read())["content"]

categories = get_json_data(api_url, 'category')
for cat in categories:
    markup_cat.add(telebot.types.InlineKeyboardButton(cat["name"], callback_data=str(cat["id"])))

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
	bot.reply_to(message, "Seja bem vendo ao bot do @grupos_ti. Selecione uma opção: ", reply_markup=markup_initial)

@bot.message_handler(commands=['categorias'])
def send_welcome(message):
	bot.reply_to(message, "Categorias:", reply_markup=markup_cat)

@bot.message_handler(func=lambda message: True)
def echo_all(message):
	bot.reply_to(message, message.text)


@bot.callback_query_handler(func=lambda call: True)
def  test_callback(call):
    if call.data == "start":
        bot.edit_message_reply_markup(call.message.chat.id, call.message.message_id, reply_markup=markup_cat)
        return

    chats = get_json_data(api_url, 'chat/category/' + call.data)
    markup = telebot.types.InlineKeyboardMarkup()
    for chat in chats:
        markup.add(telebot.types.InlineKeyboardButton(chat["username"], url=chat["url"]))
    markup.add(telebot.types.InlineKeyboardButton(emoji.emojize(':leftwards_arrow_with_hook:', use_aliases=True) + " Voltar", callback_data="start"))
    bot.edit_message_reply_markup(call.message.chat.id, call.message.message_id, reply_markup=markup)

bot.polling()
