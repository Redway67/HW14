import telebot
from telebot import apihelper

TOKEN = '1014617754:AAHQGgsUEMOZpHs3IZyrUddV4qt10z6HHJI'

proxies = {
    'http': 'http://167.86.96.4:3128',
    'https': 'http://167.86.96.4:3128',
}

TEXT_START = 'Привет! Это бот сообщающий температуру сейчас в выбранном Вами городе'
TEXT_HELP = '/t '

apihelper.proxy = proxies
bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, TEXT_START)


@bot.message_handler(commands=['help'])
def send_welcome(message):
    bot.reply_to(message, TEXT_HELP)


bot.polling()
