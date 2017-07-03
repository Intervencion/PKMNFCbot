from config import *

def listener(messages):
	for m in messages:
		cid = m.chat.id
		uid = m.from_user.id
		uname = m.from_user.username
		mct = m.chat.title
		ufm = m.from_user.first_name
		ulm = m.from_user.last_name
			
	#if m.content_type == 'text':
		if m.text:



##########################################################
#################### Encuesta Bienvenida #################
			@bot.message_handler(func=lambda m: True, content_types=['new_chat_member'])
			def on_user_joins(m):
				cid = m.chat.id
				bienvenida = ""
				if(m.new_chat_member.username=="PKMNFCbot"):
					l= 1
				
				else:
					if (m.new_chat_member.username is None):
						nun = ""
						nun = m.new_chat_member.first_name
						if (m.new_chat_member.last_name is not None):
							nun += " "
							nun += m.new_chat_member.last_name
							bienvenida = f'Bienvenido al grupo {mct} '
						else: 
							bienvenida = f'Bienvenido al grupo {mct} '
					else:
						nun = m.new_chat_member.username
						bienvenida = f'Bienvenido al grupo {mct} @'
					bot.send_message(cid, f'''{bienvenida}{nun}
					, vamos a proceder a hacerte la encuesta de entrada:\n 1.- ¿Nostalfag?\n 2.- ¿Charmander, Squirtle o Bulbasaur?\n 3.-¿Legalfag o Piratafag?\n 4.-¿Fola sí o Fola no?\n<a href='https://raw.githubusercontent.com/Intervencion/PKMNFCbot/master/Audios/pokemon.mp3'>⁣</a>\nSi te interesa saber las funciones que tiene RotomDex, ábreme chat en PRIVADO y hazme /help''', parse_mode = "HTML")
			mensaje = f"{{autogreen}}User:{{/green}} {ufm}\n"
			if cid < 0:
				mensaje += f"{{autoyellow}}Chat:{{/yellow}} {mct}\n"
				mensaje += f"{{autored}}Hora:{{/red}} {hora}\n"
				mensaje += f"{{autocyan}}UserID:{{/cyan}} [{uid}]"
			if cid < 0:
				mensaje += f"{{autoblue}} ChatID:{{/blue}} [{cid}]"
				mensaje += "\n"
				mensaje += f"{{automagenta}}Mensaje:{{/magenta}} {m.text}\n"
				mensaje += "{autoblack}-------------------------------{/black}\n"
			else:
				mensaje += f"{{autored}}Hora:{{/red}} {hora}\n"
				mensaje += f"{{autocyan}}UserID:{{/cyan}} [{uid}] "
				mensaje += f"{{automagenta}}Mensaje:{{/magenta}} {m.text}\n"
				mensaje += "{autoblack}-------------------------------{/black}\n"
				
			if(m.text.startswith("!") or m.text.startswith("/")):
				f = open('log.txt', 'a')
				f.write(mensaje)
				f.close()
				patata = open('id.txt', 'a')
				patata.write(f'@{uname} [{uid}]\n')
				patata.close()
				print (Color(str(mensaje)))

bot.set_update_listener(listener)