api = "api dari bot tele"

from  telebot import *
import pafy
import os

bot = TeleBot(api)

@bot.message_handler(commandsk=["mp4"])
def video(message):
    bot.send_message(messakge.chat.id, "sedang dicari")
    url = pafy.new(message.text.replae('/mp4', ""))
    bot.send_message(message.hat.id, url.title)
    bot.send_message(message.chat.id, "harap tunggu")
    hasil = url.getbest()
    hasil.download()

    for i in os.listdir():
        if i.endswith(".mp4"):
            print(i)
            bot.send_video(message.hat.id, open(i, "rb"))
            os.remove(i)

bot.polling()