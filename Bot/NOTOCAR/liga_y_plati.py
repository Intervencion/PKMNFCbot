from config import *

@bot.message_handler(commands=['plati'])
def command_plati(m):
	bot.reply_to(m,'<a href="https://www.forocoches.com/foro/showthread.php?t=6838079">Plataforma Pokémon Forocoches</a>', parse_mode="HTML", disable_web_page_preview=True)
	try:
		c.execute("SELECT Contador FROM TContador WHERE Nombre ='plati'")
		for i in c:
			print(i[0])
			increment = i[0] +1
			c.execute("UPDATE TContador SET Contador = Contador + 1 WHERE Nombre = 'plati'")
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






@bot.message_handler(commands=['liga'])
def command_liga(m):
	bot.reply_to(m,'<a href="http://www.forocoches.com/foro/showthread.php?t=5293279">Liga Forocoches (Ed. Alola)</a>', parse_mode="HTML", disable_web_page_preview=True)
	try:
		c.execute("SELECT Contador FROM TContador WHERE Nombre ='liga'")
		for i in c:
			print(i[0])
			increment = i[0] +1
			c.execute("UPDATE TContador SET Contador = Contador + 1 WHERE Nombre = 'liga'")
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