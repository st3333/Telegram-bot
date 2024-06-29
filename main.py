from telebot import*
import config

bot = TeleBot(config.token)
@bot.message_handler(commands= ['start'])
def start(message):
    bot.send_message(message.chat.id, "привет я эхо бот!")

@bot.message_handler(content_types=['text'])
def echo_message(message):
    bot.send_message(message.chat.id, message.text)
bot.polling(non_stop=True)    