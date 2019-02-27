from config import *
from mysql_connector import *

def pintar_tipo(tipo):
	etipo=""
	if(tipo == "Acero"):
		etipo = "  ⚙"
	elif(tipo == "Agua"):
		etipo = "   💦"
	elif(tipo == "Bicho"):
		etipo = "  🐛"
	elif(tipo == "Dragón"):
		etipo = "  🐉"
	elif(tipo == "Eléctrico"):
		etipo = "⚡️"
	elif(tipo == "Fantasma"):
		etipo = " 👻"
	elif(tipo == "Fuego"):
		etipo = "  🔥"
	elif(tipo == "Hada"):
		etipo = "   🎀"
	elif(tipo == "Hielo"):
		etipo = "  ❄️"
	elif(tipo == "Lucha"):
		etipo = "  💪"
	elif(tipo == "Normal"):
		etipo = "  🐕"
	elif(tipo == "Planta"):
		etipo = "  🍃"
	elif(tipo == "Psíquico"):
		etipo = " 🔮"
	elif(tipo == "Roca"):
		etipo = "   🗿"
	elif(tipo == "Siniestro"):
		etipo = "👤"
	elif(tipo == "Tierra"):
		etipo = "  🌎"
	elif(tipo == "Veneno"):
		etipo = "  🍄"
	elif(tipo == "Volador"):
		etipo = " 🌪"

	return etipo


def pintar_stats(hp, atk, defe, atksp, defsp, spd):
	
	if hp<=60:
		cbhp = "📕"
	elif (hp>60 and hp<=80):
		cbhp = "📙"
	elif (hp>80 and hp<=100):
		cbhp = "📒"
	elif hp>100:
		cbhp = "📗"
		
	if atk<=60:
		cbatk = "📕"
	elif (atk>60 and atk<=80):
		cbatk = "📙"
	elif (atk>80 and atk<=100):
		cbatk = "📒"

	elif atk>100:
		cbatk = "📗"

	if defe<=60:
		cbdefe = "📕"
	elif (defe>60 and defe<=80):
		cbdefe = "📙"
	elif (defe>80 and defe<=100):
		cbdefe = "📒"
	elif defe>100:
		cbdefe = "📗"

	if atksp<=60:
		cbatksp = "📕"
	elif (atksp>60 and atksp<=80):
		cbatksp = "📙"
	elif (atksp>80 and atksp<=100):
		cbatksp = "📒"
	elif atksp>100:
		cbatksp = "📗"
		
	if defsp<=60:
		cbdefsp = "📕"
	elif (defsp>60 and defsp<=80):
		cbdefsp = "📙"
	elif (defsp>80 and defsp<=100):
		cbdefsp = "📒"
	elif defsp>100:
		cbdefsp = "📗"
		
	if spd<=60:
		cbspd = "📕"
	elif (spd>60 and spd<=80):
		cbspd = "📙"
	elif (spd>80 and spd<=100):
		cbspd = "📒"
	elif spd>100:
		cbspd = "📗"
			
	return cbhp, cbatk, cbdefe, cbatksp, cbdefsp, cbspd

tipos = {
	"steel":"Acero",
	"water":"Agua",
	"bug":"Bicho",
	"dragon":"Dragón",
	"electric":"Eléctrico",
	"ghost":"Fantasma",
	"fire":"Fuego",
	"fairy":"Hada",
	"ice":"Hielo",
	"fighting":"Lucha",
	"normal":"Normal",
	"grass":"Planta",
	"psychic":"Psíquico",
	"rock":"Roca",
	"dark":"Siniestro",
	"ground":"Tierra",
	"poison":"Veneno",
	"flying":"Volador"
}

#cursor.execute("SELECT Ndex,Nombre,Linkfoto,hp,atk,defe,atksp,defsp,spd,hab1,hab2,habo,tipo1,tipo2,evhp,evatk,evdefe,evatksp,evdefsp,evspd from POKEMON WHERE Nombre='" + str(pkmn)+ "'"))

def poke_normal(pkmn):
	print("1) entro en la función de poke normal")
	print(pkmn)
	print("2) El poke con mayus es " + pkmn.capitalize())
	#c.execute("SELECT Ndex,Nombre,Linkfoto,hp,atk,defe,atksp,defsp,spd,hab1,hab2,habo,tipo1,tipo2,evhp,evatk,evdefe,evatksp,evdefsp,evspd from POKEMON WHERE Nombre='" + str(pkmn)+ "'")
	try:
		c.execute("SELECT Ndex,Nombre,Linkfoto,hp,atk,defe,atksp,defsp,spd,hab1,hab2,habo,tipo1,tipo2,evhp,evatk,evdefe,evatksp,evdefsp,evspd from pokemon WHERE Nombre='" + str(pkmn)+ "'")
	except Exception as e:
		print(e)
	print("Voy despues del cursor 'c'")
	for i in c:
		dex = i[0]
		name = i[1]
		imgpkm = i[2]
		hp = i[3]
		atk = i[4]
		defe = i[5]
		atksp = i[6]
		defsp = i[7]
		spd = i[8]
		hab1 = i[9]
		hab2 = i[10]
		habo = i[11]
		tipo1 = i[12]
		tipo2 = i[13]
		evhp = i[14]
		evatk = i[15]
		evdefe = i[16]
		evatksp = i[17]
		evdefsp = i[18]
		evspd = i[19]
	print(dex, name,imgpkm, hp, atk, defe, atksp, defsp, spd, hab1, hab2, habo, tipo1, tipo2, evhp, evatk, evdefe, evatksp, evdefsp, evspd)
	return dex, name,imgpkm, hp, atk, defe, atksp, defsp, spd, hab1, hab2, habo, tipo1, tipo2, evhp, evatk, evdefe, evatksp, evdefsp, evspd


#############################################################################
#########################FUNCION PRINCIPAL DE STATS #########################
############################################################################

@bot.message_handler(func=lambda m: m.text and (m.text.startswith("!stats") or m.text.startswith("/stats")))
def command_stats(m):
#	global dex
	cid = m.chat.id
	pkmn = m.text.lower().split(' ', 1)[1].capitalize()
	print("3) AHORA TE PONGO EL POKE CAPITALISAO")
	print("4) " + pkmn)
	dex = 0
#	print(dex)
	name = ""
	imgpkm = ""
	hp = 0
	atk = 0
	defe = 0
	atksp = 0
	defsp = 0
	spd = 0
	hab1 = ""
	hab2 = ""
	habo = ""
	tipo1 = ""
	tipo2 = ""
	evhp = 0
	evatk = 0
	evdefe = 0
	evatksp = 0
	evdefsp =0
	evspd = 0
	cbhp = ""
	cbatk = ""
	cbdefe = ""
	cbatksp = ""
	cbdefsp = ""
	cbspd = ""
	etipo= ""
	habilidades= ""
	sname = ""
	flagr = 0


	markup = types.InlineKeyboardMarkup()
	markup.add(types.InlineKeyboardButton("En desarollo", callback_data = "pkmn"))
	bot.send_chat_action(cid, "typing")
	nomega = ["venusaur", "blastoise", "charizard", "alakazam", "gengar", "kaangaskhan", "pinsir", "gyarados", "aerodactyl", "mewtwo", "ampharos", "scizor", "heracross", "houndoom", "tyranitar", "blaziken", "gardevoir", "mawile", "aggron", "medichamp", "manectric", "banette", "absol", "garchomp", "lucario", "pidgeot", "sharpedo", "salamance", "abomasnow", "beedrill", "slowbro", "steelix", "sceptile", "swampert", "sableye", "camerut", "altaria", "glalie", "metagross", "latios", "latias", "rayquaza", "lopunny", "gallade", "audino", "diancie"]
	alolaform = ["Rattata", "Raticate", "Raichu", "Sandshrew", "Sandslash", "Vulpix", "Ninetales", "Diglett", "Dugtrio", "Meowth", "Persian", "Geodude", "Graveler", "Golem", "Grimer", "Muk", "Exeggutor", "Marowak"]


	try:
		if (m.text.lower().split(' ', 2)[2] == "mega"):
			npkmn = m.text.lower().split(' ', 2)[1]
			if(npkmn in nomega):
				print("5) Sé que pone mega y además tiene mega")
				bot.reply_to(m, "Las megas estarán pronto, ¡lo siento!", reply_markup=markup, parse_mode="Markdown")
				flagr = 1
			else:
				print("6) Sé que pone mega y este poke no tiene mega")
				bot.reply_to(m, "Este poke no tiene mega, pedazo troll", reply_markup=markup, parse_mode="Markdown")
				flagr =1
	except:
		print("7) NO HABIA SEGUNDA PALABRA EN MEGA")

	try:
		print("8) Voy a mirar si pone alola")
		if(m.text.lower().split(' ', 2)[2] == "alola"):
			npkmn = m.text.split(' ', 2)[1]
			npkmn = npkmn.capitalize()
			sppkmn = m.text.split(' ', 2)[2]
			sppkmn = sppkmn.capitalize()
			print(npkmn)
			if(npkmn in alolaform):
				print("9) Sé que pone alola y además tiene forma alola")
				npkmn = npkmn + " " + sppkmn
				dex, name,imgpkm, hp, atk, defe, atksp, defsp, spd, hab1, hab2, habo, tipo1, tipo2, evhp, evatk, evdefe, evatksp, evdefsp, evspd = poke_normal(npkmn)
				#dex = dex -10000
				t = hp + atk + defe + atksp + defsp + spd
				cbhp, cbatk, cbdefe, cbatksp, cbdefsp, cbspd = pintar_stats(hp, atk, defe, atksp, defsp, spd)
				etipo1 = pintar_tipo(tipo1)
#				etipo1 = etipo
				etipo2 = pintar_tipo(tipo2)
#				etipo2 = etipo
				print("Es de alola, pero... ¿Tiene habilidad 2?: " + hab2)
				if (((hab2 == " ") or (hab2 == "No tiene")) and ((habo == " ") or (habo == "No tiene"))):
					habilidades = "`Habilidad` " + str(hab1)
				elif ((habo == " ") or (habo == "No tiene")):
					habilidades = "`Habilidad 1` " + str(hab1) + "\n`Habilidad 2` " + str(hab2)
				elif ((hab2 == " ") or (hab2 == "No tiene")):
					habilidades = "`Habilidad 1` " + str(hab1) + "\n`Hab. Oculta` " + str(habo)
				else:
					habilidades = "`Habilidad 1` " + str(hab1) + "\n`Habilidad 2` " + str(hab2) + "\n`Hab. Oculta` " + str(habo)

				if (tipo2 is not " "):
					tipos = "`" + tipo1 + etipo1 + "`\n" + "`" + tipo2 + etipo2 + "`"
				else:
					tipos = tipo1 + etipo1

				if ")" in imgpkm:
					imgpkm = imgpkm
				else:
					imgpkm = imgpkm + ")"

				if "Código cero" in name:
					sname = "type\_null"
				elif "Lycanroc nocturno" in name:
					sname = "lycanroc-midnight"
				elif "Wishiwashi forma individual" in name:
					sname = "wishiwashi"
				elif "Minior forma meteorito" in name:
					sname = "minior"
				elif "Minior forma núcleo" in name:
					sname = "minior"
				elif " " in name:
					sname = name.replace(" ", "_")
				else:
					sname = name
				
				print("Alola dex")
				if dex > 9999: dex %= 1000
				print(dex)
				
			#	if len(dex) == 5:
			#		dex = dex[2:]
			#	else:
			#		dex = dex

#				bot.reply_to(m,
#				"_#" + dex + "_ - " + "*" + name + "*\n" + tipos + "\n\n`PS`: " + str(cbhp) + str(hp) +
#				"\n`Ataque` " + str(cbatk) + str(atk) + "\n`Defensa` " + str(cbdefe)+ str(defe) + "\n`Atk. Esp.` " + str(cbatksp) + str(atksp) +
#				"\n`Def. Esp.` " + str(cbdefsp) + str(defsp) + "\n`Velocidad` " + str(cbspd) + str(spd) + "\n`Total` " + str(t) +
#				"\n\n" + habilidades + "\n" + "[⁣](" + imgpkm
#				+ "\n["+name+ " en Smogon](http://www.smogon.com/dex/sm/pokemon/" + sname + ")", parse_mode = "Markdown")




################{}.format -> f"{a}"############################"



#				bot.reply_to(m, f"_# {dex}_ - *{name}*\n{tipos}\n\n`PS`: str(cbhp}{hp}\n`Ataque`: {cbatk}{atk}\n`Defensa`: {cbdefe}{defe}\n`Atk. Esp.`: {cbatksp}{atksp}\n`Def. Esp.`: {cbdefsp}{defsp}\n`Velocidad`: {cbspd}{spd}\n`Total`: {t}\n\n{habilidades}\n[⁣]({imgpkm}\n[{name} en Smogon](http://www.smogon.com/dex/sm/pokemon/{sname})", parse_mode = "Markdown")
#				bot.reply_to(m, """
#				_# {dex}_ - *{name}*\n{tipos}\n\n`PS`: {cbhp}{hp}
#				\n`Ataque`: {cbatk}{atk}\n`Defensa`: {cbdefe}{defe}\n`Atk. Esp.`: {cbatksp}{atksp}
#				\n`Def. Esp.`: {cbdefsp}{defsp}\n`Velocidad`: {cbspd}{spd}\n`Total`: {t}
#				\n\n{habilidades}\n[⁣]({imgpkm}
#				\n[{name} en Smogon](http://www.smogon.com/dex/sm/pokemon/{sname})"""
#				.format(dex, name, tipos, cbhp, hp, cbatk, atk, cbdef, defe, cbatksp, atksp, cbdefsp, defsp, cbspd, spd, t, habilidades, imgpkmn, sname), parse_mode = "Markdown")


				ficha = "_# {0}_ - *{1}*\n{2}\n\n`PS:` {3}{4}\n`Ataque:` {5}{6}\n`Defensa:` {7}{8}\n`Atk. Esp.:` {9}{10}\n`Def. Esp.:` {11}{12}\n`Velocidad:` {13}{14}\n`Total:` {15}\n\n{16}\n[⁣]({17}\n[{1} en Smogon](http://www.smogon.com/dex/sm/pokemon/{18})"
				bot.reply_to(m, ficha.format(dex, name, tipos, cbhp, hp, cbatk, atk, cbdefe, defe, cbatksp, atksp, cbdefsp, defsp, cbspd, spd, t, habilidades, imgpkm, sname), parse_mode = "Markdown")

				#print("L318. Parece que L319 peta al ser dex un INT")
				#print("_#" + dex + "_ - " + "*" + name + "*\n" + tipos + "\n\n`PS`: " + str(cbhp) + str(hp) +"\n`Ataque` " + str(cbatk) + str(atk) + "\n`Defensa` " + str(cbdefe)+ str(defe) + "\n`Atk. Esp.` " + str(cbatksp) + str(atksp) + "\n`Def. Esp.` " + str(cbdefsp) + str(defsp) + "\n`Velocidad` " + str(cbspd) + str(spd) + "\n`Total` " + str(t) + "\n\n" + habilidades + "\n" + "[⁣](" + imgpkm + "\n\n["+name+ " en Smogon](http://www.smogon.com/dex/sm/pokemon/" + name + ")")
				print("L320. Estoy aquí porque estoy comprobando si dex necesita ser pasado a str en el print o no.")
				print("_#" + str(dex) + "_ - " + "*" + name + "*\n" + tipos + "\n\n`PS`: " + str(cbhp) + str(hp) +"\n`Ataque` " + str(cbatk) + str(atk) + "\n`Defensa` " + str(cbdefe)+ str(defe) + "\n`Atk. Esp.` " + str(cbatksp) + str(atksp) + "\n`Def. Esp.` " + str(cbdefsp) + str(defsp) + "\n`Velocidad` " + str(cbspd) + str(spd) + "\n`Total` " + str(t) + "\n\n" + habilidades + "\n" + "[⁣](" + imgpkm + "\n\n["+name+ " en Smogon](http://www.smogon.com/dex/sm/pokemon/" + name + ")")

				flagr = 2
			else:
				print("11) Sé que pone alola y este poke no tiene forma alola")
				bot.reply_to(m, "Este poke no tiene forma alola, pedazo troll", reply_markup=markup, parse_mode="Markdown")
				flagr = 2

	except:
		print("12) NO HABIA SEGUNDA PALABRA EN ALOLA")
	try:
		if(flagr == 0):
			print("13) No pone mega ni pone alola")
		#		sppkmn = m.text.split(' ', 2)[2]
		#		sppkmn = sppkmn.capitalize()
			dex, name,imgpkm, hp, atk, defe, atksp, defsp, spd, hab1, hab2, habo, tipo1, tipo2, evhp, evatk, evdefe, evatksp, evdefsp, evspd = poke_normal(pkmn)
			t = hp + atk + defe + atksp + defsp + spd
			cbhp, cbatk, cbdefe, cbatksp, cbdefsp, cbspd = pintar_stats(hp, atk, defe, atksp, defsp, spd)
			etipo1 = pintar_tipo(tipo1)
		#	etipo1 = etipo
			etipo2 = pintar_tipo(tipo2)
		#	etipo2 = etipo
	#		if (((hab2 is not " ") or (hab2 is not "No tiene")) and ((habo is not " ") or (habo is not "No tiene"))):
	#			habilidades = "`Habilidad 1` " + str(hab1) + "\n`Habilidad 2` " + str(hab2) + "\n`Hab. Oculta` " + str(habo)
	#		elif ((hab2 is not " ") or (hab2 is not "No tiene")):
	#			habilidades = "`Habilidad 1` " + str(hab1) + "\n`Habilidad 2` " + str(hab2)
	#		elif ((habo is not " ") or (habo is not "No tiene")):
	#			habilidades = "`Habilidad 1` " + str(hab1) + "\n`Hab. Oculta` " + str(habo)
	#		else:
	#			habilidades = "`Habilidad` " + str(hab1)
			print("¿Tiene habilidad 2?: " + hab2)
			print("Confirmamos si tiene o no habilidad 2:")
			if (((hab2 == " ") or (hab2 == "No tiene")) and ((habo == " ") or (habo == "No tiene"))):
				print("hab2 error en if")
				habilidades = "`Habilidad` " + str(hab1)
			elif ((habo == " ") or (habo == "No tiene")):
				habilidades = "`Habilidad 1` " + str(hab1) + "\n`Habilidad 2` " + str(hab2)
				print("elif1")
			elif ((hab2 == " ") or (hab2 == "No tiene")):
				habilidades = "`Habilidad 1` " + str(hab1) + "\n`Hab. Oculta` " + str(habo)
				print("elif2")
			else:
				habilidades = "`Habilidad 1` " + str(hab1) + "\n`Habilidad 2` " + str(hab2) + "\n`Hab. Oculta` " + str(habo)	
				print("Else")

			print("Hemos confirmado la hab2. Vamos a confirmar el tipo2")
			if (tipo2 is not " "):
				tipos = "`" + tipo1 + etipo1 + "`\n" + "`" + tipo2 + etipo2 + "`"
			else:
				tipos = tipo1 + etipo1
			
			print("Add ')' a los links que sean necesarios")
			if ")" in imgpkm:
				imgpkm = imgpkm
			else:
				imgpkm = imgpkm + ")"
			
			print("Empezamos comprovacion de Pokemons especiales")
			if "Código cero" in name:
				sname = "type\_null"
			elif "Lycanroc nocturno" in name:
				sname = "lycanroc-midnight"
			elif "Wishiwashi forma individual" in name:
				sname = "wishiwashi"
			elif "Minior forma meteorito" in name:
				sname = "minior"
			elif "Minior forma núcleo" in name:
				sname = "minior"
			elif " " in name:
				sname = name.replace(" ", "_")
			else:
				sname = name
			
			print("dex sin mega ni alola")
			if dex > 9999: dex %= 1000
			print(dex)
		#	try:
		#		if len(dex) == 5:
		#			print("Entramos al if")
		#			dex = dex[2:]
		#		else:
		#			print("Entramos al else")
		#			dex = dex
		#	except Exception as e:
		#		print(e)

			print("Procedemos a enviar la ficha al chat")
			ficha = "_# {0}_ - *{1}*\n{2}\n\n`PS:` {3}{4}\n`Ataque:` {5}{6}\n`Defensa:` {7}{8}\n`Atk. Esp.:` {9}{10}\n`Def. Esp.:` {11}{12}\n`Velocidad:` {13}{14}\n`Total:` {15}\n\n{16}\n[⁣]({17}\n[{1} en Smogon](http://www.smogon.com/dex/sm/pokemon/{18})"
			bot.reply_to(m, ficha.format(dex, name, tipos, cbhp, hp, cbatk, atk, cbdefe, defe, cbatksp, atksp, cbdefsp, defsp, cbspd, spd, t, habilidades, imgpkm, sname), parse_mode = "Markdown")


			#bot.reply_to(m,
			#"_#" + dex + "_ - " + "*" + name + "*\n" + tipos + "\n\n`PS`: " + str(cbhp) + str(hp) +
			#"\n`Ataque` " + str(cbatk) + str(atk) + "\n`Defensa` " + str(cbdefe)+ str(defe) + "\n`Atk. Esp.` " + str(cbatksp) + str(atksp) +
			#"\n`Def. Esp.` " + str(cbdefsp) + str(defsp) + "\n`Velocidad` " + str(cbspd) + str(spd) + "\n`Total` " + str(t) +
			#"\n\n" + habilidades + "\n" + "[⁣](" + imgpkm
			#+ "\n["+name+ " en Smogon](http://www.smogon.com/dex/sm/pokemon/" + sname + ")", parse_mode = "Markdown")
			
			#print("L419. Parece que L319 peta al ser dex un INT")
			#print("_#" + dex + "_ - " + "*" + name + "*\n" + tipos + "\n\n`PS`: " + str(cbhp) + str(hp) +"\n`Ataque` " + str(cbatk) + str(atk) + "\n`Defensa` " + str(cbdefe)+ str(defe) + "\n`Atk. Esp.` " + str(cbatksp) + str(atksp) + "\n`Def. Esp.` " + str(cbdefsp) + str(defsp) + "\n`Velocidad` " + str(cbspd) + str(spd) + "\n`Total` " + str(t) + "\n\n" + habilidades + "\n" + "[⁣](" + imgpkm + "\n\n["+name+ " en Smogon](http://www.smogon.com/dex/sm/pokemon/" + name + ")")
			print("L421. Estoy aquí porque estoy comprobando si dex necesita ser pasado a str en el print o no.")
			print("_#" + str(dex) + "_ - " + "*" + name + "*\n" + tipos + "\n\n`PS`: " + str(cbhp) + str(hp) +"\n`Ataque` " + str(cbatk) + str(atk) + "\n`Defensa` " + str(cbdefe)+ str(defe) + "\n`Atk. Esp.` " + str(cbatksp) + str(atksp) + "\n`Def. Esp.` " + str(cbdefsp) + str(defsp) + "\n`Velocidad` " + str(cbspd) + str(spd) + "\n`Total` " + str(t) + "\n\n" + habilidades + "\n" + "[⁣](" + imgpkm + "\n\n["+name+ " en Smogon](http://www.smogon.com/dex/sm/pokemon/" + name + ")")

	except Exception as e:
		print(e)
		bot.reply_to(m, "Introduce un pokémon, por favor.")
