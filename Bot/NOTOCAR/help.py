from config import *

@bot.message_handler(commands=['help'])
def command_help(m):
	cid = m.chat.id
	ayuda = "Los comandos de este bot son los siguientes:\n"
	ayuda += "/addfc XXXX-XXXX-XXXX ---- Añadir tu Friend Code a la lista.\n"
	ayuda += "/editfc XXXX-XXXX-XXXX  ---- Editar tu Friend Code y tu alias guardados.\n"
	ayuda += "/fc ---- Te permite ver la lista de Friend Code del grupo.\n"
	ayuda += "/mifc ---- Te permite ver tu *Friend Code*.\n"
	ayuda += "/stats P ---- Dónde P es un pokémon, devuelve los stats y sus habilidades.\n"
	ayuda += "/evs ---- Muestra una lista para farmear evs.\n"
	ayuda += "/natus ---- Muestra una imagen con los stats de las naturalezas, tanto en castellano como inglés.\n"
	ayuda += "/festiplaza ----- Devuelve el link con toda la info de la festiplaza.\n"
	ayuda += "/plati ----- Devuelve el link de la plataforma pokémon de forocoches.\n"
	ayuda += "/liga ----- Devuelve el link de la liga pokémon de forocoches.\n"
	ayuda += "/info X ---- Devuelve el link de wikidex con lo introducido.\n"
	ayuda += "/bug --- Reporta un bug a los desarrolladores.\n"
	ayuda += "/contact --- Manda un mensaje a los desarrolladores.\n"
	ayuda += ""
	bot.send_message(cid, ayuda)
	try:
		c.execute("SELECT Contador FROM TContador WHERE Nombre ='help'")
		for i in c:
			print(i[0])
			increment = i[0] +1
			c.execute("UPDATE TContador SET Contador='" + str(increment) + "' WHERE Nombre = 'help'")
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
