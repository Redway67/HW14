import telebot
from telebot import apihelper
from parcer import get_temperature

TOKEN = '1014617754:AAHQGgsUEMOZpHs3IZyrUddV4qt10z6HHJI'

apihelper.proxy = {'https': 'https://85.132.71.82:3128'}

bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, 'Привет! Это бот сообщающий текущую температуру в выбранном Вами городе. \n'
                          'А также (если есть) архивной температуры,  \n'
                          'т.е. минимальной и максимальной в этот день в течении последних ста лет \n\n'
                          'Для справки наберите /help .')


@bot.message_handler(commands=['help'])
def send_welcome(message):
    bot.reply_to(message, '/t  (Название города) \n'
                          'Название города для России и стран бывшего СССР можно писать кириллицей. \n'
                          'Остальные города мира в их правильном написании латиницей. \n '
                          'По умолчанию будет выбран город Москва')


@bot.message_handler(commands=['t'])
def temperature_info(message):
    city_name = ' '.join(message.text.split(' ')[1:])
    city_name = city_name.replace(' ', '')
    answer = get_temperature(city_name)
    bot.reply_to(message, answer)


if __name__ == '__main__':
    bot.polling()
