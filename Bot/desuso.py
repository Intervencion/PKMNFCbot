
			
			
			@bot.message_handler(func=lambda m: m.text and m.text.startswith("!stats"))
			def command_stats(m):
				cid = m.chat.id
				bot.send_chat_action(cid, "typing")
				nomega = ["venusaur", "blastoise", "charizard", "alakazam", "gengar", "kangaskhan", "pinsir", "gyarados", "aerodactyl", "mewtwo", "ampharos", "scizor", "heracross", "houndoom", "tyranitar", "blaziken", "gardevoir", "mawile", "aggron", "medichamp", "manectric", "banette", "absol", "garchomp", "lucario", "pidgeot", "sharpedo", "salamance", "abomasnow", "beedrill", "slowbro", "steelix", "sceptile", "swampert", "sableye", "camerut", "altaria", "glalie", "metagross", "latios", "latias", "rayquaza", "lopunny", "gallade", "audino", "diancie"]
				k = 1
#					if ((cid in grupos_admitidos) or (cid in admins)):
				if k == 1:
					try:
						pkmn = m.text.lower().split(' ', 1)[1].replace(" ","-")
						url = 'http://pokeapi.co/api/v2/pokemon/' + pkmn
						request = urllib.request.Request(url)
						request.add_header('User-Agent',"cheese")
						
						##### PROBANDO TRADUCCION DE HABILIDAD

						
						############### MEGAS Y ALOLAS ############
						
#						if hasattr(m.text.lower().split(' ', 2)[2], 'attr_name'):
						try:
							if (m.text.lower().split(' ', 2)[2] == "mega"):
								pkmn = m.text.lower().split(' ', 2)[1]
								if(pkmn in nomega):
									print("Sé que pone mega y además tiene mega")
									imgpkm, name, hp, atk, defe, atksp, defsp, spd, t, s0 = es_mega(m,request)
									#ficha = "*" + name + "*" + "\n\n [ ](" + imgpkm + "\n`PS`: " + str(hp) + "\n`Ataque` " + str(atk) + "\n`Defensa` " + str(defe) + "\n`Atk. Especial` " + str(atksp) + "\n`Def. Especial` " + str(defsp) + "\n`Velocidad` " + str(spd) + "\n`Total` " + str(t) + "\n\n`Habilidad 1` " + str(s0) + "\n\n["+ name + " en Smogon](http://www.smogon.com/dex/xy/pokemon/" + name + ")"
									ficha_mega = "*" + name + "*" + "\n`PS`: " + str(hp) + "\n`Ataque` " + str(atk) + "\n`Defensa` " + str(defe) + "\n`Atk. Especial` " + str(atksp) + "\n`Def. Especial` " + str(defsp) + "\n`Velocidad` " + str(spd) + "\n`Total` " + str(t) + "\n\n`Habilidad 1` " + str(s0) + "\n\n[ ](" + imgpkm
									markup = types.InlineKeyboardMarkup()
									markup.add(types.InlineKeyboardButton(pkmn, callback_data = "pkmn"))
									bot.reply_to(m, ficha_mega, reply_markup=markup, parse_mode = "Markdown")
									
									@bot.callback_query_handler(func=lambda call: call.data == "pkmn")
									def r0_call_back(call):
										editm = call.message.message_id
										markup = types.InlineKeyboardMarkup()
										markup.add(types.InlineKeyboardButton(pkmn + " mega", callback_data = "pkmn_mega"))
										print("POKÉMON SEGUNDO",editm)
										print(call.message.chat.id)
										bot.edit_message_text(ficha_mega, call.message.chat.id , editm, reply_markup=markup, parse_mode = "Markdown")
										bot.answer_callback_query(call.id, text="Llamando a " + pkmn) #Sale en pantalla

									
								#	markup = types.InlineKeyboardMarkup()
								#	markup.add(types.InlineKeyboardButton(pkmn, callback_data="data1"))
								#	bot.send_message(cid, ficha, reply_markup=markup, parse_mode = "Markdown")
								else:
									print("Este poke no tiene mega")
									bot.reply_to(m, "Este pokémon no tiene mega, señor trol l.")
									
						except:
							print("no ponía mega")
#							if(pkmn in nomega):
#						if (m.text.lower().split(' ', 2)[2] == "mega"):
#							
#							
#							pkmn = m.text.lower().split(' ', 2)[1]
#							if(pkmn in nomega):
#								imgpkm, hp, atk, defe, atksp, defsp, spd, t, s0 = tiene_mega(m,request)
#							else:
#								print("Este poke no tiene mega")
#								bot.reply_to(m, "Este pokémon no tiene mega, señor troll.")
#								bot.send_message(cid, "Este poke no tiene mega")
#
#
#						else:
#							print("no ponía mega" , m.text.lower().split(' ', 2)[2])


			
					### AQUI ABAJO CONTROLAMOS QUE EXISTA LO QUE ESCRIBE EL USER TROLL DE TURNO
						data = urllib.request.urlopen(request)
						datajson = json.loads(data.read().decode(data.info().get_param('charset') or 'utf-8'))
						name = datajson["forms"][0]['name'].title()
						if 'stats' in datajson:
							hp =  datajson["stats"][5]['base_stat']
							atk = datajson["stats"][4]['base_stat']
							defe = datajson["stats"][3]['base_stat']
							atksp = datajson["stats"][2]['base_stat']
							defsp= datajson["stats"][1]['base_stat']
							spd = datajson["stats"][0]['base_stat']
							t = hp + atk + defe + atksp +defsp + spd
							hskill = []
							sh = "No tiene"
							s0 = "No tiene"
							s1 = "No tiene"
							s2 = "No tiene"
							for r in datajson['abilities']:
								
								print(r)
						
						
								skill = datajson['abilities']
							#	hskill[i] = skill
				
#				print(datajson["species"])
							print("ahora debo devolver el nombre de la habilidad")
							print(str(datajson['id']).zfill(5))
							npkmn = str(datajson['id']).zfill(5)
							imgpkm = "https://raw.githubusercontent.com/Intervencion/PKMNFCbot/master/Sprites/" + str(npkmn) + ".png)"
							print(skill[0]['ability']['name'])
							print()
							print(len(skill))
							i = len(skill)
							print(skill[0]['is_hidden'])
							
							
							if i==1:
								s0 = una_habilidad(skill, s0)
							
							elif i==2:
								sh, s0, s1 = dos_habilidades(skill, sh, s0, s1)
									
							elif i==3:
								sh, s0, s1, s2 = tres_habilidades(skill, sh, s0, s1, s2)

							print("debería funcionar")
							sh = sh.replace("-"," ").title()
							s0 = s0.replace("-"," ").title()
							s1 = s1.replace("-"," ").title()
							s2 = s2.replace("-"," ").title()
							
							print("ahora voy a poner los iconos")
							if hp<=60:
								cbhp = "📕"
							elif (hp>60 and hp<=80):
								cbhp = "📙"
							elif (hp>80 and hp<=100):
								cbhp = "📒"
							elif hp>100:
								cbhp = "📗"
							
###################################### EL BOTÓN DE LA MEGA ##################
							print("iconos puestos")
							markup = types.InlineKeyboardMarkup()
#							markup.add(types.InlineKeyboardButton("result1", callback_data="data1"))
						#	mega = m.text.lower().split(' ', 2)[2]
						#	print(mega)
							print("voy a mandar el mensaje")
							bot.reply_to(m,
							"*" + name + "*\n" + tipos + "\n\n`PS`: " + str(cbhp) + str(hp) +
							"\n`Ataque` " + str(atk) + "\n`Defensa` " + str(defe) + "\n`Atk. Especial` " + str(atksp) + 
							"\n`Def. Especial` " + str(defsp) + "\n`Velocidad` " + str(spd) + "\n`Total` " + str(t) + 
							"\n\n`Habilidad 1` " + str(s1) + "\n`Habilidad 2` " + str(s0) + "\n`Hab. Oculta` " + str(sh) + "[ ](" + imgpkm 
							+ "\n\n["+name+ " en Smogon](http://www.smogon.com/dex/xy/pokemon/" + name + ")",reply_markup=markup, parse_mode = "Markdown")
						else:
							bot.reply_to(m, "dep")
					except:
						bot.send_message(cid, "Que no hay séptima, so pesado. Y eso no es un pokémon.", parse_mode = "Markdown")
				else:
					bot.send_message( cid, "Este bot solo funciona en grupos designados. Para entrar en la lista blanca usa /contact desde el grupo en el que quieras usar el bot y evaluaremos el caso.")
    







###########################################################
######################## EJEMPLO JSON #####################
#@bot.message_handler(commands=['rae'])
#def command_rae(m):
     
#      cid = m.chat.id
#      msg = m.text[5:]
#      link = urllib.urlopen("http://dulcinea.herokuapp.com/api/?query=" + msg)
#      data = json.loads(link.read())
#      for r in data['response']:
#            if 'meanings' in r:
#                bot.send_message(cid, data["response"][0]["meanings"][0]["meaning"])
#                bot.send_message(cid, data["response"][1]["meanings"][0]["meaning"])
#                break;
#           else:
#                bot.send_message(cid, "Error en la busqueda")
 








######################################################
################ MÉTODO 1 ###########################
#@bot.message_handler(commands=['stats'])
#def command_stats(m):
#	cid = m.chat.id
#	if ((cid in grupos_admitidos) or (cid in admins)):
#		pkmn = m.text.split(' ', 1)[1].replace(" ","")
#		bot.send_message(cid, "este es el mensaje " + pkmn)
#		link = urllib.request.urlopen('http://pokeapi.co/api/v2/pokemon/' + pkmn)
#		data = json.loads(link.read().decode(response.info().get_param('charset') or 'utf-8')
#		bot.send_message(cid, data["stats"][0]['base_stat'])
#	else:
#		bot.send_message( cid, "Este bot solo funciona en grupos designados. Para entrar en la lista blanca usa /contact desde el grupo en el que quieras usar el bot y evaluaremos el caso.")







######################################################
################ MÉTODO 3 ###########################
	
#@bot.message_handler(commands=['stats'])
#def command_stats(m):
#	cid = m.chat.id
#	if ((cid in grupos_admitidos) or (cid in admins)):
#		pkmn = m.text.split(' ', 1)[1].replace(" ","")
#		bot.send_message(cid, "este es el mensaje " + pkmn)
#		link = urllib.request.urlopen('http://pokeapi.co/api/v2/pokemon/' + pkmn)
#		data = json.loads(link.read())
#		for r in data['stats']:
#			if 'stat' in data:
#		bot.send_message(cid, data["stats"][0]['base_stat'])
#				break;
#			else:
#				bot.send_message(cid, "Error en la busqueda")
#	else:
#		bot.send_message( cid, "Este bot solo funciona en grupos designados. Para entrar en la lista blanca usa /contact desde el grupo en el que quieras usar el bot y evaluaremos el caso.")






####################################################################################
######################################EXTERNAS######################################






def es_mega(m, request):
	print("Este poke sí tiene mega")
	data = urllib.request.urlopen(request)
	datajson = json.loads(data.read().decode(data.info().get_param('charset') or 'utf-8'))
	name = datajson["forms"][0]['name'].title()
	pkmn = m.text.lower().split(' ', 2)[1]
	if 'stats' in datajson:
		hp =  datajson["stats"][5]['base_stat']
		print ("Aquí los evs de hp que da este poke")
		print(datajson["stats"][5]['effort'])
		atk = datajson["stats"][4]['base_stat']
		defe = datajson["stats"][3]['base_stat']
		atksp = datajson["stats"][2]['base_stat']
		defsp= datajson["stats"][1]['base_stat']
		spd = datajson["stats"][0]['base_stat']
		print("ahora vienen los tipos?")
		print(datajson["types"][0]["type"]["name"])
		t = hp + atk + defe + atksp +defsp + spd
		s0 = "No tiene"
#		skill = []
		skill = datajson['abilities']
		print("ahora debo devolver el nombre de la habilidad")
		print(str(datajson['species']['url']))
		j = str(datajson['species']['url']).split('/', 6)[6].replace("/", "")
		j = j.zfill(5)
		j= int(j) + 10000
		imgpkm = "https://raw.githubusercontent.com/Intervencion/PKMNFCbot/master/Sprites/" + str(j) + ".png"
		print (imgpkm)
		print(skill[0]['ability']['name'])
		s0 = skill[0]['ability']['name'].capitalize().replace("-", " ")
		print()
		print(len(skill))
		i = len(skill)
		print(skill[0]['is_hidden'])
		return imgpkm, name, hp, atk, defe, atksp, defsp, spd, t, s0


def tiene_mega(m,request):
	data = urllib.request.urlopen(request)
	datajson = json.loads(data.read().decode(data.info().get_param('charset') or 'utf-8'))
	name = datajson["forms"][0]['name'].title()
	if 'stats' in datajson:
		hp =  datajson["stats"][5]['base_stat']
		atk = datajson["stats"][4]['base_stat']
		defe = datajson["stats"][3]['base_stat']
		atksp = datajson["stats"][2]['base_stat']
		defsp= datajson["stats"][1]['base_stat']
		spd = datajson["stats"][0]['base_stat']
		t = hp + atk + defe + atksp +defsp + spd
		hskill = []
		sh = "No tiene"
		s0 = "No tiene"
		s1 = "No tiene"
		s2 = "No tiene"
		for r in datajson['abilities']:
			print(r)
			skill = datajson['abilities']
			print("ahora debo devolver el nombre de la habilidad")
			print(str(datajson['id']).zfill(5))
		npkmn = str(datajson['id']).zfill(5)
		imgpkm = "https://raw.githubusercontent.com/Intervencion/PKMNFCbot/master/Sprites/" + str(npkmn) + ".png)"
		print(skill[0]['ability']['name'])
		print()
		print(len(skill))
		i = len(skill)
		print(skill[0]['is_hidden'])
					
							
		if i==1:
			s0 = una_habilidad(skill, s0)
							
		if i==2:
			sh, s0, s1 = dos_habilidades(skill, sh, s0, s1)
								
		if i==3:
			sh, s0, s1, s2 = tres_habilidades(skill, sh, s0, s1, s2)

		print("debería funcionar")
		sh = sh.replace("-"," ").title()
		s0 = s0.replace("-"," ").title()
		s1 = s1.replace("-"," ").title()
		s2 = s2.replace("-"," ").title()
	return imgpkm, name, hp, atk, defe, atksp, defsp, spd, t, s0, s1, s2, sh







def una_habilidad(skill, s0):
	print("Entro en la función 1")
	s0 = skill[0]['ability']['name']
	return s0
#

def dos_habilidades(skill, sh, s0, s1):
	print("Entro en la función 2")
	print(skill[0])
	print(skill[1])
	if skill[0]['is_hidden'] == True:
		print("Tiene 1 habilidad y una oculta    1")
		sh = skill[0]['ability']['name']
		s1 = skill[1]['ability']['name']
									
	if skill[1]['is_hidden'] == True:
		print("Tiene 1 habilidad y una oculta    2")
		sh = skill[1]['ability']['name']
		s0= skill[0]['ability']['name']
									
	if (skill[0]['is_hidden'] == False) and (skill[1]['is_hidden'] == False):
		print("Tiene 2 habilidades y no oculta")
		s0 = skill[0]['ability']['name']
		s1 = skill[1]['ability']['name']
	return sh,s0,s1
##

def tres_habilidades(skill, sh, s0, s1, s2):
	print("Entro en la función 3")
	if skill[0]['is_hidden'] == True:
		print("Tiene 2 habilidad y una oculta    1")
		sh = skill[0]['ability']['name']
		s1 = skill[1]['ability']['name']
		s2 = skill[2]['ability']['name']
	
	if skill[1]['is_hidden'] == True:
		print("Tiene 2 habilidad y una oculta    2")
		sh = skill[1]['ability']['name']
		s0= skill[0]['ability']['name']
		s2 = skill[2]['ability']['name']
	
	if skill[2]['is_hidden'] == True:
		print("Tiene 2 habilidad y una oculta    3")
		sh = skill[2]['ability']['name']
		s0= skill[0]['ability']['name']
		s1 = skill[1]['ability']['name']
		
	if (skill[0]['is_hidden'] == False) and (skill[1]['is_hidden'] == False) and (skill[2]['is_hidden'] == False):
		print("Tiene 3 habilidad y no oculta")
		s0 = skill[0]['ability']['name']
		s1 = skill[1]['ability']['name']
		s2 = skill[2]['ability']['name']
	return sh,s0,s1,s2
###