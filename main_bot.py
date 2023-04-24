import telebot
api_token = '5967772925:AAGsn7o7XiPNr4lzjU3ErAxSlrqS5zaFN7Q'

bot = telebot.TeleBot(api_token)


@bot.message_handler(content_types=['text'])
def echo(message):
    bot.send_message(message.chat.id, text=f"{message.text}")


bot.polling(none_stop=True)
