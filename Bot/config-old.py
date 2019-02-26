#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#################################################
#                   BOT TOKEN #
#################################################

import os
import telebot
from telebot import types
from colorclass import Color
import json
import time
import six
import sys
import traceback
import re
import socket
from collections import OrderedDict
import requests



admins = [1896312, 9662836]

#################################################
#          USEFUL FUNCTIONS AND DATAS           #
#################################################

#def send_udp(txt):
#    sock.sendto(MESSAGE.format(txt).encode(), (UDP_IP, UDP_PORT))


userStep = dict()


def is_recent(m):
    return (time.time() - m.date) < 5


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

