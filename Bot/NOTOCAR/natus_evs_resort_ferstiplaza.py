from config import *

@bot.message_handler(commands=['festiplaza'])
def command_fiestiplaza(m):
	bot.reply_to(m,'<a href="https://docs.google.com/document/d/1tBMEb8xfogGqUqbxHuWC6LupSe7-3bKbCpGVF8nSVRA/edit">Toda la información sobre la Festiplaza.</a>', parse_mode="HTML", disable_web_page_preview=True)
	try:
		c.execute("SELECT Contador FROM TContador WHERE Nombre ='festiplaza'")
		for i in c:
			print(i[0])
			increment = i[0] +1
			c.execute("UPDATE TContador SET Contador='" + str(increment) + "' WHERE Nombre = 'festiplaza'")
	except:
		mensaje = f"No he contado bien mamá.\n"
		mensaje += f"User: {ufm}\n"
		mensaje += f"Chat: {mct}\n"
		mensaje += f"Hora: {hora}\n"
		mensaje += f"UserID: [{uid}]"
		mensaje += f" ChatID: [{cid}]"
		mensaje += "\n"
		mensaje += f"Mensaje: {texto}\n"
		mensaje += "-------------------------------\n"
		bot.send_message(admins[0], mensaje, parse_mode = "Markdown")
	





@bot.message_handler(commands=['resort'])
def command_resort(m):
	bot.reply_to(m,'<a href="https://docs.google.com/document/d/1ANGMKXv9zQBh1iYYGxthpp5kGueDpbBYCseR-bsJc60/edit">Toda la información sobre el Resort.</a>', parse_mode="HTML", disable_web_page_preview=True)
	try:
		c.execute("SELECT Contador FROM TContador WHERE Nombre ='resort'")
		for i in c:
			print(i[0])
			increment = i[0] +1
			c.execute("UPDATE TContador SET Contador='" + str(increment) + "' WHERE Nombre = 'resort'")
	except:
		mensaje = f"No he contado bien mamá.\n"
		mensaje += f"User: {ufm}\n"
		mensaje += f"Chat: {mct}\n"
		mensaje += f"Hora: {hora}\n"
		mensaje += f"UserID: [{uid}]"
		mensaje += f" ChatID: [{cid}]"
		mensaje += "\n"
		mensaje += f"Mensaje: {texto}\n"
		mensaje += "-------------------------------\n"
		bot.send_message(admins[0], mensaje, parse_mode = "Markdown")
	
	
	
	


@bot.message_handler(commands=['evs'])
def command_evs(m):
	bot.reply_to(m,"""*HP*\n*–* `Caterpie` : Ruta 1. 1 EV de HP\n*–* `Makuhita` : Ruta 2. 1 EV de HP
	\n\n*Ataque*\n*–* `Pikipek` : Ruta 1. 1 EV de Ataque\n*–* `Yangoos` : Ruta 1, Ruta 2 (Por el día). 1 EV de Ataque
	\n*–* `Mankey` : Ruta 3. 1 EV de Ataque\n\n*Defensa*\n*–* `Roggenrola` : Colina Dequilate. 1 EV de Defensa
	\n*–* `Cubone` : Área Volcánica Wela. 1 EV de Defensa\n*–* `Geodude` : Ruta 12. 1 EV de Defensa
	\n*–* `Torkoal` : Ruta 12. 2 EVs de Defensa\n\n*Ataque Especial*\n*–* `Magnemite` : Escuela de Entrenadores (Ruta 1). 
	1 EV de Ataque Especial\n*–* `Oricorio` : Jardines de Melemele. 2 EVs de Ataque Especial\n\n*Defensa Especial*
	\n*–* `Tentacool` : Mar de Melemele (Surf). 1 EV de Defensa Especial\n*–* `Drowzee` : Ruta 2. 1 EV de Defensa Especial
	\n\n*Velocidad*\n*–* `Wingull` : Ruta 1, Afueras de Akala. 1 EV de Velocidad\n*–* `Rattata de Alola` : Ruta 1, Ruta 2 (Por la noche). 
	1 EV de Velocidad\n*–* `Meowth de Alola` : Escuela de Entrenadores (Ruta 1), Ruta 2. 1 EV de Velocidad\n*–* `Spearow` : Ruta 2, Ruta 3. 
	1 EV de Velocidad""", parse_mode="markdown", disable_web_page_preview=True)
	try:
		c.execute("SELECT Contador FROM TContador WHERE Nombre ='evs'")
		for i in c:
			print(i[0])
			increment = i[0] +1
			c.execute("UPDATE TContador SET Contador='" + str(increment) + "' WHERE Nombre = 'evs'")
	except:
		mensaje = f"No he contado bien mamá.\n"
		mensaje += f"User: {ufm}\n"
		mensaje += f"Chat: {mct}\n"
		mensaje += f"Hora: {hora}\n"
		mensaje += f"UserID: [{uid}]"
		mensaje += f" ChatID: [{cid}]"
		mensaje += "\n"
		mensaje += f"Mensaje: {texto}\n"
		mensaje += "-------------------------------\n"
		bot.send_message(admins[0], mensaje, parse_mode = "Markdown")






@bot.message_handler(commands=['natus'])
def command_natu(m):
	bot.reply_to(m,"*Naturalezas*[⁣](http://i.imgur.com/IRFr5SG.jpg)", parse_mode="Markdown")
	try:
		c.execute("SELECT Contador FROM TContador WHERE Nombre ='natus'")
		for i in c:
			print(i[0])
			increment = i[0] +1
			c.execute("UPDATE TContador SET Contador='" + str(increment) + "' WHERE Nombre = 'natus'")
	except:
		mensaje = f"No he contado bien mamá.\n"
		mensaje += f"User: {ufm}\n"
		mensaje += f"Chat: {mct}\n"
		mensaje += f"Hora: {hora}\n"
		mensaje += f"UserID: [{uid}]"
		mensaje += f" ChatID: [{cid}]"
		mensaje += "\n"
		mensaje += f"Mensaje: {texto}\n"
		mensaje += "-------------------------------\n"
		bot.send_message(admins[0], mensaje, parse_mode = "Markdown")