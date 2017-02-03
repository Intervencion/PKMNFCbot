SELECT * Into DestinationTableName From SourceTableName Where 1 = 2
SELECT * INTO MyNewTable FROM MyTable



############### MEGAS ################

						if (m.text.lower().split(' ', 2)[2] == "mega"):
							
							mega = m.text.lower().split(' ', 2)[2]
							nomega = m.text.lower().split(' ', 2)[1]
							print("Este es el mensaje que comprueba si nos ha pedido una mega", mega)
							if (nomega =="venusaur" or nomega=="blastoise" or nomega=="charizard" or nomega=="alakazam" or nomega=="gengar" or nomega=="kangaskhan" or nomega=="pinsir" or nomega=="gyarados" or nomega=="aerodactyl" or nomega=="mewtwo" or nomega=="ampharos" or nomega=="scizor" or nomega=="heracross" or nomega=="houndoom" or nomega=="tyranitar" or nomega=="blaziken" or nomega=="gardevoir" or nomega=="mawile" or nomega=="aggron" or nomega=="medichamp" or nomega=="manectric" or nomega=="banette" or nomega=="absol" or nomega=="garchomp" or nomega=="lucario" or nomega=="pidgeot" or nomega=="sharpedo" or nomega=="salamance" or nomega=="abomasnow" or nomega=="beedrill"  or nomega=="slowbro" or nomega=="steelix" or nomega=="sceptile" or nomega=="swampert" or nomega=="sableye" or nomega=="camerut" or nomega=="altaria" or nomega=="glalie" or nomega=="metagross" or nomega=="latios"  or nomega=="latias"  or nomega=="rayquaza"  or nomega=="lopunny"  or nomega=="gallade" or nomega=="audino"  or nomega=="diancie"):
							nomega = [venusaur, blastoise, charizard, alakazam, gengar, kangaskhan, pinsir, gyarados, aerodactyl, mewtwo, ampharos, scizor, heracross, houndoom, tyranitar, blaziken, gardevoir, mawile, aggron, medichamp, manectric, banette, absol, garchomp, lucario, pidgeot, sharpedo, salamance, abomasnow, beedrill"  or nomega=="slowbro, steelix, sceptile, swampert, sableye, camerut, altaria, glalie, metagross, latios, latias, rayquaza, lopunny, gallade, audino, diancie]
							if m.text in [nomega]
							   print("Este poke sí tiene mega")
							else:
								print("Este poke no tiene mega")
								bot.reply_to(m, "Este pokémon no tiene mega, señor troll.")
								
								
						else:
							print("no ponía mega" , m.text.lower().split(' ', 2)[2])
							
nomega = [venusaur, blastoise, charizard, alakazam, gengar, kangaskhan, pinsir, gyarados, aerodactyl, mewtwo, ampharos, scizor, heracross, houndoom, tyranitar, blaziken, gardevoir, mawile, aggron, medichamp, manectric, banette, absol, garchomp, lucario, pidgeot, sharpedo, salamance, abomasnow, beedrill"  or nomega=="slowbro, steelix, sceptile, swampert, sableye, camerut, altaria, glalie, metagross, latios, latias, rayquaza, lopunny, gallade, audino, diancie]
	
							
							
@bot.message_handler(commands=['editfc']) 
def command_editfc(m):
	cid = m.chat.id
	uid = m.from_user.id
	if m.from_user.username == None:
		uname = m.from_user.first_name + " " + m.from_user.last_name
	else:
		uname = m.from_user.username
	if cid == grupos_admitidos or admins:
		try:
			fc = m.text.split(' ', 1)[1].replace(" ","")
			pattern = '^\d\d\d\d-\d\d\d\d-\d\d\d\d$'
			if re.match(pattern, fc, flags=0):
				try:
				    c.execute("UPDATE PKMN SET 'fc' = '" + fc +  "' WHERE iduser = " + str(uid))
				    bot.send_message( cid, "Se ha cambiado el registro de *" + uname + "* ahora con *Friend Code* *" + fc + "*.", parse_mode = "Markdown")
				    con.commit()
	
				except sqlite3.Error:
				    bot.send_message( cid, "Ha ocurrido un error. Inténtalo de nuevo.")
			else:
				
				bot.send_message(cid, "El formato del comando es /editfc *XXXX-XXXX-XXXX* donde X son números.", parse_mode = "Markdown")
		    
		except:
			bot.send_message( cid, "El formato del comando es /editfc *XXXX-XXXX-XXXX* donde X son números.", parse_mode = "Markdown")
	else:
		bot.send_message( cid, "Este bot solo funciona en grupos designados. Por ahora no se admiten nuevos grupos.")
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
################################# PARA MONTAR LA BD CON LOS POKEMON


k = 721
for i in range(0, k):
    
	url = 'http://pokeapi.co/api/v2/pokemon/' + k
	request = urllib.request.Request(url)
	request.add_header('User-Agent',"cheese")
    
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
		evhp =  datajson["stats"][5]['effort']
		evatk =  datajson["stats"][4]['effort']
		evdefe =  datajson["stats"][3]['effort']
		evatksp =  datajson["stats"][2]['effort']
		evdefsp =  datajson["stats"][1]['effort']
		evspd =  datajson["stats"][0]['effort']
		tipo1 = datajson["types"][0]["type"]["name"]
		tipo2 = datajson["types"][1]["type"]["name"]
		t = hp + atk + defe + atksp +defsp + spd
		sh = ""
		s0 = ""
		s1 = ""
		s2 = ""
		for r in datajson['abilities']:
			print(r)
			skill = datajson['abilities']
			#	hskill[i] = skill

#			print(datajson["species"])
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

c.execute("INSERT INTO POKEMON (idpkmn,Ndex,Nombre,Linkfoto,hp,atk,defe,atksp,defsp,spd,hab1,hab2,habo,tipo1,tipo2,evhp,evatk,evdefe,evatksp,evdefsp,evspd) VALUES (NULL," + npkmn + " , '" + name + "', '" + imgpkmn + "',"+ hp + ","+ atk + ","+ defe + ","+ atksp + ","+ defsp + ","+ spd + ",'Programasdor', 'Haker', 'Shurmano', 'Forero', 'Troll', "+ evhp + ","+ evatk + ","+ evdefe + ","+ evatksp + ","+ evdefsp + ","+ evspd + ")")
