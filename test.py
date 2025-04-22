import telebot

bot = telebot.TeleBot() # <--- TOKEN

#from CrocoBot3.message_handlers.start import start

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, 'moin')
    print('sent')

@bot.message_handler(content_types=['text'])
def other(message):
    bot.send_message(message.chat.id, 'moin')
    print('sent')


bot.polling()