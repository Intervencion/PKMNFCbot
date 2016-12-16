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


grupos_admitidos = -20432512 #Aquí se tendrán que añadir a mano los ID de los grupos que usen el bot
admins = 9662836, 1896312

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
			def on_user_joins(message):
				cid = message.chat.id
				nun = message.new_chat_member.username
				bot.send_message(cid, "Bienvenido al grupo de *Pokémon* *@" + str(nun) + "*, vamos a proceder a hacerte la encuesta de entrada:\n 1.- ¿Nostalfag? \n 2.- ¿Charmander, Squirtle o Bulbasaur?\n 3.-¿Legalfag o Piratafag?\n 4.-¿Fola sí o Fola no?\n\nSi te interesa saber las funciones que tiene RotomDex, ábreme chat en PRIVADO y hazme /help", parse_mode = "Markdown")
			#bot.send_message(cid, "Bienvenido al grupo de *Pokémon* *@" + str("jaja") + "*, vamos a proceder a hacerte la encuesta de entrada:\n 1.- ¿Nostalfag? \n 2.- ¿Charmander, Squirtle o Bulbasaur?\n 3.-¿Legalfag o Piratafag?\n 4.-¿Fola sí o Fola no?", parse_mode = "Markdown")
			#if m.content_type == 'new_chat_member':
			if cid > 0:
				mensaje = str(m.chat.first_name) + " [" + str(cid) + "]: " + m.text
			else:
				mensaje = str(m.from_user.first_name) + "[" + str(cid) + "]: " + m.text 
			f = open('log.txt', 'a')
			f.write(mensaje + "\n")
			f.close()
			patata = open('id.txt', 'a')
			patata.write("@" + str(uname) + "[" + str(uid) + "]" + "\n")
			patata.close()
			print (str(cid), str(uid), mensaje)
			
			
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
@bot.message_handler(commands=['evs'])
def command_evs(m):
	cid = m.chat.id
	bot.reply_to(m,'*HP*\n*–* `Caterpie` : Ruta 1. 1 EV de HP\n*–* `Makuhita` : Ruta 2. 1 EV de HP\n\n*Ataque*\n*–* `Pikipek` : Ruta 1. 1 EV de Ataque\n*–* `Yangoos` : Ruta 1, Ruta 2 (Por el día). 1 EV de Ataque\n*–* `Mankey` : Ruta 3. 1 EV de Ataque\n\n*Defensa*\n*–* `Roggenrola` : Colina Dequilate. 1 EV de Defensa\n*–* `Cubone` : Área Volcánica Wela. 1 EV de Defensa\n*–* `Geodude` : Ruta 12. 1 EV de Defensa\n*–* `Torkoal` : Ruta 12. 2 EVs de Defensa\n\n*Ataque Especial*\n*–* `Magnemite` : Escuela de Entrenadores (Ruta 1). 1 EV de Ataque Especial\n*–* `Oricorio` : Jardines de Melemele. 2 EVs de Ataque Especial\n\n*Defensa Especial*\n*–* `Tentacool` : Mar de Melemele (Surf). 1 EV de Defensa Especial\n*–* `Drowzee` : Ruta 2. 1 EV de Defensa Especial\n\n*Velocidad*\n*–* `Wingull` : Ruta 1, Afueras de Akala. 1 EV de Velocidad\n*–* `Rattata de Alola` : Ruta 1, Ruta 2 (Por la noche). 1 EV de Velocidad\n*–* `Meowth de Alola` : Escuela de Entrenadores (Ruta 1), Ruta 2. 1 EV de Velocidad\n*–* `Spearow` : Ruta 2, Ruta 3. 1 EV de Velocidad', parse_mode="markdown", disable_web_page_preview=True)

@bot.message_handler(commands=['natus'])
def command_natu(m):
	cid = m.chat.id
	bot.reply_to(m,"*Naturalezas*[ ](http://i.imgur.com/IRFr5SG.jpg)", parse_mode="Markdown")
