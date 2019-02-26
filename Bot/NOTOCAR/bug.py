from config import *

@bot.message_handler(commands=['bug'])
def command_bug(m):
	cid = m.chat.id
	uid = m.from_user.id
	ufm = m.from_user.first_name
	ulm = m.from_user.first_name
	uname = m.from_user.username
	mct = m.chat.title
	try:
		texto = m.text.split(' ', 1)[1]
		mensaje = f"User: {ufm}\n"
		mensaje += f"Chat: {mct}\n"
		mensaje += f"Hora: {hora}\n"
		mensaje += f"UserID: [{uid}]"
		mensaje += f" ChatID: [{cid}]"
		mensaje += "\n"
		mensaje += f"Mensaje: {texto}\n"
		mensaje += "-------------------------------\n"

		f = open('bugs.txt', 'a')
		f.write(mensaje)
		f.close()
		print ("Mensaje guardado en bugs.txt")
		bot.reply_to(m,"Tu mensaje ha sido recibido.")	
		bot.send_message(admins[0], f"Hay un mensaje nuevo de @{uname} [{uid}] enviado desde <i>{mct}</i> [{cid}] en <code>bugs.txt</code>.", parse_mode = "HTML")
		bot.send_message(admins[1], f"Hay un mensaje nuevo de @{uname} [{uid}] enviado desde <i>{mct}</i> [{cid}] en <code>bugs.txt</code>.", parse_mode = "HTML")
		try:
			c.execute("SELECT Contador FROM TContador WHERE Nombre ='bug'")
			for i in c:
				print(i[0])
				increment = i[0] +1
				c.execute("UPDATE TContador SET Contador='" + str(increment) + "' WHERE Nombre = 'bug'")
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
		bot.send_message(cid, "El formato del comando es /bug *X* donde X es el mensaje que quieras enviar.", parse_mode = "Markdown")
