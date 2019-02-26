from config import *

@bot.message_handler(commands=['info'])
def command_info(m):
	cid = m.chat.id
	try:
		dex = m.text.split(' ', 1)[1].replace(" ","_")
		bot.reply_to(m,f'https://www.wikidex.net/wiki/{dex}', disable_web_page_preview=True)
		try:
			c.execute("SELECT Contador FROM TContador WHERE Nombre ='info'")
			for i in c:
				print(i[0])
				increment = i[0] +1
				c.execute("UPDATE TContador SET Contador = Contador + 1 WHERE Nombre = 'info'")
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
	except:
		bot.send_message(cid, "El formato del comando es /info *X* donde X es el nombre del pokémon, movimiento u objeto.", parse_mode = "Markdown")