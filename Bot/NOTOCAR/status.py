from config import *

@bot.message_handler(commands=['status']) 
def command_status(m):
	cid = m.chat.id
	uid = m.from_user.id
	adms = []	
	if cid < 0:
		admins = bot.get_chat_administrators(m.chat.id)
		estadisticas = ""
		c.execute("SELECT * FROM TContador")
		for i in c:
			print(f"{i[0]}: {i[1]}")
			estadisticas += f'`{i[0]}`: {i[1]}\n'
			for admin in range(len(admins)):
				r = admins[admin]
				adms.append(r.user.id)
				print('\n' + str(admins[admin]))
				print(adms)
				bot.send_message(cid, f'Administrador(es): {adms}')
				bot.send_message(cid, f'Info extensa:  {r}')
				bot.send_message(cid, f"Desde *2017-06-19 13:00:00*:\n{estadisticas}", parse_mode = "Markdown")
	else:
		bot.send_message(cid, 'Este comando solo funciona en grupos.')