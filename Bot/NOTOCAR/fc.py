from config import *


@bot.message_handler(commands=['eg'])
def command_eg(m):
	cid = m.chat.id
	print("Linea 6-8")
	EG = existeGrupo(cid)
	print("eg pre eg==1")
	if(EG == 1):
		bot.send_message(cid, "El grupo existe en la BD",
						 parse_mode="Markdown")
	else:
		bot.send_message(cid, "El grupo NO existe en la BD",
						 parse_mode="Markdown")

def existeGrupo(cid):
	print("Estamos antes del execute de def existeGrupo(cid):")
	#c.execute(f"SELECT COUNT(*) FROM GRUPO WHERE idGrupo ='{cid}'")
	c.execute('SELECT COUNT(*) FROM GRUPO WHERE idGrupo=?', (cid,))
	r = c.fetchone()
	if r:
		print("Vamos a ver si el select de grupo ha devuelto algún elemento")
		print(f'El resultado del select es: {r[0]}')
		EG =r[0]
	else: 
		print("Estamos aquí porque el select nos ha devuelto un elemento vacío")
		EG = 0

	#try:
	#	for i in c:
	#		print("Vamos a ver si el select de grupo ha devuelto algún elemento")
	#		print(f'El resultado del select es: {i[0]}')
	#		EG =i[0]
	#
	#except Exception as e:
	#	print("except Exception as e: L27")
	#	print(e)
	#	print("Estamos aquí porque el select nos ha devuelto un elemento vacío")
	#	EG = 0
	#
	return EG

def existeUser(uid):
	#c.execute(f"SELECT COUNT(*) FROM Usuarios WHERE idUsuario ='{uid}'")
	c.execute('SELECT COUNT(*) FROM Usuarios WHERE idUsuario=?', (uid,))
	try:
		for i in c:
			print("Vamos a ver si el select de Usuarios ha devuelto algún elemento")
			print(f"El resultado del select es: {i[0]}")
			EU =i[0]
	
	except Exception as e:
		print(e)
		print("Estamos aquí porque el select nos ha devuelto un elemento vacío")
		EU = 0
	
	return EU

def existeUserGru(uid,cid):
	#c.execute(f"SELECT COUNT(*) FROM UsuGrupo WHERE idUsuarioFK ='{uid}' AND idGrupoFK ='{cid}'")
	c.execute('SELECT COUNT(*) FROM UsuGrupo WHERE idUsuarioFK=? AND idGrupoFK=?', (uid, cid,))
	try:
		for i in c:
			print("Vamos a ver si el select de UsuGrupo ha devuelto algún elemento")
			print(f"El resultado del select es: {i[0]}")
			EUG =i[0]
	
	except Exception as e:
		print(e)
		print("Estamos aquí porque el select nos ha devuelto un elemento vacío")
		EUG = 0
	print(f"Vamos a devolver el valor de EUG que es {EUG}")
	return EUG

@bot.message_handler(commands=['fc'])
def command_fc(m):
	cid = m.chat.id 
	uname = m.from_user.username
	uid = m.from_user.id
	arrayl = []
	try:
	
		#c.execute(f"SELECT idUsuario,ALIAS,FC FROM Usuarios INNER JOIN UsuGrupo ON Usuarios.idUsuario = UsuGrupo.idUsuarioFK WHERE UsuGrupo.idGrupoFK ='{cid}' ORDER BY ALIAS ASC")
		c.execute('SELECT idUsuario,ALIAS,FC FROM Usuarios INNER JOIN UsuGrupo ON Usuarios.idUsuario = UsuGrupo.idUsuarioFK WHERE UsuGrupo.idGrupoFK=? ORDER BY ALIAS ASC', (cid,))
		print("hago el for?")
		for i in c:
			print("1")
			Alias_resultado = f'{i[1]}: '
			print("2)" + str(Alias_resultado))
			fc_resultado = i[2]
			print("3)" + str(fc_resultado))
			p = f'*{Alias_resultado}* `{fc_resultado}`'
			print("4" + str(p))
			arrayl.append(p)
			print("5")
		f = str(arrayl).replace(" '","").replace("'","")
		f = f.replace(",", "\n").replace("[","").replace("]","")
		if not f:
			f = "Tu fc no aparece en la lista. Añadete con /addfc."
			print(str(f))
			bot.send_message(cid, f'{f}', parse_mode = "Markdown")
			con.commit()
		elif (f == None):
			f = "Tu fc no aparece en la lista. Añadete con /addfc."
			bot.send_message(cid, f'{f}', parse_mode = "Markdown")
			con.commit()
		else:
			print(str(f))
			bot.send_message(cid, f'{f}', parse_mode = "Markdown")
			con.commit()
		try:
			#c.execute("SELECT Contador FROM TContador WHERE Nombre ='fc'")
			c.execute("SELECT Contador FROM TContador WHERE Nombre ='fc'")
			for i in c:
				print(i[0])
				increment = i[0] +1
				#c.execute("UPDATE TContador SET Contador='" + str(increment) + "' WHERE Nombre = 'fc'")
				c.execute("UPDATE TContador SET Contador = Contador + 1 WHERE Nombre = 'fc'")
		except Exception as e:
			print(e)
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
	except Exception as e:
		print(e)
		bot.send_message(cid, "No hemos podido mostrarte la lista")
		

@bot.message_handler(commands=['addfc'])
def command_addfc(m):
	cid = m.chat.id
	uid = m.from_user.id
	mct = m.chat.title
	ufm = m.from_user.first_name
	ulm = m.from_user.last_name
	if (m.from_user.username is None):
		if (ulm == None):
			uname = ufm
		else:
			uname = f'{ufm} {ulm}'
	else:
		uname = m.from_user.username
	if(cid>0):
		bot.send_message(cid,"Este comando es solo para grupos")
	elif(cid<0):
		print(str(cid))
		print("VAMOS A LEERLO SIN TRY")
		try:
			uname2 = f'@{uname}'
			fc = m.text.split(' ', 1)[1].replace(" ", "")
			#print("voy a capitalizar")
			#fc.capitalize()
			print(str(fc))
			#print("he capitalizado, voy a crear el patrón")
			print("Entro sin capitalizar. Voy a crear el patrón")
			pattern = '^\d{4}-\d{4}-\d{4}$'
			print("creado el patrón, voy a comprobar que coincide")
			if re.match(pattern, fc, flags=0):
				try:
					#c.execute("SELECT Contador FROM TContador WHERE Nombre ='addfc'")
					c.execute("SELECT Contador FROM TContador WHERE Nombre ='addfc'")
					for i in c:
						print(i[0])
						increment = i[0] +1
						#c.execute("UPDATE TContador SET Contador='" + str(increment) + "' WHERE Nombre = 'addfc'")
						c.execute("UPDATE TContador SET Contador = Contador + 1 WHERE Nombre = 'addfc'")
				except Exception as e:
					print(e)
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
				print("He entrado comprovando que el patrón es bueno")
				print("voy a mirar si el grupo ya existe")
				EG = existeGrupo(cid)
				print("estoy antes de EG == 0 y despues de EG = existeGrupo(cid)") 
				if (EG == 0):
					print("El Grupo no existe, ergo tengo que crearlo")
					print(m.chat.title)
					print(f"El nombre del chat es: {mct}")
					print("Ahora vamos a hacer el insert en el grupo")
					try:
						#c.execute(f"INSERT INTO Grupo (idGrupo,NombreGrup) VALUES ('{cid}','{mct}')")
						c.execute('INSERT INTO Grupo (idGrupo,NombreGrup) VALUES (?, ?)', (cid, mct,))
						print(f"El id del grupo {cid}")
						nocapital = uname.capitalize()
						#nocapital2 = "@" + str(nocapital)
						nocapital2 = f"@{nocapital}"
						EU = existeUser(uid)
						if(EU == 0):
							#c.execute(f"INSERT INTO Usuarios (idUsuario,ALIAS,FC) VALUES ('{uid}','@{nocapital}','{fc}')")
							c.execute("INSERT INTO Usuarios (idUsuario,ALIAS,FC) VALUES (?, ?, ?)", (uid, nocapital2, fc,))
					#	c.execute("INSERT INTO Usuarios (idUsuario,ALIAS,FC) VALUES ('" + str(uid) + "', '@" + uname.capitalize() + "','" + fc + "')")
						print("ESTOY DEBAJO DEL IF de ENTRE USUARIO = 0")
						#c.execute(f"INSERT INTO UsuGrupo(idUsuarioFK,idGrupoFK) VALUES ('{uid}','{cid}')")
						c.execute("INSERT INTO UsuGrupo (idUsuarioFK,idGrupoFK) VALUES (?, ?)", (uid, cid,))
						bot.send_message(cid, f"Se ha registrado a *{uname}* con Friend Code *{fc}*.", parse_mode="Markdown")
						con.commit()
					except sqlite3.Error as e:
						print(e)
						bot.send_message( cid, "Ya has introducido tu código a la DB en este grupo, si quieres editarlo usa /editfc.")
						
					
					
				elif(EG == 1):
					print("El grupo sí existe")
					nocapital = uname.capitalize()
					#nocapital2 = "@" + str(nocapital)
					nocapital2 = f"@{nocapital}"
					try:
						EU = existeUser(uid)
						if(EU == 0):
							#c.execute(f"INSERT INTO Usuarios (idUsuario,ALIAS,FC) VALUES ('{uid}', '@{nocapital}','{fc}')")
							c.execute("INSERT INTO Usuarios (idUsuario,ALIAS,FC) VALUES (?, ?, ?)", (uid, nocapital2, fc,))
					#	c.execute("INSERT INTO Usuarios (idUsuario,ALIAS,FC) VALUES ('" + str(uid) + "', '@" + uname.capitalize() + "','" + fc + "')")
						print("ESTOY DEBAJO DEL IF de ENTRE USUARIO = 0 Y AHORA VOY A COMPROBAR EUG")
						EUG = existeUserGru(uid,cid)
						print("Sabemos que EUG vale " + str(EUG))
						if(EUG == 0):
							print("Entro cuando no existe la combinación usuario - grupo")
							#c.execute(f"INSERT INTO UsuGrupo(idUsuarioFK,idGrupoFK) VALUES ('{uid}','{cid}')")
							c.execute("INSERT INTO UsuGrupo (idUsuarioFK,idGrupoFK) VALUES (?, ?)", (uid, cid,))
							bot.send_message(cid, f"Se ha registrado a *{uname}* con Friend Code *{fc}*.", parse_mode="Markdown")
						if(EUG == 1):
							bot.send_message( cid, "Ya has introducido tu código a la DB en este grupo, si quieres editarlo usa /editfc.")
						con.commit()
					except sqlite3.Error as e:
						print(e)
						bot.send_message( cid, "Ya has introducido tu código a la DB en este grupo, si quieres editarlo usa /editfc.")
						
			else:
				bot.send_message(cid, "El formato del comando es /addfc *XXXX-XXXX-XXXX* donde X son números.",
								 parse_mode="Markdown")
		except Exception as e:
			print("Except de L234. El addfc ha petado dentro del primer try, en el EG = existeGrupo(cid) de L179")
			print(e)
			bot.send_message(cid, "El formato del comando es /addfc *XXXX-XXXX-XXXX* donde X son números.",
							 parse_mode="Markdown")
							 


@bot.message_handler(commands=['editfc']) 
def command_editfc(m):
	cid = m.chat.id
	uid = m.from_user.id
	uname = m.from_user.username
	#uname2 = "@" + str(uname)
	uname2 = f'@{uname}'
	ufm = m.from_user.first_name
	ulm = m.from_user.last_name
	if (uname is None):
		uname = f"{ufm} {ulm}"
	else:
		uname = uname
	try:
		uname2 = f'@{uname}'
		fc = m.text.split(' ', 1)[1].replace(" ","")
		pattern = '^\d{4}-\d{4}-\d{4}$'
		if re.match(pattern, fc, flags=0):
			EU = existeUser(uid)
			if(EU == 1):
				try:
				  #c.execute(f"UPDATE Usuarios SET 'FC' = '{fc}', 'ALIAS'='@{uname}' WHERE idUsuario = '{uid}'")
				  c.execute("UPDATE Usuarios SET 'FC'=?, 'ALIAS'=? WHERE idUsuario=?", (fc, uname2, uid,))
				  print(c.fetchone())
				  bot.send_message( cid, f"Se ha cambiado el registro de *{uname2}* ahora con *Friend Code {fc}*.", parse_mode = "Markdown")
				  con.commit()
				except sqlite3.Error:
				  bot.send_message( cid, "Ha ocurrido un error. Inténtalo de nuevo.")
			else:
				bot.send_message( cid, "Para editar tu código amigo primero tienes que registrarte con /addfc.", parse_mode = "Markdown")
		else:
			
			bot.send_message(cid, "El formato del comando es /editfc *XXXX-XXXX-XXXX* donde X son números.", parse_mode = "Markdown")
	except Exception as e:
		print(e)
		bot.send_message( cid, "El formato del comando es /editfc *XXXX-XXXX-XXXX* donde X son números.", parse_mode = "Markdown")


@bot.message_handler(commands=['del'])
def command_deletebtag(m):
	cid = m.chat.id
	uid = m.from_user.id
	ufm = m.from_user.first_name
	ulm = m.from_user.last_name
	if (m.from_user.username is None):
		if (ulm is None):
			uname = ufm
		else:
			uname = f'{ufm} {ulm}'
	else:
		uname = m.from_user.username
	try:
		uname2 = f'@{uname}'
		fcid = m.text.split(' ', 1)[1].upper()
		print(fcid)
		if (str(fcid).startswith("MI FC")):
			reply = "Tu FC no está en la BBDD."
			try:
				print("1")
				#c.execute(f"SELECT FC FROM Usuarios WHERE idUsuario ='{uid}'")
				c.execute('SELECT FC FROM Usuarios WHERE idUsuario=?', (uid,))
				print("2")
				for i in c:
					print("3")
					if i[0] is None:
						print("4")
						reply = "Tu FC no está en la BBDD."
					else:
						print("5")
						fcid = i[0]
						#c.execute(f"DELETE FROM Usuarios WHERE FC = '{fcid}'")
						c.execute('DELETE FROM Usuarios WHERE FC=?', (fcid,))
						print("11")
						#c.execute(f"DELETE FROM UsuGrupo WHERE idUsuarioFK ='{uid}'")
						c.execute('DELETE FROM UsuGrupo WHERE idUsuarioFK=?', (uid,))
						print("12")
						reply = "Tu FC ha sido borrado de la BBDD."
						print("FC borrado de la Base de Datos :'(")
				bot.send_message(cid, reply, parse_mode = "Markdown")
				con.commit()
			except sqlite3.Error:			
			  bot.send_message(cid, "ExceptError: El formato del comando es `/del Mi FC`.", parse_mode="Markdown")
			  print("except sqlite3 L321")
		else:
			bot.send_message(cid, "ElseError: El formato del comando es `/del Mi FC`.", parse_mode="Markdown")
			print("else L324")
	except Exception as e:
		print("exception as e L327")
		print(e)
		bot.send_message(cid, "ExceptError: El formato del comando es `/del Mi FC`.", parse_mode="Markdown")



@bot.message_handler(commands=['mifc']) 
def command_mifc(m):
	cid = m.chat.id
	uid = m.from_user.id
	ufm = m.from_user.first_name
	ulm = m.from_user.last_name
	if (m.from_user.username is None):
		if (ulm == None):
			uname = ufm
		else:
			uname = f'{ufm} {ulm}'
	else:
		uname = m.from_user.username

	
	try:	
		uname2 = f'@{uname}'
		#c.execute(f"SELECT ALIAS,FC from Usuarios WHERE idUsuario={uid}")
		c.execute('SELECT ALIAS,FC from Usuarios WHERE idUsuario=?', (uid,))
		
		for i in c:
			alias_resultado = f"{i[0]} "
			fc_resultado = i[1]
			
		bot.send_message( cid, f'*{alias_resultado}*: `{fc_resultado}`', parse_mode = "Markdown")
		con.commit()
		try:
			#c.execute("SELECT Contador FROM TContador WHERE Nombre ='mifc'")
			c.execute("SELECT Contador FROM TContador WHERE Nombre ='mifc'")
			for i in c:
				print(i[0])
				increment = i[0] +1
				#c.execute("UPDATE TContador SET Contador='" + str(increment) + "' WHERE Nombre = 'mifc'")
				c.execute("UPDATE TContador SET Contador = Contador + 1 WHERE Nombre = 'mifc'")
		except Exception as e:
			print(e)
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
	except Exception as e:
		print(e)
		bot.send_message( cid, "Tu fc no aparece en la lista. Añadete con /addfc.", parse_mode = "Markdown")