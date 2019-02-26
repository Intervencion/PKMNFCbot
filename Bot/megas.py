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





c.execute("""
INSERT INTO POKEMON (idpkmn,Ndex,Nombre,Link_Foto,Puntos_Salud,
Ataque,Defensa,Ataque_Especial,Defensa_Especial,Velocidad,Habilidad_1,
Habilidad_2,Habilidad_Oculta,tipo1,tipo2,ev_Puntos_Salud,ev_Ataque,
ev_Defensa,ev_Ataque_Especial,ev_Defensa_Especial,ev_Velocidad)
VALUES (NULL, 11150, 'Mewtwo Mega Y', 'https://raw.githubusercontent.com/Intervencion/PKMNFCbot/master/Sprites/11150.png',
106,150,70,194,120,140,
'Insomnio',' ',' ','Psíquico',' ',
0000000, 0000000, 0000000, 0000000, 0000000, 0000000)
""")

c.execute("""
INSERT INTO POKEMON (idpkmn,Ndex,Nombre,Link_Foto,Puntos_Salud,
Ataque,Defensa,Ataque_Especial,Defensa_Especial,Velocidad,Habilidad_1,
Habilidad_2,Habilidad_Oculta,tipo1,tipo2,ev_Puntos_Salud,ev_Ataque,
ev_Defensa,ev_Ataque_Especial,ev_Defensa_Especial,ev_Velocidad)
VALUES (NULL, 10150, 'Mewtwo Mega X', 'https://raw.githubusercontent.com/Intervencion/PKMNFCbot/master/Sprites/10150.png',
106,190,100,154,100,130,
'Impasible',' ',' ','Psíquico','Lucha',
0000000, 0000000, 0000000, 0000000, 0000000, 0000000)
""")

c.execute("""
INSERT INTO POKEMON (idpkmn,Ndex,Nombre,Link_Foto,Puntos_Salud,
Ataque,Defensa,Ataque_Especial,Defensa_Especial,Velocidad,Habilidad_1,
Habilidad_2,Habilidad_Oculta,tipo1,tipo2,ev_Puntos_Salud,ev_Ataque,
ev_Defensa,ev_Ataque_Especial,ev_Defensa_Especial,ev_Velocidad)
VALUES (NULL, 10719, 'Diancie Mega', 'https://raw.githubusercontent.com/Intervencion/PKMNFCbot/master/Sprites/10719.png',
50,160,110,160,110,110,
'Espejo Mágico',' ',' ','Roca','Hada',
0000000, 0000000, 0000000, 0000000, 0000000, 0000000)
""")

c.execute("""
INSERT INTO POKEMON (idpkmn,Ndex,Nombre,Link_Foto,Puntos_Salud,
Ataque,Defensa,Ataque_Especial,Defensa_Especial,Velocidad,Habilidad_1,
Habilidad_2,Habilidad_Oculta,tipo1,tipo2,ev_Puntos_Salud,ev_Ataque,
ev_Defensa,ev_Ataque_Especial,ev_Defensa_Especial,ev_Velocidad)
VALUES (NULL, 10531, 'Audino Mega', 'https://raw.githubusercontent.com/Intervencion/PKMNFCbot/master/Sprites/10531.png',
103,60,126,80,126,50,
'Alma Cura',' ',' ','Hada','Normal',
0000000, 0000000, 0000000, 0000000, 0000000, 0000000)
""")

c.execute("""
INSERT INTO POKEMON (idpkmn,Ndex,Nombre,Link_Foto,Puntos_Salud,
Ataque,Defensa,Ataque_Especial,Defensa_Especial,Velocidad,Habilidad_1,
Habilidad_2,Habilidad_Oculta,tipo1,tipo2,ev_Puntos_Salud,ev_Ataque,
ev_Defensa,ev_Ataque_Especial,ev_Defensa_Especial,ev_Velocidad)
VALUES (NULL, 10475, 'Gallade Mega', 'https://raw.githubusercontent.com/Intervencion/PKMNFCbot/master/Sprites/10475.png',
68,165,95,65,115,110,
'Foco Interno',' ',' ','Lucha','Psíquico',
0000000, 0000000, 0000000, 0000000, 0000000, 0000000)
""")

c.execute("""
INSERT INTO POKEMON (idpkmn,Ndex,Nombre,Link_Foto,Puntos_Salud,
Ataque,Defensa,Ataque_Especial,Defensa_Especial,Velocidad,Habilidad_1,
Habilidad_2,Habilidad_Oculta,tipo1,tipo2,ev_Puntos_Salud,ev_Ataque,
ev_Defensa,ev_Ataque_Especial,ev_Defensa_Especial,ev_Velocidad)
VALUES (NULL, 10428, 'Rayquaza Mega', 'https://raw.githubusercontent.com/Intervencion/PKMNFCbot/master/Sprites/10428.png',
65,136,94,54,96,135,
'Intrépido',' ',' ','Lucha','Normal',
0000000, 0000000, 0000000, 0000000, 0000000, 0000000)
""")

c.execute("""
INSERT INTO POKEMON (idpkmn,Ndex,Nombre,Link_Foto,Puntos_Salud,
Ataque,Defensa,Ataque_Especial,Defensa_Especial,Velocidad,Habilidad_1,
Habilidad_2,Habilidad_Oculta,tipo1,tipo2,ev_Puntos_Salud,ev_Ataque,
ev_Defensa,ev_Ataque_Especial,ev_Defensa_Especial,ev_Velocidad)
VALUES (NULL, 10384, 'Rayquaza Mega', 'https://raw.githubusercontent.com/Intervencion/PKMNFCbot/master/Sprites/10384.png',
105,180,100,180,100,115,
'Ráfaga Delta',' ',' ','Dragón','Volador',
0000000, 0000000, 0000000, 0000000, 0000000, 0000000)
""")

c.execute("""
INSERT INTO POKEMON (idpkmn,Ndex,Nombre,Link_Foto,Puntos_Salud,
Ataque,Defensa,Ataque_Especial,Defensa_Especial,Velocidad,Habilidad_1,
Habilidad_2,Habilidad_Oculta,tipo1,tipo2,ev_Puntos_Salud,ev_Ataque,
ev_Defensa,ev_Ataque_Especial,ev_Defensa_Especial,ev_Velocidad)
VALUES (NULL, 10380, 'Latias Mega', 'https://raw.githubusercontent.com/Intervencion/PKMNFCbot/master/Sprites/10380.png',
80,100,120,140,150,110,
'Levitación',' ',' ','Dragón','Psíquico',
0000000, 0000000, 0000000, 0000000, 0000000, 0000000)
""")

c.execute("""
INSERT INTO POKEMON (idpkmn,Ndex,Nombre,Link_Foto,Puntos_Salud,
Ataque,Defensa,Ataque_Especial,Defensa_Especial,Velocidad,Habilidad_1,
Habilidad_2,Habilidad_Oculta,tipo1,tipo2,ev_Puntos_Salud,ev_Ataque,
ev_Defensa,ev_Ataque_Especial,ev_Defensa_Especial,ev_Velocidad)
VALUES (NULL, 10381, 'Latios Mega', 'https://raw.githubusercontent.com/Intervencion/PKMNFCbot/master/Sprites/10381.png',
80,130,100,160,120,110,
'Levitación',' ',' ','Dragón','Psíquico',
0000000, 0000000, 0000000, 0000000, 0000000, 0000000)
""")

c.execute("""
INSERT INTO POKEMON (idpkmn,Ndex,Nombre,Link_Foto,Puntos_Salud,
Ataque,Defensa,Ataque_Especial,Defensa_Especial,Velocidad,Habilidad_1,
Habilidad_2,Habilidad_Oculta,tipo1,tipo2,ev_Puntos_Salud,ev_Ataque,
ev_Defensa,ev_Ataque_Especial,ev_Defensa_Especial,ev_Velocidad)
VALUES (NULL, 10373, 'Salamence Mega', 'https://raw.githubusercontent.com/Intervencion/PKMNFCbot/master/Sprites/10373.png',
95,145,130,120,90,120,
'Piel Celeste',' ',' ','Dragón','Volador',
0000000, 0000000, 0000000, 0000000, 0000000, 0000000)
""")

c.execute("""
INSERT INTO POKEMON (idpkmn,Ndex,Nombre,Link_Foto,Puntos_Salud,
Ataque,Defensa,Ataque_Especial,Defensa_Especial,Velocidad,Habilidad_1,
Habilidad_2,Habilidad_Oculta,tipo1,tipo2,ev_Puntos_Salud,ev_Ataque,
ev_Defensa,ev_Ataque_Especial,ev_Defensa_Especial,ev_Velocidad)
VALUES (NULL, 10376, 'Metagross Mega', 'https://raw.githubusercontent.com/Intervencion/PKMNFCbot/master/Sprites/10376.png',
80,145,150,105,110,110,
'Garra Dura',' ',' ','Acero','Psíquico',
0000000, 0000000, 0000000, 0000000, 0000000, 0000000)
""")

c.execute("""
INSERT INTO POKEMON (idpkmn,Ndex,Nombre,Link_Foto,Puntos_Salud,
Ataque,Defensa,Ataque_Especial,Defensa_Especial,Velocidad,Habilidad_1,
Habilidad_2,Habilidad_Oculta,tipo1,tipo2,ev_Puntos_Salud,ev_Ataque,
ev_Defensa,ev_Ataque_Especial,ev_Defensa_Especial,ev_Velocidad)
VALUES (NULL, 10362, 'Glalie Mega', 'https://raw.githubusercontent.com/Intervencion/PKMNFCbot/master/Sprites/10362.png',
80,120,80,120,80,100,
'Piel Helada',' ',' ','Hielo',' ',
0000000, 0000000, 0000000, 0000000, 0000000, 0000000)
""")

c.execute("""
INSERT INTO POKEMON (idpkmn,Ndex,Nombre,Link_Foto,Puntos_Salud,
Ataque,Defensa,Ataque_Especial,Defensa_Especial,Velocidad,Habilidad_1,
Habilidad_2,Habilidad_Oculta,tipo1,tipo2,ev_Puntos_Salud,ev_Ataque,
ev_Defensa,ev_Ataque_Especial,ev_Defensa_Especial,ev_Velocidad)
VALUES (NULL, 10334, 'Altaria Mega', 'https://raw.githubusercontent.com/Intervencion/PKMNFCbot/master/Sprites/10334.png',
75,110,110,110,105,80,
'Piel Feérica',' ',' ','Dragón','Volador',
0000000, 0000000, 0000000, 0000000, 0000000, 0000000)
""")

c.execute("""
INSERT INTO POKEMON (idpkmn,Ndex,Nombre,Link_Foto,Puntos_Salud,
Ataque,Defensa,Ataque_Especial,Defensa_Especial,Velocidad,Habilidad_1,
Habilidad_2,Habilidad_Oculta,tipo1,tipo2,ev_Puntos_Salud,ev_Ataque,
ev_Defensa,ev_Ataque_Especial,ev_Defensa_Especial,ev_Velocidad)
VALUES (NULL, 10323, 'Camerut Mega', 'https://raw.githubusercontent.com/Intervencion/PKMNFCbot/master/Sprites/10323.png',
70,120,100,145,105,20,
'Potencia Bruta',' ',' ','Fuego','Tierra',
0000000, 0000000, 0000000, 0000000, 0000000, 0000000)
""")

c.execute("""
INSERT INTO POKEMON (idpkmn,Ndex,Nombre,Link_Foto,Puntos_Salud,
Ataque,Defensa,Ataque_Especial,Defensa_Especial,Velocidad,Habilidad_1,
Habilidad_2,Habilidad_Oculta,tipo1,tipo2,ev_Puntos_Salud,ev_Ataque,
ev_Defensa,ev_Ataque_Especial,ev_Defensa_Especial,ev_Velocidad)
VALUES (NULL, 10302, 'Sableye Mega', 'https://raw.githubusercontent.com/Intervencion/PKMNFCbot/master/Sprites/10302.png',
50,85,125,85,115,20,
'Espejo Mágico',' ',' ','Siniestro','Fantasma',
0000000, 0000000, 0000000, 0000000, 0000000, 0000000)
""")

c.execute("""
INSERT INTO POKEMON (idpkmn,Ndex,Nombre,Link_Foto,Puntos_Salud,
Ataque,Defensa,Ataque_Especial,Defensa_Especial,Velocidad,Habilidad_1,
Habilidad_2,Habilidad_Oculta,tipo1,tipo2,ev_Puntos_Salud,ev_Ataque,
ev_Defensa,ev_Ataque_Especial,ev_Defensa_Especial,ev_Velocidad)
VALUES (NULL, 10260, 'Swampert Mega', 'https://raw.githubusercontent.com/Intervencion/PKMNFCbot/master/Sprites/10260.png',
100,150,110,95,110,70,
'Nado Rápido',' ',' ','Tierra','Agua',
0000000, 0000000, 0000000, 0000000, 0000000, 0000000)
""")

c.execute("""
INSERT INTO POKEMON (idpkmn,Ndex,Nombre,Link_Foto,Puntos_Salud,
Ataque,Defensa,Ataque_Especial,Defensa_Especial,Velocidad,Habilidad_1,
Habilidad_2,Habilidad_Oculta,tipo1,tipo2,ev_Puntos_Salud,ev_Ataque,
ev_Defensa,ev_Ataque_Especial,ev_Defensa_Especial,ev_Velocidad)
VALUES (NULL, 10254, 'Sceptile Mega', 'https://raw.githubusercontent.com/Intervencion/PKMNFCbot/master/Sprites/10254.png',
70,110,75,145,85,145,
'Pararayos',' ',' ','Dragón','Planta',
0000000, 0000000, 0000000, 0000000, 0000000, 0000000)
""")

c.execute("""
INSERT INTO POKEMON (idpkmn,Ndex,Nombre,Link_Foto,Puntos_Salud,
Ataque,Defensa,Ataque_Especial,Defensa_Especial,Velocidad,Habilidad_1,
Habilidad_2,Habilidad_Oculta,tipo1,tipo2,ev_Puntos_Salud,ev_Ataque,
ev_Defensa,ev_Ataque_Especial,ev_Defensa_Especial,ev_Velocidad)
VALUES (NULL, 10208, 'Steelix Mega', 'https://raw.githubusercontent.com/Intervencion/PKMNFCbot/master/Sprites/10208.png',
75,125,230,55,95,30,
'Poder Arena',' ',' ','Acero','Tierra',
0000000, 0000000, 0000000, 0000000, 0000000, 0000000)
""")

c.execute("""
INSERT INTO POKEMON (idpkmn,Ndex,Nombre,Link_Foto,Puntos_Salud,
Ataque,Defensa,Ataque_Especial,Defensa_Especial,Velocidad,Habilidad_1,
Habilidad_2,Habilidad_Oculta,tipo1,tipo2,ev_Puntos_Salud,ev_Ataque,
ev_Defensa,ev_Ataque_Especial,ev_Defensa_Especial,ev_Velocidad)
VALUES (NULL, 10080, 'Slowbro Mega', 'https://raw.githubusercontent.com/Intervencion/PKMNFCbot/master/Sprites/10080.png',
95,75,180,130,80,30,
'Caparazón',' ',' ','Psíquico','Agua',
0000000, 0000000, 0000000, 0000000, 0000000, 0000000)
""")

c.execute("""
INSERT INTO POKEMON (idpkmn,Ndex,Nombre,Link_Foto,Puntos_Salud,
Ataque,Defensa,Ataque_Especial,Defensa_Especial,Velocidad,Habilidad_1,
Habilidad_2,Habilidad_Oculta,tipo1,tipo2,ev_Puntos_Salud,ev_Ataque,
ev_Defensa,ev_Ataque_Especial,ev_Defensa_Especial,ev_Velocidad)
VALUES (NULL, 10460, 'Abomasnow Mega', 'https://raw.githubusercontent.com/Intervencion/PKMNFCbot/master/Sprites/10460.png',
90,132,105,135,105,30,
'Nevada',' ',' ','Planta','Hielo',
0000000, 0000000, 0000000, 0000000, 0000000, 0000000)
""")

c.execute("""
INSERT INTO POKEMON (idpkmn,Ndex,Nombre,Link_Foto,Puntos_Salud,
Ataque,Defensa,Ataque_Especial,Defensa_Especial,Velocidad,Habilidad_1,
Habilidad_2,Habilidad_Oculta,tipo1,tipo2,ev_Puntos_Salud,ev_Ataque,
ev_Defensa,ev_Ataque_Especial,ev_Defensa_Especial,ev_Velocidad)
VALUES (NULL, 10319, 'Sharpedo Mega', 'https://raw.githubusercontent.com/Intervencion/PKMNFCbot/master/Sprites/10319.png',
70,140,70,110,65,105,
'Mandíbula Fuerte',' ',' ','Agua','Siniestro',
0000000, 0000000, 0000000, 0000000, 0000000, 0000000)
""")

c.execute("""
INSERT INTO POKEMON (idpkmn,Ndex,Nombre,Link_Foto,Puntos_Salud,
Ataque,Defensa,Ataque_Especial,Defensa_Especial,Velocidad,Habilidad_1,
Habilidad_2,Habilidad_Oculta,tipo1,tipo2,ev_Puntos_Salud,ev_Ataque,
ev_Defensa,ev_Ataque_Especial,ev_Defensa_Especial,ev_Velocidad)
VALUES (NULL, 10018, 'Pidgeot Mega', 'https://raw.githubusercontent.com/Intervencion/PKMNFCbot/master/Sprites/10018.png',
83,80,80,135,80,121,
'Indefenso',' ',' ','Normal','Volador',
0000000, 0000000, 0000000, 0000000, 0000000, 0000000)
""")

c.execute("""
INSERT INTO POKEMON (idpkmn,Ndex,Nombre,Link_Foto,Puntos_Salud,
Ataque,Defensa,Ataque_Especial,Defensa_Especial,Velocidad,Habilidad_1,
Habilidad_2,Habilidad_Oculta,tipo1,tipo2,ev_Puntos_Salud,ev_Ataque,
ev_Defensa,ev_Ataque_Especial,ev_Defensa_Especial,ev_Velocidad)
VALUES (NULL, 10448, 'Lucario Mega', 'https://raw.githubusercontent.com/Intervencion/PKMNFCbot/master/Sprites/10448.png',
70,145,88,140,70,112,
'Adaptable',' ',' ','Lucha','Acero',
0000000, 0000000, 0000000, 0000000, 0000000, 0000000)
""")

c.execute("""
INSERT INTO POKEMON (idpkmn,Ndex,Nombre,Link_Foto,Puntos_Salud,
Ataque,Defensa,Ataque_Especial,Defensa_Especial,Velocidad,Habilidad_1,
Habilidad_2,Habilidad_Oculta,tipo1,tipo2,ev_Puntos_Salud,ev_Ataque,
ev_Defensa,ev_Ataque_Especial,ev_Defensa_Especial,ev_Velocidad)
VALUES (NULL, 10445, 'Garchomp Mega', 'https://raw.githubusercontent.com/Intervencion/PKMNFCbot/master/Sprites/10445.png',
108,170,115,120,95,92,
'Poder Arena',' ',' ','Dragón','Tierra',
0000000, 0000000, 0000000, 0000000, 0000000, 0000000)
""")

c.execute("""
INSERT INTO POKEMON (idpkmn,Ndex,Nombre,Link_Foto,Puntos_Salud,
Ataque,Defensa,Ataque_Especial,Defensa_Especial,Velocidad,Habilidad_1,
Habilidad_2,Habilidad_Oculta,tipo1,tipo2,ev_Puntos_Salud,ev_Ataque,
ev_Defensa,ev_Ataque_Especial,ev_Defensa_Especial,ev_Velocidad)
VALUES (NULL, 10359, 'Absol Mega', 'https://raw.githubusercontent.com/Intervencion/PKMNFCbot/master/Sprites/10359.png',
65,150,60,115,60,115,
'Espejo Mágico',' ',' ','Siniestro',' ',
0000000, 0000000, 0000000, 0000000, 0000000, 0000000)
""")

c.execute("""
INSERT INTO POKEMON (idpkmn,Ndex,Nombre,Link_Foto,Puntos_Salud,
Ataque,Defensa,Ataque_Especial,Defensa_Especial,Velocidad,Habilidad_1,
Habilidad_2,Habilidad_Oculta,tipo1,tipo2,ev_Puntos_Salud,ev_Ataque,
ev_Defensa,ev_Ataque_Especial,ev_Defensa_Especial,ev_Velocidad)
VALUES (NULL, 10354, 'Banette Mega', 'https://raw.githubusercontent.com/Intervencion/PKMNFCbot/master/Sprites/10354.png',
64,165,75,93,83,75,
'Bromista',' ',' ','Fantasma',' ',
0000000, 0000000, 0000000, 0000000, 0000000, 0000000)
""")

c.execute("""
INSERT INTO POKEMON (idpkmn,Ndex,Nombre,Link_Foto,Puntos_Salud,
Ataque,Defensa,Ataque_Especial,Defensa_Especial,Velocidad,Habilidad_1,
Habilidad_2,Habilidad_Oculta,tipo1,tipo2,ev_Puntos_Salud,ev_Ataque,
ev_Defensa,ev_Ataque_Especial,ev_Defensa_Especial,ev_Velocidad)
VALUES (NULL, 10310, 'Manectric Mega', 'https://raw.githubusercontent.com/Intervencion/PKMNFCbot/master/Sprites/10310.png',
70,75,80,135,80,135,
'Intimidación',' ',' ','Eléctrico',' ',
0000000, 0000000, 0000000, 0000000, 0000000, 0000000)
""")


c.execute("""
INSERT INTO POKEMON (idpkmn,Ndex,Nombre,Link_Foto,Puntos_Salud,
Ataque,Defensa,Ataque_Especial,Defensa_Especial,Velocidad,Habilidad_1,
Habilidad_2,Habilidad_Oculta,tipo1,tipo2,ev_Puntos_Salud,ev_Ataque,
ev_Defensa,ev_Ataque_Especial,ev_Defensa_Especial,ev_Velocidad)
VALUES (NULL, 10308, 'Medicham Mega', 'https://raw.githubusercontent.com/Intervencion/PKMNFCbot/master/Sprites/10308.png',
60,100,85,80,85,100,
'Energía Pura',' ',' ','Lucha','Psíquico',
0000000, 0000000, 0000000, 0000000, 0000000, 0000000)
""")

c.execute("""
INSERT INTO POKEMON (idpkmn,Ndex,Nombre,Link_Foto,Puntos_Salud,
Ataque,Defensa,Ataque_Especial,Defensa_Especial,Velocidad,Habilidad_1,
Habilidad_2,Habilidad_Oculta,tipo1,tipo2,ev_Puntos_Salud,ev_Ataque,
ev_Defensa,ev_Ataque_Especial,ev_Defensa_Especial,ev_Velocidad)
VALUES (NULL, 10306, 'Aggron Mega', 'https://raw.githubusercontent.com/Intervencion/PKMNFCbot/master/Sprites/10306.png',
70,140,230,60,80,50,
'Filtro',' ',' ','Acero',' ',
0000000, 0000000, 0000000, 0000000, 0000000, 0000000)
""")

c.execute("""
INSERT INTO POKEMON (idpkmn,Ndex,Nombre,Link_Foto,Puntos_Salud,
Ataque,Defensa,Ataque_Especial,Defensa_Especial,Velocidad,Habilidad_1,
Habilidad_2,Habilidad_Oculta,tipo1,tipo2,ev_Puntos_Salud,ev_Ataque,
ev_Defensa,ev_Ataque_Especial,ev_Defensa_Especial,ev_Velocidad)
VALUES (NULL, 10303, 'Mawile Mega', 'https://raw.githubusercontent.com/Intervencion/PKMNFCbot/master/Sprites/10303.png',
50,105,125,55,95,50,
'Potencia',' ',' ','Hada','Acero',
0000000, 0000000, 0000000, 0000000, 0000000, 0000000)
""")

c.execute("""
INSERT INTO POKEMON (idpkmn,Ndex,Nombre,Link_Foto,Puntos_Salud,
Ataque,Defensa,Ataque_Especial,Defensa_Especial,Velocidad,Habilidad_1,
Habilidad_2,Habilidad_Oculta,tipo1,tipo2,ev_Puntos_Salud,ev_Ataque,
ev_Defensa,ev_Ataque_Especial,ev_Defensa_Especial,ev_Velocidad)
VALUES (NULL, 10282, 'Gardevoir Mega', 'https://raw.githubusercontent.com/Intervencion/PKMNFCbot/master/Sprites/10282.png',
68,85,65,165,135,100,
'Piel Feérica',' ',' ','Hada','Psíquico',
0000000, 0000000, 0000000, 0000000, 0000000, 0000000)
""")

c.execute("""
INSERT INTO POKEMON (idpkmn,Ndex,Nombre,Link_Foto,Puntos_Salud,
Ataque,Defensa,Ataque_Especial,Defensa_Especial,Velocidad,Habilidad_1,
Habilidad_2,Habilidad_Oculta,tipo1,tipo2,ev_Puntos_Salud,ev_Ataque,
ev_Defensa,ev_Ataque_Especial,ev_Defensa_Especial,ev_Velocidad)
VALUES (NULL, 10257, 'Blaziken Mega', 'https://raw.githubusercontent.com/Intervencion/PKMNFCbot/master/Sprites/10257.png',
80,160,80,130,80,100,
'Impulso',' ',' ','Lucha','Fuego',
0000000, 0000000, 0000000, 0000000, 0000000, 0000000)
""")

c.execute("""
INSERT INTO POKEMON (idpkmn,Ndex,Nombre,Link_Foto,Puntos_Salud,
Ataque,Defensa,Ataque_Especial,Defensa_Especial,Velocidad,Habilidad_1,
Habilidad_2,Habilidad_Oculta,tipo1,tipo2,ev_Puntos_Salud,ev_Ataque,
ev_Defensa,ev_Ataque_Especial,ev_Defensa_Especial,ev_Velocidad)
VALUES (NULL, 10248, 'Tyranitar Mega', 'https://raw.githubusercontent.com/Intervencion/PKMNFCbot/master/Sprites/10248.png',
100,164,150,95,120,71,
'Tormenta Arena',' ',' ','Siniestro','Roca',
0000000, 0000000, 0000000, 0000000, 0000000, 0000000)
""")

c.execute("""
INSERT INTO POKEMON (idpkmn,Ndex,Nombre,Link_Foto,Puntos_Salud,
Ataque,Defensa,Ataque_Especial,Defensa_Especial,Velocidad,Habilidad_1,
Habilidad_2,Habilidad_Oculta,tipo1,tipo2,ev_Puntos_Salud,ev_Ataque,
ev_Defensa,ev_Ataque_Especial,ev_Defensa_Especial,ev_Velocidad)
VALUES (NULL, 10229, 'Houndoom Mega', 'https://raw.githubusercontent.com/Intervencion/PKMNFCbot/master/Sprites/10229.png',
75,90,90,140,90,115,
'Poder Solar',' ',' ','Siniestro','Fuego',
0000000, 0000000, 0000000, 0000000, 0000000, 0000000)
""")

c.execute("""
INSERT INTO POKEMON (idpkmn,Ndex,Nombre,Link_Foto,Puntos_Salud,
Ataque,Defensa,Ataque_Especial,Defensa_Especial,Velocidad,Habilidad_1,
Habilidad_2,Habilidad_Oculta,tipo1,tipo2,ev_Puntos_Salud,ev_Ataque,
ev_Defensa,ev_Ataque_Especial,ev_Defensa_Especial,ev_Velocidad)
VALUES (NULL, 10214, 'Heracross Mega', 'https://raw.githubusercontent.com/Intervencion/PKMNFCbot/master/Sprites/10214.png',
80,185,115,40,105,75,
'Encadenado',' ',' ','Bicho','Lucha',
0000000, 0000000, 0000000, 0000000, 0000000, 0000000)
""")

c.execute("""
INSERT INTO POKEMON (idpkmn,Ndex,Nombre,Link_Foto,Puntos_Salud,
Ataque,Defensa,Ataque_Especial,Defensa_Especial,Velocidad,Habilidad_1,
Habilidad_2,Habilidad_Oculta,tipo1,tipo2,ev_Puntos_Salud,ev_Ataque,
ev_Defensa,ev_Ataque_Especial,ev_Defensa_Especial,ev_Velocidad)
VALUES (NULL, 10212, 'Scizor Mega', 'https://raw.githubusercontent.com/Intervencion/PKMNFCbot/master/Sprites/10212.png',
70,150,140,65,100,75,
'Experto',' ',' ','Bicho','Acero',
0000000, 0000000, 0000000, 0000000, 0000000, 0000000)
""")

c.execute("""
INSERT INTO POKEMON (idpkmn,Ndex,Nombre,Link_Foto,Puntos_Salud,
Ataque,Defensa,Ataque_Especial,Defensa_Especial,Velocidad,Habilidad_1,
Habilidad_2,Habilidad_Oculta,tipo1,tipo2,ev_Puntos_Salud,ev_Ataque,
ev_Defensa,ev_Ataque_Especial,ev_Defensa_Especial,ev_Velocidad)
VALUES (NULL, 10181, 'Ampharos Mega', 'https://raw.githubusercontent.com/Intervencion/PKMNFCbot/master/Sprites/10181.png',
90,95,105,165,110,45,
'Rompemoldes',' ',' ','Dragón','Eléctrico',
0000000, 0000000, 0000000, 0000000, 0000000, 0000000)
""")

c.execute("""
INSERT INTO POKEMON (idpkmn,Ndex,Nombre,Link_Foto,Puntos_Salud,
Ataque,Defensa,Ataque_Especial,Defensa_Especial,Velocidad,Habilidad_1,
Habilidad_2,Habilidad_Oculta,tipo1,tipo2,ev_Puntos_Salud,ev_Ataque,
ev_Defensa,ev_Ataque_Especial,ev_Defensa_Especial,ev_Velocidad)
VALUES (NULL, 10015, 'Beedrill Mega', 'https://raw.githubusercontent.com/Intervencion/PKMNFCbot/master/Sprites/10015.png',
65,150,40,15,80,145,
'Adaptabilidad',' ',' ','Bicho','Veneno',
0000000, 0000000, 0000000, 0000000, 0000000, 0000000)
""")



########################## FORMAS ALTERNATIVAS #########################

c.execute("""
INSERT INTO POKEMON (idpkmn,Ndex,Nombre,Link_Foto,Puntos_Salud,
Ataque,Defensa,Ataque_Especial,Defensa_Especial,Velocidad,Habilidad_1,
Habilidad_2,Habilidad_Oculta,tipo1,tipo2,ev_Puntos_Salud,ev_Ataque,
ev_Defensa,ev_Ataque_Especial,ev_Defensa_Especial,ev_Velocidad)
VALUES (NULL, 10089, 'Muk Alola', 'https://raw.githubusercontent.com/Intervencion/PKMNFCbot/master/Sprites/10089.png',
105,105,75,65,100,50,
'Toque Tóxico','Gula','Reacción Química','Veneno','Siniestro',
0000001, 0000001, 0000000, 0000000, 0000000, 0000000)
""")

c.execute("""
INSERT INTO POKEMON (idpkmn,Ndex,Nombre,Link_Foto,Puntos_Salud,
Ataque,Defensa,Ataque_Especial,Defensa_Especial,Velocidad,Habilidad_1,
Habilidad_2,Habilidad_Oculta,tipo1,tipo2,ev_Puntos_Salud,ev_Ataque,
ev_Defensa,ev_Ataque_Especial,ev_Defensa_Especial,ev_Velocidad)
VALUES (NULL, 10648, 'Meloetta Danza', 'https://raw.githubusercontent.com/Intervencion/PKMNFCbot/master/Sprites/10648.png',
100,128,90,77,77,128,
'Dicha',' ',' ','Lucha','Normal',
0000000, 0000001, 0000001, 0000000, 0000000, 0000001)
""")

c.execute("""
INSERT INTO POKEMON (idpkmn,Ndex,Nombre,Link_Foto,Puntos_Salud,
Ataque,Defensa,Ataque_Especial,Defensa_Especial,Velocidad,Habilidad_1,
Habilidad_2,Habilidad_Oculta,tipo1,tipo2,ev_Puntos_Salud,ev_Ataque,
ev_Defensa,ev_Ataque_Especial,ev_Defensa_Especial,ev_Velocidad)
VALUES (NULL, 11646, 'Kyurem Blanco', 'https://raw.githubusercontent.com/Intervencion/PKMNFCbot/master/Sprites/11646.png',
125,170,100,120,90,95,
'Turbollama',' ',' ','Dragón','Hielo',
0000001, 0000001, 0000000, 0000001, 0000000, 0000000)
""")

c.execute("""
INSERT INTO POKEMON (idpkmn,Ndex,Nombre,Link_Foto,Puntos_Salud,
Ataque,Defensa,Ataque_Especial,Defensa_Especial,Velocidad,Habilidad_1,
Habilidad_2,Habilidad_Oculta,tipo1,tipo2,ev_Puntos_Salud,ev_Ataque,
ev_Defensa,ev_Ataque_Especial,ev_Defensa_Especial,ev_Velocidad)
VALUES (NULL, 10646, 'Kyurem Negro', 'https://raw.githubusercontent.com/Intervencion/PKMNFCbot/master/Sprites/10646.png',
125,170,100,120,90,95,
'Terravoltaje',' ',' ','Dragón','Hielo',
0000001, 0000001, 0000000, 0000001, 0000000, 0000000)
""")

c.execute("""
INSERT INTO POKEMON (idpkmn,Ndex,Nombre,Link_Foto,Puntos_Salud,
Ataque,Defensa,Ataque_Especial,Defensa_Especial,Velocidad,Habilidad_1,
Habilidad_2,Habilidad_Oculta,tipo1,tipo2,ev_Puntos_Salud,ev_Ataque,
ev_Defensa,ev_Ataque_Especial,ev_Defensa_Especial,ev_Velocidad)
VALUES (NULL, 12386, 'Deoxys Velocidad', 'https://raw.githubusercontent.com/Intervencion/PKMNFCbot/master/Sprites/12386.png',
50,95,90,95,90,180,
'Presión',' ',' ','Psçiquico',' ',
0000000, 0000000, 0000000, 0000000, 0000000, 0000003)
""")

c.execute("""
INSERT INTO POKEMON (idpkmn,Ndex,Nombre,Link_Foto,Puntos_Salud,
Ataque,Defensa,Ataque_Especial,Defensa_Especial,Velocidad,Habilidad_1,
Habilidad_2,Habilidad_Oculta,tipo1,tipo2,ev_Puntos_Salud,ev_Ataque,
ev_Defensa,ev_Ataque_Especial,ev_Defensa_Especial,ev_Velocidad)
VALUES (NULL, 11386, 'Deoxys Defensa', 'https://raw.githubusercontent.com/Intervencion/PKMNFCbot/master/Sprites/11386.png',
50,70,160,70,160,90,
'Presión',' ',' ','Psçiquico',' ',
0000000, 0000000, 0000002, 0000000, 0000001, 0000000)
""")

c.execute("""
INSERT INTO POKEMON (idpkmn,Ndex,Nombre,Link_Foto,Puntos_Salud,
Ataque,Defensa,Ataque_Especial,Defensa_Especial,Velocidad,Habilidad_1,
Habilidad_2,Habilidad_Oculta,tipo1,tipo2,ev_Puntos_Salud,ev_Ataque,
ev_Defensa,ev_Ataque_Especial,ev_Defensa_Especial,ev_Velocidad)
VALUES (NULL, 10386, 'Deoxys Ataque', 'https://raw.githubusercontent.com/Intervencion/PKMNFCbot/master/Sprites/10386.png',
50,180,20,180,20,150,
'Presión',' ',' ','Psçiquico',' ',
0000000, 0000002, 0000000, 0000001, 0000000, 0000000)
""")

c.execute("""
INSERT INTO POKEMON (idpkmn,Ndex,Nombre,Link_Foto,Puntos_Salud,
Ataque,Defensa,Ataque_Especial,Defensa_Especial,Velocidad,Habilidad_1,
Habilidad_2,Habilidad_Oculta,tipo1,tipo2,ev_Puntos_Salud,ev_Ataque,
ev_Defensa,ev_Ataque_Especial,ev_Defensa_Especial,ev_Velocidad)
VALUES (NULL, 11413, 'Wormadan Basura', 'https://raw.githubusercontent.com/Intervencion/PKMNFCbot/master/Sprites/11413.png',
60,69,95,69,95,36,
'Anticipación',' ','Funda','Bicho','Acero',
0000000, 0000000, 0000001, 0000000, 0000001, 0000000)
""")

c.execute("""
INSERT INTO POKEMON (idpkmn,Ndex,Nombre,Link_Foto,Puntos_Salud,
Ataque,Defensa,Ataque_Especial,Defensa_Especial,Velocidad,Habilidad_1,
Habilidad_2,Habilidad_Oculta,tipo1,tipo2,ev_Puntos_Salud,ev_Ataque,
ev_Defensa,ev_Ataque_Especial,ev_Defensa_Especial,ev_Velocidad)
VALUES (NULL, 10413, 'Wormadan Arena', 'https://raw.githubusercontent.com/Intervencion/PKMNFCbot/master/Sprites/10413.png',
60,79,105,59,85,36,
'Anticipación',' ','Funda','Bicho','Tierra',
0000000, 0000000, 0000002, 0000000, 0000000, 0000000)
""")

c.execute("""
INSERT INTO POKEMON (idpkmn,Ndex,Nombre,Link_Foto,Puntos_Salud,
Ataque,Defensa,Ataque_Especial,Defensa_Especial,Velocidad,Habilidad_1,
Habilidad_2,Habilidad_Oculta,tipo1,tipo2,ev_Puntos_Salud,ev_Ataque,
ev_Defensa,ev_Ataque_Especial,ev_Defensa_Especial,ev_Velocidad)
VALUES (NULL, 10555, 'Darmanitan Durama', 'https://raw.githubusercontent.com/Intervencion/PKMNFCbot/master/Sprites/10555.png',
105,30,105,140,105,55,
'Modo durama',' ',' ','Fuego','Psíquico',
0000000, 0000000, 0000000, 0000002, 0000000, 0000000)
""")

c.execute("""
INSERT INTO POKEMON (idpkmn,Ndex,Nombre,Link_Foto,Puntos_Salud,
Ataque,Defensa,Ataque_Especial,Defensa_Especial,Velocidad,Habilidad_1,
Habilidad_2,Habilidad_Oculta,tipo1,tipo2,ev_Puntos_Salud,ev_Ataque,
ev_Defensa,ev_Ataque_Especial,ev_Defensa_Especial,ev_Velocidad)
VALUES (NULL, 10487, 'Giratina Origen', 'https://raw.githubusercontent.com/Intervencion/PKMNFCbot/master/Sprites/10487.png',
150,120,100,120,100,90,
'Levitación',' ',' ','Dragón','Fantasma',
0000003, 0000000, 0000000, 0000000, 0000000, 0000000)
""")

c.execute("""
INSERT INTO POKEMON (idpkmn,Ndex,Nombre,Link_Foto,Puntos_Salud,
Ataque,Defensa,Ataque_Especial,Defensa_Especial,Velocidad,Habilidad_1,
Habilidad_2,Habilidad_Oculta,tipo1,tipo2,ev_Puntos_Salud,ev_Ataque,
ev_Defensa,ev_Ataque_Especial,ev_Defensa_Especial,ev_Velocidad)
VALUES (NULL, 10492, 'Shaymin Cielo', 'https://raw.githubusercontent.com/Intervencion/PKMNFCbot/master/Sprites/10492.png',
100,103,75,120,75,127,
'Dicha',' ',' ','Planta','Volador',
0000003, 0000000, 0000000, 0000000, 0000000, 0000000)
""")

c.execute("""
INSERT INTO POKEMON (idpkmn,Ndex,Nombre,Link_Foto,Puntos_Salud,
Ataque,Defensa,Ataque_Especial,Defensa_Especial,Velocidad,Habilidad_1,
Habilidad_2,Habilidad_Oculta,tipo1,tipo2,ev_Puntos_Salud,ev_Ataque,
ev_Defensa,ev_Ataque_Especial,ev_Defensa_Especial,ev_Velocidad)
VALUES (NULL, 14479, 'Rotom Lavado', 'https://raw.githubusercontent.com/Intervencion/PKMNFCbot/master/Sprites/14479.png',
50,65,107,105,107,86,
'Levitate',' ',' ','Eléctrico','Agua',
0000000, 0000000, 0000000, 0000001, 0000000, 0000001)
""")

c.execute("""
INSERT INTO POKEMON (idpkmn,Ndex,Nombre,Link_Foto,Puntos_Salud,
Ataque,Defensa,Ataque_Especial,Defensa_Especial,Velocidad,Habilidad_1,
Habilidad_2,Habilidad_Oculta,tipo1,tipo2,ev_Puntos_Salud,ev_Ataque,
ev_Defensa,ev_Ataque_Especial,ev_Defensa_Especial,ev_Velocidad)
VALUES (NULL, 13479, 'Rotom Corte', 'https://raw.githubusercontent.com/Intervencion/PKMNFCbot/master/Sprites/13479.png',
50,65,107,105,107,86,
'Levitate',' ',' ','Eléctrico','Planta',
0000000, 0000000, 0000000, 0000001, 0000000, 0000001)
""")

c.execute("""
INSERT INTO POKEMON (idpkmn,Ndex,Nombre,Link_Foto,Puntos_Salud,
Ataque,Defensa,Ataque_Especial,Defensa_Especial,Velocidad,Habilidad_1,
Habilidad_2,Habilidad_Oculta,tipo1,tipo2,ev_Puntos_Salud,ev_Ataque,
ev_Defensa,ev_Ataque_Especial,ev_Defensa_Especial,ev_Velocidad)
VALUES (NULL, 12479, 'Rotom Calor', 'https://raw.githubusercontent.com/Intervencion/PKMNFCbot/master/Sprites/12479.png',
50,65,107,105,107,86,
'Levitate',' ',' ','Eléctrico','Fuego',
0000000, 0000000, 0000000, 0000001, 0000000, 0000001)
""")

c.execute("""
INSERT INTO POKEMON (idpkmn,Ndex,Nombre,Link_Foto,Puntos_Salud,
Ataque,Defensa,Ataque_Especial,Defensa_Especial,Velocidad,Habilidad_1,
Habilidad_2,Habilidad_Oculta,tipo1,tipo2,ev_Puntos_Salud,ev_Ataque,
ev_Defensa,ev_Ataque_Especial,ev_Defensa_Especial,ev_Velocidad)
VALUES (NULL, 11479, 'Rotom Frío', 'https://raw.githubusercontent.com/Intervencion/PKMNFCbot/master/Sprites/11479.png',
50,65,107,105,107,86,
'Levitate',' ',' ','Eléctrico','Hielo',
0000000, 0000000, 0000000, 0000001, 0000000, 0000001)
""")

c.execute("""
INSERT INTO POKEMON (idpkmn,Ndex,Nombre,Link_Foto,Puntos_Salud,
Ataque,Defensa,Ataque_Especial,Defensa_Especial,Velocidad,Habilidad_1,
Habilidad_2,Habilidad_Oculta,tipo1,tipo2,ev_Puntos_Salud,ev_Ataque,
ev_Defensa,ev_Ataque_Especial,ev_Defensa_Especial,ev_Velocidad)
VALUES (NULL, 10479, 'Rotom Ventilador', 'https://raw.githubusercontent.com/Intervencion/PKMNFCbot/master/Sprites/10479.png',
50,65,107,105,107,86,
'Levitate',' ',' ','Eléctrico','Volador',
0000000, 0000000, 0000000, 0000001, 0000000, 0000001)
""")

c.execute("""
INSERT INTO POKEMON (idpkmn,Ndex,Nombre,Link_Foto,Puntos_Salud,
Ataque,Defensa,Ataque_Especial,Defensa_Especial,Velocidad,Habilidad_1,
Habilidad_2,Habilidad_Oculta,tipo1,tipo2,ev_Puntos_Salud,ev_Ataque,
ev_Defensa,ev_Ataque_Especial,ev_Defensa_Especial,ev_Velocidad)
VALUES (NULL, 10658, 'Greninja Ash', 'https://raw.githubusercontent.com/Intervencion/PKMNFCbot/master/Sprites/10681.png',
72,145,67,153,71,132,
'Fuerte Afecto',' ',' ','Siniestro','Agua',
0000000, 0000000, 0000000, 0000000, 0000000, 0000003)
""")

c.execute("""
INSERT INTO POKEMON (idpkmn,Ndex,Nombre,Link_Foto,Puntos_Salud,
Ataque,Defensa,Ataque_Especial,Defensa_Especial,Velocidad,Habilidad_1,
Habilidad_2,Habilidad_Oculta,tipo1,tipo2,ev_Puntos_Salud,ev_Ataque,
ev_Defensa,ev_Ataque_Especial,ev_Defensa_Especial,ev_Velocidad)
VALUES (NULL, 10681, 'Aegislash Filo', 'https://raw.githubusercontent.com/Intervencion/PKMNFCbot/master/Sprites/10681.png',
60,150,50,150,50,60,
'Cambio Táctico',' ',' ','Fantasma','Acero',
0000000, 0000003, 0000000, 0000000, 0000000, 0000000)
""")

c.execute("""
INSERT INTO POKEMON (idpkmn,Ndex,Nombre,Link_Foto,Puntos_Salud,
Ataque,Defensa,Ataque_Especial,Defensa_Especial,Velocidad,Habilidad_1,
Habilidad_2,Habilidad_Oculta,tipo1,tipo2,ev_Puntos_Salud,ev_Ataque,
ev_Defensa,ev_Ataque_Especial,ev_Defensa_Especial,ev_Velocidad)
VALUES (NULL, 10641, 'Tornadus Totem', 'https://raw.githubusercontent.com/Intervencion/PKMNFCbot/master/Sprites/10641.png',
79,100,80,110,90,121,
'Regeneración',' ',' ','Volador',' ',
0000003, 0000000, 0000000, 0000000, 0000000, 0000000)
""")

c.execute("""
INSERT INTO POKEMON (idpkmn,Ndex,Nombre,Link_Foto,Puntos_Salud,
Ataque,Defensa,Ataque_Especial,Defensa_Especial,Velocidad,Habilidad_1,
Habilidad_2,Habilidad_Oculta,tipo1,tipo2,ev_Puntos_Salud,ev_Ataque,
ev_Defensa,ev_Ataque_Especial,ev_Defensa_Especial,ev_Velocidad)
VALUES (NULL, 10642, 'Thundurus Totem', 'https://raw.githubusercontent.com/Intervencion/PKMNFCbot/master/Sprites/10642.png',
79,105,70,145,80,101,
'Ambsorbe Electricidad',' ',' ','Eléctrico','Volador',
0000000, 0000003, 0000000, 0000000, 0000000, 0000000)
""")

c.execute("""
INSERT INTO POKEMON (idpkmn,Ndex,Nombre,Link_Foto,Puntos_Salud,
Ataque,Defensa,Ataque_Especial,Defensa_Especial,Velocidad,Habilidad_1,
Habilidad_2,Habilidad_Oculta,tipo1,tipo2,ev_Puntos_Salud,ev_Ataque,
ev_Defensa,ev_Ataque_Especial,ev_Defensa_Especial,ev_Velocidad)
VALUES (NULL, 10645, 'Landorus Totem', 'https://raw.githubusercontent.com/Intervencion/PKMNFCbot/master/Sprites/10645.png',
89,145,90,105,80,91,
'Intimidación',' ',' ','Tierra','Volador',
0000000, 0000000, 0000000, 0000003, 0000000, 0000000)
""")


########################## FORMAS ALTERNATIVAS  FIN #########################

c.execute("""
INSERT INTO POKEMON (idpkmn,Ndex,Nombre,Link_Foto,Puntos_Salud,
Ataque,Defensa,Ataque_Especial,Defensa_Especial,Velocidad,Habilidad_1,
Habilidad_2,Habilidad_Oculta,tipo1,tipo2,ev_Puntos_Salud,ev_Ataque,
ev_Defensa,ev_Ataque_Especial,ev_Defensa_Especial,ev_Velocidad)
VALUES (NULL, 10142, 'Aerodactyl Mega', 'https://raw.githubusercontent.com/Intervencion/PKMNFCbot/master/Sprites/10142.png',
80,135,85,70,95,150,
'Garra Dura',' ',' ','Roca','Volador',
0000000, 0000000, 0000000, 0000000, 0000000, 0000000)
""")

c.execute("""
INSERT INTO POKEMON (idpkmn,Ndex,Nombre,Link_Foto,Puntos_Salud,
Ataque,Defensa,Ataque_Especial,Defensa_Especial,Velocidad,Habilidad_1,
Habilidad_2,Habilidad_Oculta,tipo1,tipo2,ev_Puntos_Salud,ev_Ataque,
ev_Defensa,ev_Ataque_Especial,ev_Defensa_Especial,ev_Velocidad)
VALUES (NULL, 10130, 'Gyarados Mega', 'https://raw.githubusercontent.com/Intervencion/PKMNFCbot/master/Sprites/10130.png',
95,155,109,70,130,81,
'Rompemoldes',' ',' ','Agua','Siniestro',
0000000, 0000000, 0000000, 0000000, 0000000, 0000000)
""")

c.execute("""
INSERT INTO POKEMON (idpkmn,Ndex,Nombre,Link_Foto,Puntos_Salud,
Ataque,Defensa,Ataque_Especial,Defensa_Especial,Velocidad,Habilidad_1,
Habilidad_2,Habilidad_Oculta,tipo1,tipo2,ev_Puntos_Salud,ev_Ataque,
ev_Defensa,ev_Ataque_Especial,ev_Defensa_Especial,ev_Velocidad)
VALUES (NULL, 10127, 'Pinsir Mega', 'https://raw.githubusercontent.com/Intervencion/PKMNFCbot/master/Sprites/10127.png',
65,155,120,65,90,105,
'Piel Celeste',' ',' ','Bicho','Volador',
0000000, 0000000, 0000000, 0000000, 0000000, 0000000)
""")

c.execute("""
INSERT INTO POKEMON (idpkmn,Ndex,Nombre,Link_Foto,Puntos_Salud,
Ataque,Defensa,Ataque_Especial,Defensa_Especial,Velocidad,Habilidad_1,
Habilidad_2,Habilidad_Oculta,tipo1,tipo2,ev_Puntos_Salud,ev_Ataque,
ev_Defensa,ev_Ataque_Especial,ev_Defensa_Especial,ev_Velocidad)
VALUES (NULL, 10115, 'Kangaskhan Mega', 'https://raw.githubusercontent.com/Intervencion/PKMNFCbot/master/Sprites/10115.png',
105,125,100,60,100,100,
'Amor Filial',' ',' ','Normal',' ',
0000000, 0000000, 0000000, 0000000, 0000000, 0000000)
""")

c.execute("""
INSERT INTO POKEMON (idpkmn,Ndex,Nombre,Link_Foto,Puntos_Salud,
Ataque,Defensa,Ataque_Especial,Defensa_Especial,Velocidad,Habilidad_1,
Habilidad_2,Habilidad_Oculta,tipo1,tipo2,ev_Puntos_Salud,ev_Ataque,
ev_Defensa,ev_Ataque_Especial,ev_Defensa_Especial,ev_Velocidad)
VALUES (NULL, 10094, 'Gengar Mega', 'https://raw.githubusercontent.com/Intervencion/PKMNFCbot/master/Sprites/10094.png',
60,65,80,170,95,130,
'Sombra Trampa',' ',' ','Fantasma','Veneno',
0000000, 0000000, 0000000, 0000000, 0000000, 0000000)
""")

c.execute("""
INSERT INTO POKEMON (idpkmn,Ndex,Nombre,Link_Foto,Puntos_Salud,
Ataque,Defensa,Ataque_Especial,Defensa_Especial,Velocidad,Habilidad_1,
Habilidad_2,Habilidad_Oculta,tipo1,tipo2,ev_Puntos_Salud,ev_Ataque,
ev_Defensa,ev_Ataque_Especial,ev_Defensa_Especial,ev_Velocidad)
VALUES (NULL, 10065, 'Alakazam Mega', 'https://raw.githubusercontent.com/Intervencion/PKMNFCbot/master/Sprites/10065.png',
55,50,65,175,95,150,
'Rastro',' ',' ','Psíquico',' ',
0000000, 0000000, 0000000, 0000000, 0000000, 0000000)
""")

c.execute("""
INSERT INTO POKEMON (idpkmn,Ndex,Nombre,Link_Foto,Puntos_Salud,
Ataque,Defensa,Ataque_Especial,Defensa_Especial,Velocidad,Habilidad_1,
Habilidad_2,Habilidad_Oculta,tipo1,tipo2,ev_Puntos_Salud,ev_Ataque,
ev_Defensa,ev_Ataque_Especial,ev_Defensa_Especial,ev_Velocidad)
VALUES (NULL, 11006, 'Charizard Mega Y', 'https://raw.githubusercontent.com/Intervencion/PKMNFCbot/master/Sprites/11006.png',
78,104,78,159,115,100,
'Sequía',' ',' ','Fuego','Volador',
0000000, 0000000, 0000000, 0000000, 0000000, 0000000)
""")

c.execute("""
INSERT INTO POKEMON (idpkmn,Ndex,Nombre,Link_Foto,Puntos_Salud,
Ataque,Defensa,Ataque_Especial,Defensa_Especial,Velocidad,Habilidad_1,
Habilidad_2,Habilidad_Oculta,tipo1,tipo2,ev_Puntos_Salud,ev_Ataque,
ev_Defensa,ev_Ataque_Especial,ev_Defensa_Especial,ev_Velocidad)
VALUES (NULL, 10006, 'Charizard Mega X', 'https://raw.githubusercontent.com/Intervencion/PKMNFCbot/master/Sprites/10006.png',
78,130,111,130,85,100,
'Garra Dura',' ',' ','Fuego','Dragón',
0000000, 0000000, 0000000, 0000000, 0000000, 0000000)
""")

c.execute("""
INSERT INTO POKEMON (idpkmn,Ndex,Nombre,Link_Foto,Puntos_Salud,
Ataque,Defensa,Ataque_Especial,Defensa_Especial,Velocidad,Habilidad_1,
Habilidad_2,Habilidad_Oculta,tipo1,tipo2,ev_Puntos_Salud,ev_Ataque,
ev_Defensa,ev_Ataque_Especial,ev_Defensa_Especial,ev_Velocidad)
VALUES (NULL, 10003, 'Venusaur Mega', 'https://raw.githubusercontent.com/Intervencion/PKMNFCbot/master/Sprites/10003.png',
80,100,123,122,120,80,
'Sebo',' ',' ','Planta','Veneno',
0000000, 0000000, 0000000, 0000000, 0000000, 0000000)
""")

c.execute("""
INSERT INTO POKEMON (idpkmn,Ndex,Nombre,Link_Foto,Puntos_Salud,
Ataque,Defensa,Ataque_Especial,Defensa_Especial,Velocidad,Habilidad_1,
Habilidad_2,Habilidad_Oculta,tipo1,tipo2,ev_Puntos_Salud,ev_Ataque,
ev_Defensa,ev_Ataque_Especial,ev_Defensa_Especial,ev_Velocidad)
VALUES (NULL, 10009, 'Blastoise Mega', 'https://raw.githubusercontent.com/Intervencion/PKMNFCbot/master/Sprites/10009.png',
80,103, 120, 135, 115, 80,
'Megadisparador', ' ' , ' ', 'Agua', ' ',
0000000, 0000000, 0000000, 0000000, 0000000, 0000000)
""")