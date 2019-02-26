from config import *

@bot.message_handler(commands=['start'])
def command_start(m):
	cid = m.chat.id
	uid = m.from_user.id
	username = m.chat.username
	if m.text.find(" ") != -1:
		comando = m.text.split(' ', 1)[1] #// Deeplinking
	else:
		if not str(cid) in usuarios:
			usuarios.append(str(cid))
#			aux = open( '/home/axel/bots/users.txt', 'a') # Y lo insertamos en el fichero 'users.txt'
			aux = open( 'users.txt', 'a')
			aux.write( f'id: {uid} user: {username} \n')
			aux.close()
			bot.send_message( cid, "Bienvenido al bot \n Si encuentras algún bug o dato erróneo, no dudes en hacérnoslo saber con /bug y la descripción del mismo.")
		else:
			bot.send_message( cid, "Bienvenido al bot \n Si encuentras algún bug o dato erróneo, no dudes en hacérnoslo saber con /bug y la descripción del mismo.")
	try:
		c.execute("SELECT Contador FROM TContador WHERE Nombre ='start'")
		for i in c:
			print(i[0])
			increment = i[0] +1
			c.execute("UPDATE TContador SET Contador = Contador + 1 WHERE Nombre = 'start'")
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