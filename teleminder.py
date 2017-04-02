# -*- coding: utf-8 -*-
import os
import time
import threading
from random import randint

import telebot
from telebot import types
import schedule
import cat



TOKEN = 'TOKEN'
CHAT_ID = 123456
WHEN = '9:30'
IMAGES_PATH = os.path.dirname(os.path.abspath(__file__)) +'/images/'

tb = telebot.TeleBot(TOKEN)

def send_random_cat():
    cat.getCat(directory= IMAGES_PATH + 'last_random_cat', filename='cat', format='gif')
    photo = open(IMAGES_PATH + 'last_random_cat/cat.gif', 'rb')
    tb.send_document(CHAT_ID, photo)


def send_sad_cat():
    photo = open(IMAGES_PATH +'/sad_cat/sad_cat'+str(randint(1,11))+'.jpg', 'rb')
    tb.send_photo(CHAT_ID, photo)


def send_reminder(message):
    tb.reply_to(message, "Muy mal, te aviso en 30 min")
    threading.Timer(60*30, send_message).start()

def send_message():
    markup = types.ReplyKeyboardMarkup()
    markup.add('Sí, a la hora', 'Sí, tarde', 'Nop', 'Free Day' )
    tb.send_message(CHAT_ID, "¿Te has tomado la pastilla?", None, None, markup)

# Handle all other messages with content_type 'text' (content_types defaults to ['text'])
@tb.message_handler(func=lambda message: True)
def process_message(message):
    if message.text == u'Sí, a la hora':
        send_random_cat()
    elif message.text == u'Sí, tarde':
        send_sad_cat()
    elif message.text == u'Free Day':
        send_random_cat()
    elif message.text == u'Nop':
        send_reminder(message)


def main():
    tb.send_message(CHAT_ID, "¡Hola! Soy Teleminder.", None, None, None)
    schedule.every().day.at(WHEN).do(send_message)
    send_message()
    tb.polling()
    while True:
        schedule.run_pending()
        time.sleep(1)


if __name__ == "__main__":
    main()