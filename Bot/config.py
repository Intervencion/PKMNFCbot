#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#################################################
#                   BOT TOKEN #
#################################################
# -*- coding: utf-8 -*-
#!/usr/bin/env python3.6
import sys
import re
import telebot
from telebot import types
import time 
import json
import urllib
import random
import os
import six
import re
import socket
import requests
from collections import OrderedDict
from colorclass import Color
from io import StringIO

print(Color(
    '{autored}[{/red}{autoyellow}+{/yellow}{autored}]{/red} {autocyan} Archivo principal importado.{/cyan}'))

import sqlite3
con = sqlite3.connect('pkmnbot.db',check_same_thread = False)
c = con.cursor()
pkmn = ""

TOKEN = '' 


usuarios = [line.rstrip('\n') for line in open('users.txt')] 

bot = telebot.TeleBot(TOKEN) 
hora = time.strftime("%Y-%m-%d %H:%M:%S")

def listener(messages):
	for m in messages:
		cid = m.chat.id
		uid = m.from_user.id
		ufm = m.from_user.first_name
		ulm = m.from_user.first_name
		uname = m.from_user.username
		mct = m.chat.title
		texto = m.text.split(' ', 1)[1]

###################### INICIO CONTADORES DE USO ################
count_addfc = 0
count_editfc = 0
count_fc = 0
count_mifc = 0
count_stats = 0
count_evs = 0
count_natus = 0
count_festiplaza = 0
count_plati = 0
count_liga = 0
count_info = 0
count_bug = 0
count_contact = 0



admins = [1896312,9662836]

#################################################
#          USEFUL FUNCTIONS AND DATAS           #
#################################################

#def send_udp(txt):
#    sock.sendto(MESSAGE.format(txt).encode(), (UDP_IP, UDP_PORT))


userStep = dict()


def is_recent(m):
    return (time.time() - m.date) < 5


def line(alt=False):
    if alt:
        return u'\n—————————————————————————\n'
    else:
        return u'\n`—————————————————————————`\n'


def send_exception(exception):
    exc_type, exc_obj, exc_tb = sys.exc_info()
    tb = traceback.extract_tb(exc_tb, 4)
    message = '\n`' + str(exc_type) + '`'
    message += '\n\n`' + str(exc_obj) + '`'
    for row in tb:
        message += line()
        for val in row:
            message += '`' + str(val) + '`\n'
    return message

