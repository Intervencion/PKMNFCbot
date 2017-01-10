# -*- coding: utf-8 -*-

import sys
import re
import telebot
from telebot import types
import time 
import json
import urllib
import random
import PIL
from PIL import Image

import sqlite3
con = sqlite3.connect('pkmnbot.db',check_same_thread = False)
c = con.cursor()

TOKEN = 'TOKEN' 
INSULTS = ["eres gilipollas", "cómeme los huevos", "abrazafarolas","bocachancla", "parguela","eres tan feo que ni tu madre estaba en el parto", "me voy a cagar en las cuatro farolas que alumbran la tumba de tu puta madre", "dile a tu madre que deje de cambiarse de pintalabios que me está dejando la polla como un arcoiris", "eres tan feo que cuando te miras al espejo te pegas en defensa propia", "tu madre es tan puta que se quitó un ojo para tener un agujero más.", "eres tan gordo que tu grupo sanguíneo es A-peritivo", "eres homoretrasado","sabes menos de pokémon que Fola", "eres más inútil que Hydreigon firme", "eres tan tonto que te han cogido de tronista"]


usuarios = [line.rstrip('\n') for line in open('users.txt')] 

bot = telebot.TeleBot(TOKEN) 


grupos_admitidos = -1001087339246, -1001031662216, -1001059767714 #Aquí se tendrán que añadir a mano los ID de los grupos que usen el bot (grupo, liga, asd)
admins = 1896312, 9662836
jan = 1896312


def listener(messages):
	for m in messages:
		cid = m.chat.id
		uid = m.from_user.id
		uname = m.from_user.username
			
	#if m.content_type == 'text':
		if m.text:


##########################################################
#################### Encuesta Bienvenida #################
			@bot.message_handler(func=lambda m: True, content_types=['new_chat_member'])
			def on_user_joins(m):
				cid = m.chat.id
				cname = m.chat.title
			#	nun = "@{}".format(m.from_user.new_chat_member.username) if m.from_user.username else m.from_user.first_name
				if (m.new_chat_member.username is None):
					nun = m.new_chat_member.first_name
					if (m.new_chat_member.last_name is not None):
						nun += " "
						nun += m.new_chat_member.last_name
					else: 
						bienvenida = "Bienvenido al grupo"
						bienvenida += str(cname)
						bienvenida += " "
				else:
					nun = m.new_chat_member.username
					bienvenida = "Bienvenido al grupo "
					bienvenida += str(cname)
					bienvenida += " @"
				#	bienvenida += "<b>Pokémon</b> @"
				bot.send_message(cid, str(bienvenida) + str(nun) +
				", vamos a proceder a hacerte la encuesta de entrada:\n 1.- ¿Nostalfag? "
				"\n 2.- ¿Charmander, Squirtle o Bulbasaur?\n 3.-¿Legalfag o Piratafag?\n " 
				"4.-¿Fola sí o Fola no?\n<a href='https://raw.githubusercontent.com/Intervencion/PKMNFCbot/master/Audios/pokemon.mp3'> </a>)\nSi te interesa saber las funciones que tiene RotomDex, "
				"ábreme chat en PRIVADO y hazme /help", parse_mode = "HTML")
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
				
			if(m.text.startswith("!") or m.text.startswith("/")):
				f = open('log.txt', 'a')
				f.write(mensaje)
				f.close()
				patata = open('id.txt', 'a')
				patata.write("@" + str(uname) + "[" + str(uid) + "]" + "\n")
				patata.close()
				print (mensaje)
			
			
bot.set_update_listener(listener)




@bot.message_handler(commands=['tetas'])
def command_boobs(message):
    response = urllib.request.urlopen('http://api.oboobs.ru/noise/1')
    i = 0
    while i < 10:
        data = json.loads(response.read().decode(response.info().get_param('charset') or 'utf-8'))
        if len(data) < 1:
            i += 1
            response = urllib.request.urlopen('http://api.oboobs.ru/noise/1')
            continue
        else:
            bot.send_message(message.chat.id, 'http://media.oboobs.ru/' + data[0]['preview'])
            return
    bot.send_message(message.chat.id, '¿Qué es una teta?')
    
    
@bot.message_handler(commands=['culos'])
def command_butts(message):
    response = urllib.request.urlopen('http://api.obutts.ru/noise/1')
    i = 0
    while i < 10:
        data = json.loads(response.read().decode(response.info().get_param('charset') or 'utf-8'))
        if len(data) < 1:
            i += 1
            response = urllib.request.urlopen('http://api.obutts.ru/noise/1')
            continue
        else:
            bot.send_message(message.chat.id, 'http://media.obutts.ru/' + data[0]['preview'])
            return
    bot.send_message(message.chat.id, '¿Qué es un culo?')
	
	
##############################################################
######################### COMANDOS DE LINKS ##################

@bot.message_handler(commands=['plati'])
def command_plati(m):
	cid = m.chat.id
	bot.reply_to(m,'<a href="https://www.forocoches.com/foro/showthread.php?t=5292857">Plataforma Pokémon Forocoches</a>', parse_mode="HTML", disable_web_page_preview=True)


@bot.message_handler(commands=['liga'])
def command_liga(m):
	cid = m.chat.id
	bot.reply_to(m,'<a href="http://www.forocoches.com/foro/showthread.php?t=5293279">Liga Forocoches (Ed. Alola)</a>', parse_mode="HTML", disable_web_page_preview=True)	
	
	
@bot.message_handler(commands=['info'])
def command_info(m):
	cid = m.chat.id
	try:
		dex = m.text.split(' ', 1)[1].replace(" ","_")
		bot.reply_to(m,'http://es.pokemon.wikia.com/wiki/' + str(dex), disable_web_page_preview=True)	
	except:
		bot.send_message(cid, "El formato del comando es /info *X* donde X es el nombre del pokémon, movimiento u objeto.", parse_mode = "Markdown")
		

@bot.message_handler(commands=['festiplaza'])
def command_fiestiplaza(m):
	cid = m.chat.id
	bot.reply_to(m,'<a href="https://docs.google.com/document/d/1tBMEb8xfogGqUqbxHuWC6LupSe7-3bKbCpGVF8nSVRA/edit">Toda la información sobre la Festiplaza.</a>', parse_mode="HTML", disable_web_page_preview=True)
	
@bot.message_handler(commands=['resort'])
def command_resort(m):
	cid = m.chat.id
	bot.reply_to(m,'<a href="https://docs.google.com/document/d/1ANGMKXv9zQBh1iYYGxthpp5kGueDpbBYCseR-bsJc60/edit">Toda la información sobre el Resort.</a>', parse_mode="HTML", disable_web_page_preview=True)
	
	
	
################################################################
#######################             ############################
################################################################
####################### COMANDOS STANDAR #######################

@bot.message_handler(commands=['start'])
def command_start(m):
	cid = m.chat.id
	if m.text.find(" ") != -1:
		comando = m.text.split(' ', 1)[1]
	else:
		if not str(cid) in usuarios:
			usuarios.append(str(cid))
#			aux = open( '/home/axel/bots/users.txt', 'a') # Y lo insertamos en el fichero 'users.txt'
			aux = open( 'users.txt', 'a')
			aux.write( "id:"+  str(cid) + " user: " + str(m.chat.username) + "\n")
			aux.close()
			bot.send_message( cid, "Bienvenido al bot")
		else:
			bot.send_message( cid, "Bienvenido al bot")

	#if comando == 'evs':
	#	command_evs(m)
		
		
		
@bot.message_handler(commands=['help'])
def command_help(m):
	cid = m.chat.id
	bot.send_message(cid, "Los comandos de este bot son los siguientes:\n/addfc XXXX-XXXX-XXXX   ----  Añadir tu Friend Code a la lista. \n/editfc XXXX-XXXX-XXXX   ---- Editar tu Friend Code guardado.  \n/fc  ---- Te permite ver la lista de Friend Code del grupo. \n/mifc  ---- Te permite ver tu *Friend Code*. \n!stats P  ---- Dónde P es un pokémon, devuelve los stats y sus habilidades. \n/evs ---- Muestra una lista para farmear evs. \n/plati  -----  Devuelve el link de la plataforma pokémon de forocoches. \n/liga  -----  Devuelve el link de la liga pokémon de forocoches. \n/info X  ---- Devuelve el link de wikidex con lo introducido.")



#############################################

bot.skip_pending = True		
bot.polling(none_stop=True)