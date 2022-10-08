import telebot
import datetime
from datetime import date
from datetime import time
from pytube import YouTube
bot = telebot.TeleBot('5157038758:AAELsqccS7dvrFyHoipSCnvJsjFeDOt_xco')

@bot.message_handler(commands=['start', 'хай'])
def start(message):
    bot.send_message(message.chat.id, 'Привет')

@bot.message_handler(commands=['yt'])
def after_text(message):
    link = bot.reply_to(message, 'Укажите ссылку на видео:')
    bot.register_next_step_handler(link, after_text_2)
def after_text_2(message):
    link=message.text
    yt = YouTube(link)
    yt.streams.filter(progressive=True)
    stream = yt.streams.get_by_itag(22)
    stream.download()
    file = open(f'{stream.default_filename}', 'rb')
    bot.send_video(message.from_user.id, file)

@bot.message_handler(commands=['date'])
def start(message):
    bot.send_message(message.chat.id, date.today())

@bot.message_handler(commands=['file'])
def start(message):
    file = open('dop.png', 'rb')
    bot.send_photo(message.chat.id, file , 'вот это фото')

@bot.message_handler(commands=['bye'])
def start(message):
    bot.send_message(message.chat.id, 'Пока')

bot.polling()

