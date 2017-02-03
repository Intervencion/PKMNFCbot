# -*- coding: utf-8 -*-

import sys
import re
import telebot
from telebot import types


TOKEN = '' 

bot = telebot.TeleBot(TOKEN) 

def listener(messages):
    for m in messages:
        cid = m.chat.id
        uid = m.from_user.id
        uname = m.from_user.username
        if m.text:
            if(m.text.startswith("!") or m.text.startswith("/")):
                mensaje = "User: " + str(m.from_user.first_name) + "\n"
                if cid < 0:
                    mensaje += "Chat: " + str(m.chat.title) + "\n"
                    mensaje += "UserID: [" + str(uid) + "]"
                if cid < 0:
                    mensaje += " ChatID: [" + str(cid) + "]"
                    mensaje += "\n"
                    mensaje += "Mensaje: " + m.text + "\n"
                    mensaje += "-------------------------------\n"
                else:
                    mensaje += "UserID: [" + str(uid) + "]\n"
                    mensaje += "Mensaje: " + m.text + "\n"
                    mensaje += "-------------------------------\n"
                f = open('mantenimiento.txt', 'a')
                f.write(mensaje)
                f.close()
                print (mensaje)
                bot.send_message(cid, "Bot under maintenance.")


bot.set_update_listener(listener)


bot.skip_pending = True		
bot.polling(none_stop=True)