# -*- coding: utf-8 -*-
import sys
import re
import telebot
from telebot import types
import time 
import json
import urllib
import random
import PIL
from PIL import Image
import sqlite3

con = sqlite3.connect('pkmnbot.db')
c = con.cursor()

print ("La base de datos funciona")

def una_habilidad(skill, s0):
	print("Entro en la función 1")
	s0 = skill[0]['ability']['name']
	return s0
#

def dos_habilidades(skill, sh, s0, s1):
	f = 0
	print("Entro en la función 2")
	if skill[0]['is_hidden'] == True:
		print("Tiene 1 habilidad y una oculta    1")
		sh = skill[0]['ability']['name']
		s1 = skill[1]['ability']['name']
									
	if skill[1]['is_hidden'] == True:
		print("Tiene 1 habilidad y una oculta    2")
		sh = skill[1]['ability']['name']
		s0= skill[0]['ability']['name']
		f = 1
									
	if (skill[0]['is_hidden'] == False) and (skill[1]['is_hidden'] == False):
		print("Tiene 2 habilidades y no oculta")
		s0 = skill[0]['ability']['name']
		s1 = skill[1]['ability']['name']
		f= 2
	return sh,s0,s1,f
##

def tres_habilidades(skill, sh, s0, s1, s2):
	print("Entro en la función 3")
	f = 0
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
		f = 1
	if skill[2]['is_hidden'] == True:
		print("Tiene 2 habilidad y una oculta    3")
		sh = skill[2]['ability']['name']
		s0= skill[0]['ability']['name']
		s1 = skill[1]['ability']['name']
		f = 2
	if (skill[0]['is_hidden'] == False) and (skill[1]['is_hidden'] == False) and (skill[2]['is_hidden'] == False):
		print("Tiene 3 habilidad y no oculta")
		s0 = skill[0]['ability']['name']
		s1 = skill[1]['ability']['name']
		s2 = skill[2]['ability']['name']
		f = 3
	return sh,s0,s1,s2,f




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





#c.execute('''CREATE TABLE PKMN (IDUSER INT PRIMARY KEY NOT NULL, ALIAS TEXT NOT NULL, FC TEXT NOT NULL)''')
#c.execute('''CREATE TABLE pruebapoke6 (idPkmn INT(5) ZFILL, nombrePkmn TEXT NOT NULL, PRIMARY KEY (idPkmn)''')

#c.execute('''CREATE TABLE POKEMON (idpkmn INT PRIMARY KEY, Ndex TEXT NOT NULL Unique,
#Nombre TEXT NOT NULL, Linkfoto TEXT NOT NULL, hp INT NOT NULL, atk INT NOT NULL, defe INT NOT NULL
#, atksp INT NOT NULL, defsp INT NOT NULL, spd INT NOT NULL, hab1 TEXT NOT NULL, hab2 TEXT NOT NULL
#, habo TEXT NOT NULL, tipo1 TEXT NOT NULL, tipo2 TEXT NOT NULL, evhp INT NOT NULL, evatk INT NOT NULL 
#, evdefe INT NOT NULL, evatksp INT NOT NULL, evdefsp INT NOT NULL, evspd INT NOT NULL)''')

#c.execute("DROP TABLE POKEMON")

print ("La tabla se ha creado")

#c.execute("INSERT INTO pruebapoke (idPkmn,nombrePkmn) VALUES (0002,'prueba poke 1')")

#c.execute("INSERT INTO POKEMON (idpkmn,Ndex,Nombre,Linkfoto,hp,atk,defe,atksp,defsp,spd,hab1,hab2,habo,tipo1,tipo2,evhp,evatk,evdefe,evatksp,evdefsp,evspd) VALUES (NULL, 9999999, 'Pokémonprueba', 'http://pokeapi.co/static/do-logo.png', 99999, 99999, 99999, 99999, 99999, 99999, 'Programasdor', 'Haker', 'Shurmano', 'Forero', 'Troll', 0000000, 0000000, 0000000, 0000000, 0000000, 0000000)")

print ("Se ha insertado la línea")

#c.execute("DELETE FROM PKMN WHERE FC = '0319-1654-1156'")
#c.execute("DELETE FROM PKMN WHERE ALIAS = 'Solonen'")
#c.execute("DELETE FROM PKMN WHERE IDUSER = 100732897")


#c.execute("UPDATE PKMN SET 'alias' = '@Miniadri'  WHERE fc = '4167-4481-7117'")
uid = '9662836'
fc1 = '1111-1111-2222'
#c.execute("UPDATE PKMN SET 'fc' = '" + fc1 +  "' WHERE iduser = " + uid)
#c.execute("UPDATE PKMN SET 'fc' = '1111-1111-1111' WHERE iduser = 9662836" )

#c.execute("ALTER TABLE PKMN ADD UNIQUE (fc)")
#c.execute("ALTER TABLE PKMN MODIFY fc TEXT UNIQUE")
#####c.execute("ALTER TABLE PKMN ADD UNIQUE un_fc (fc) ")

#ALTER TABLE usuarios ADD UNIQUE usuarios_email_uk (email);
#ALTER TABLE supplier  MODIFY supplier_name char(100) NOT NULL;

#ALTER TABLE Persons ADD CONSTRAINT uc_PersonID UNIQUE (P_Id,LastName)

#ALTER TABLE Persons ADD UNIQUE (P_Id)

#c.execute("SELECT iduser,alias,fc from PKMN")
#c.execute("SELECT idPkmn,nombrePkmn from pruebapoke1 ORDER BY nombrePkmn ASC")
#c.execute("SELECT idpkmn,Ndex,Nombre,Linkfoto,hp,atk,defe,atksp,defsp,spd,hab1,hab2,habo,tipo1,tipo2,evhp,evatk,evdefe,evatksp,evdefsp,evspd from POKEMON") #WHERE Ndex = 000003
for i in c:
	print("ID = " , i[0], "Ndex = " , i[1], "Nombre = ", i[2])
	print("\n" , i[0] ,"\n" , i[1] ,"\n" , i[2] ,"\n" , i[3] ,"\n" , i[4] ,"\n" , i[5] ,"\n" , i[6] ,"\n" , i[7] ,"\n" , i[8] ,"\n" , i[9] ,"\n" , i[10] ,"\n" , i[11] ,"\n" , i[12] ,"\n" , i[13] ,"\n" , i[14] ,"\n" , i[15] ,"\n" , i[16] ,"\n" , i[17] ,"\n" , i[18] ,"\n" , i[19] ,"\n" , i[20])

k = 722
for i in range(283, k):
	habo = "No tiene"
	hab1 = "No tiene"
	hab2 = "No tiene"
	##### POKEMON
	url = 'http://pokeapi.co/api/v2/pokemon/' + str(i)
	request = urllib.request.Request(url)
	request.add_header('User-Agent',"Mozilla/5.0 (X11; Linux i586; rv:31.0) Gecko/20100101 Firefox/31.0")
	data = urllib.request.urlopen(request)
	datajson = json.loads(data.read().decode(data.info().get_param('charset') or 'utf-8'))
	name = datajson["forms"][0]['name'].title()
	tipo2 = " "
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
		try:
			tipo2 = datajson["types"][1]["type"]["name"]
			tipo2 = tipos.get(tipo2)
		except:
			print("jaja salu2")
		
		tipo1 = tipos.get(tipo1)
		
		
		
		t = hp + atk + defe + atksp +defsp + spd
		sh = ""
		s0 = ""
		s1 = ""
		s2 = ""
		for r in datajson['abilities']:
								
			print(r)
						
						
			skill = datajson['abilities']
				
							
		print(str(datajson['id']).zfill(5))
		npkmn = str(datajson['id']).zfill(5)
		imgpkm = "https://raw.githubusercontent.com/Intervencion/PKMNFCbot/master/Sprites/" + str(npkmn) + ".png)"
							
		print("ahora debo devolver el nombre de la habilidad")
		print(skill[0]['ability']['name'])
		print()
		print(len(skill))
		i = len(skill)
		print(skill[0]['is_hidden'])
							
							
		if i==1:
			s0 = una_habilidad(skill, s0)
			url1 = 'http://pokeapi.co/api/v2/ability/' + s0
			request1 = urllib.request.Request(url1)
			request1.add_header('User-Agent',"cheese")
			data1 = urllib.request.urlopen(request1)
			datajson1 = json.loads(data1.read().decode(data1.info().get_param('charset') or 'utf-8'))
			print("Ahora viene datajson de la habilidad")
			#print(datajson1["flavor_text_entries"]) DESCRIPCIONES DE LA HABILIDAD
			#print(datajson1["effect_entries"])  EFECTO SECUNDARIO EN INGLES
			print(datajson1["names"][2]["name"])
			hab1 = datajson1["names"][2]["name"]
#			c.execute("INSERT INTO POKEMON (idpkmn,Ndex,Nombre,Linkfoto,hp,atk,defe,atksp,defsp,spd,hab1,hab2,habo,tipo1,tipo2,evhp,evatk,evdefe,evatksp,evdefsp,evspd) VALUES (NULL, "+ str(npkmn) + ", '" + name + "', '" + imgpkm + "', " + str(hp) + ", " + str(atk) + ", " + str(defe) + ", " + str(atksp) + ", " + str(defsp) + ", " + str(spd) + ", '" + hab1 + "', '" + hab2 + "', '" + habo + "', '" + tipo1 + "', '" + tipo2 + "', " + str(evhp) + ", " + str(evatk) + ", " + str(evdefe) + ", " + str(evatksp) + ", " + str(evdefsp) + ", " + str(evspd) + ")")
						
		if i==2:
			sh, s0, s1, f = dos_habilidades(skill, sh, s0, s1)
			if f == 0:
				url1 = 'http://pokeapi.co/api/v2/ability/' + sh
				request1 = urllib.request.Request(url1)
				request1.add_header('User-Agent',"cheese")
				data1 = urllib.request.urlopen(request1)
				datajson1 = json.loads(data1.read().decode(data1.info().get_param('charset') or 'utf-8'))
				print("Ahora viene datajson de la habilidad")
				#print(datajson1["flavor_text_entries"]) DESCRIPCIONES DE LA HABILIDAD
				#print(datajson1["effect_entries"])  EFECTO SECUNDARIO EN INGLES
				print(datajson1["names"][2]["name"])
				habo = datajson1["names"][2]["name"]
				
				url1 = 'http://pokeapi.co/api/v2/ability/' + s1
				request1 = urllib.request.Request(url1)
				request1.add_header('User-Agent',"cheese")
				data1 = urllib.request.urlopen(request1)
				datajson1 = json.loads(data1.read().decode(data1.info().get_param('charset') or 'utf-8'))
				print("Ahora viene datajson de la habilidad")
				#print(datajson1["flavor_text_entries"]) DESCRIPCIONES DE LA HABILIDAD
				#print(datajson1["effect_entries"])  EFECTO SECUNDARIO EN INGLES
				print(datajson1["names"][2]["name"])
				hab1 = datajson1["names"][2]["name"]
				print(npkmn)
#				c.execute("INSERT INTO POKEMON (idpkmn,Ndex,Nombre,Linkfoto,hp,atk,defe,atksp,defsp,spd,hab1,hab2,habo,tipo1,tipo2,evhp,evatk,evdefe,evatksp,evdefsp,evspd) VALUES (NULL, "+ str(npkmn) + ", '" + name + "', '" + imgpkm + "', " + str(hp) + ", " + str(atk) + ", " + str(defe) + ", " + str(atksp) + ", " + str(defsp) + ", " + str(spd) + ", '" + hab1 + "', '" + hab2 + "', '" + habo + "', '" + tipo1 + "', '" + tipo2 + "', " + str(evhp) + ", " + str(evatk) + ", " + str(evdefe) + ", " + str(evatksp) + ", " + str(evdefsp) + ", " + str(evspd) + ")")

			elif f==1:
				url1 = 'http://pokeapi.co/api/v2/ability/' + sh
				request1 = urllib.request.Request(url1)
				request1.add_header('User-Agent',"cheese")
				data1 = urllib.request.urlopen(request1)
				datajson1 = json.loads(data1.read().decode(data1.info().get_param('charset') or 'utf-8'))
				print("Ahora viene datajson de la habilidad")
				#print(datajson1["flavor_text_entries"]) DESCRIPCIONES DE LA HABILIDAD
				#print(datajson1["effect_entries"])  EFECTO SECUNDARIO EN INGLES
				print(datajson1["names"][2]["name"])
				habo = datajson1["names"][2]["name"]
				
				url1 = 'http://pokeapi.co/api/v2/ability/' + s1
				request1 = urllib.request.Request(url1)
				request1.add_header('User-Agent',"cheese")
				data1 = urllib.request.urlopen(request1)
				datajson1 = json.loads(data1.read().decode(data1.info().get_param('charset') or 'utf-8'))
				print("Ahora viene datajson de la habilidad")
				#print(datajson1["flavor_text_entries"]) DESCRIPCIONES DE LA HABILIDAD
				#print(datajson1["effect_entries"])  EFECTO SECUNDARIO EN INGLES
				print(datajson1["names"][2]["name"])
				hab1 = datajson1["names"][2]["name"]
#				c.execute("INSERT INTO POKEMON (idpkmn,Ndex,Nombre,Linkfoto,hp,atk,defe,atksp,defsp,spd,hab1,hab2,habo,tipo1,tipo2,evhp,evatk,evdefe,evatksp,evdefsp,evspd) VALUES (NULL, "+ str(npkmn) + ", '" + name + "', '" + imgpkm + "', " + str(hp) + ", " + str(atk) + ", " + str(defe) + ", " + str(atksp) + ", " + str(defsp) + ", " + str(spd) + ", '" + hab1 + "', '" + hab2 + "', '" + habo + "', '" + tipo1 + "', '" + tipo2 + "', " + str(evhp) + ", " + str(evatk) + ", " + str(evdefe) + ", " + str(evatksp) + ", " + str(evdefsp) + ", " + str(evspd) + ")")
			
			elif f==2:
				url1 = 'http://pokeapi.co/api/v2/ability/' + s0
				request1 = urllib.request.Request(url1)
				request1.add_header('User-Agent',"cheese")
				data1 = urllib.request.urlopen(request1)
				datajson1 = json.loads(data1.read().decode(data1.info().get_param('charset') or 'utf-8'))
				print("Ahora viene datajson de la habilidad")
				#print(datajson1["flavor_text_entries"]) DESCRIPCIONES DE LA HABILIDAD
				#print(datajson1["effect_entries"])  EFECTO SECUNDARIO EN INGLES
				print(datajson1["names"][2]["name"])
				hab1 = datajson1["names"][2]["name"]
				
				url1 = 'http://pokeapi.co/api/v2/ability/' + s1
				request1 = urllib.request.Request(url1)
				request1.add_header('User-Agent',"cheese")
				data1 = urllib.request.urlopen(request1)
				datajson1 = json.loads(data1.read().decode(data1.info().get_param('charset') or 'utf-8'))
				print("Ahora viene datajson de la habilidad")
				#print(datajson1["flavor_text_entries"]) DESCRIPCIONES DE LA HABILIDAD
				#print(datajson1["effect_entries"])  EFECTO SECUNDARIO EN INGLES
				print(datajson1["names"][2]["name"])
				hab2 = datajson1["names"][2]["name"]
#				c.execute("INSERT INTO POKEMON (idpkmn,Ndex,Nombre,Linkfoto,hp,atk,defe,atksp,defsp,spd,hab1,hab2,habo,tipo1,tipo2,evhp,evatk,evdefe,evatksp,evdefsp,evspd) VALUES (NULL, "+ str(npkmn) + ", '" + name + "', '" + imgpkm + "', " + str(hp) + ", " + str(atk) + ", " + str(defe) + ", " + str(atksp) + ", " + str(defsp) + ", " + str(spd) + ", '" + hab1 + "', '" + hab2 + "', '" + habo + "', '" + tipo1 + "', '" + tipo2 + "', " + str(evhp) + ", " + str(evatk) + ", " + str(evdefe) + ", " + str(evatksp) + ", " + str(evdefsp) + ", " + str(evspd) + ")")
									
		if i==3:
			sh, s0, s1, s2, f = tres_habilidades(skill, sh, s0, s1, s2)
			if f == 0:
				url1 = 'http://pokeapi.co/api/v2/ability/' + sh
				request1 = urllib.request.Request(url1)
				request1.add_header('User-Agent',"cheese")
				data1 = urllib.request.urlopen(request1)
				datajson1 = json.loads(data1.read().decode(data1.info().get_param('charset') or 'utf-8'))
				print("Ahora viene datajson de la habilidad")
				#print(datajson1["flavor_text_entries"]) DESCRIPCIONES DE LA HABILIDAD
				#print(datajson1["effect_entries"])  EFECTO SECUNDARIO EN INGLES
				print(datajson1["names"][2]["name"])
				habo = datajson1["names"][2]["name"]
				
				url1 = 'http://pokeapi.co/api/v2/ability/' + s1
				request1 = urllib.request.Request(url1)
				request1.add_header('User-Agent',"cheese")
				data1 = urllib.request.urlopen(request1)
				datajson1 = json.loads(data1.read().decode(data1.info().get_param('charset') or 'utf-8'))
				print("Ahora viene datajson de la habilidad")
				#print(datajson1["flavor_text_entries"]) DESCRIPCIONES DE LA HABILIDAD
				#print(datajson1["effect_entries"])  EFECTO SECUNDARIO EN INGLES
				print(datajson1["names"][2]["name"])
				hab1 = datajson1["names"][2]["name"]
				
				url1 = 'http://pokeapi.co/api/v2/ability/' + s2
				request1 = urllib.request.Request(url1)
				request1.add_header('User-Agent',"cheese")
				data1 = urllib.request.urlopen(request1)
				datajson1 = json.loads(data1.read().decode(data1.info().get_param('charset') or 'utf-8'))
				print("Ahora viene datajson de la habilidad")
				#print(datajson1["flavor_text_entries"]) DESCRIPCIONES DE LA HABILIDAD
				#print(datajson1["effect_entries"])  EFECTO SECUNDARIO EN INGLES
				print(datajson1["names"][2]["name"])
				hab2 = datajson1["names"][2]["name"]
#				c.execute("INSERT INTO POKEMON (idpkmn,Ndex,Nombre,Linkfoto,hp,atk,defe,atksp,defsp,spd,hab1,hab2,habo,tipo1,tipo2,evhp,evatk,evdefe,evatksp,evdefsp,evspd) VALUES (NULL, "+ str(npkmn) + ", '" + name + "', '" + imgpkm + "', " + str(hp) + ", " + str(atk) + ", " + str(defe) + ", " + str(atksp) + ", " + str(defsp) + ", " + str(spd) + ", '" + hab1 + "', '" + hab2 + "', '" + habo + "', '" + tipo1 + "', '" + tipo2 + "', " + str(evhp) + ", " + str(evatk) + ", " + str(evdefe) + ", " + str(evatksp) + ", " + str(evdefsp) + ", " + str(evspd) + ")")

			
			elif f==1:
				url1 = 'http://pokeapi.co/api/v2/ability/' + sh
				request1 = urllib.request.Request(url1)
				request1.add_header('User-Agent',"cheese")
				data1 = urllib.request.urlopen(request1)
				datajson1 = json.loads(data1.read().decode(data1.info().get_param('charset') or 'utf-8'))
				print("Ahora viene datajson de la habilidad")
				#print(datajson1["flavor_text_entries"]) DESCRIPCIONES DE LA HABILIDAD
				#print(datajson1["effect_entries"])  EFECTO SECUNDARIO EN INGLES
				print(datajson1["names"][2]["name"])
				habo = datajson1["names"][2]["name"]
				
				url1 = 'http://pokeapi.co/api/v2/ability/' + s0
				request1 = urllib.request.Request(url1)
				request1.add_header('User-Agent',"cheese")
				data1 = urllib.request.urlopen(request1)
				datajson1 = json.loads(data1.read().decode(data1.info().get_param('charset') or 'utf-8'))
				print("Ahora viene datajson de la habilidad")
				#print(datajson1["flavor_text_entries"]) DESCRIPCIONES DE LA HABILIDAD
				#print(datajson1["effect_entries"])  EFECTO SECUNDARIO EN INGLES
				print(datajson1["names"][2]["name"])
				hab1 = datajson1["names"][2]["name"]
				
				url1 = 'http://pokeapi.co/api/v2/ability/' + s2
				request1 = urllib.request.Request(url1)
				request1.add_header('User-Agent',"cheese")
				data1 = urllib.request.urlopen(request1)
				datajson1 = json.loads(data1.read().decode(data1.info().get_param('charset') or 'utf-8'))
				print("Ahora viene datajson de la habilidad")
				#print(datajson1["flavor_text_entries"]) DESCRIPCIONES DE LA HABILIDAD
				#print(datajson1["effect_entries"])  EFECTO SECUNDARIO EN INGLES
				print(datajson1["names"][2]["name"])
				hab2 = datajson1["names"][2]["name"]
#				c.execute("INSERT INTO POKEMON (idpkmn,Ndex,Nombre,Linkfoto,hp,atk,defe,atksp,defsp,spd,hab1,hab2,habo,tipo1,tipo2,evhp,evatk,evdefe,evatksp,evdefsp,evspd) VALUES (NULL, "+ str(npkmn) + ", '" + name + "', '" + imgpkm + "', " + str(hp) + ", " + str(atk) + ", " + str(defe) + ", " + str(atksp) + ", " + str(defsp) + ", " + str(spd) + ", '" + hab1 + "', '" + hab2 + "', '" + habo + "', '" + tipo1 + "', '" + tipo2 + "', " + str(evhp) + ", " + str(evatk) + ", " + str(evdefe) + ", " + str(evatksp) + ", " + str(evdefsp) + ", " + str(evspd) + ")")
			
			elif f==2:
				url1 = 'http://pokeapi.co/api/v2/ability/' + s0
				request1 = urllib.request.Request(url1)
				request1.add_header('User-Agent',"cheese")
				data1 = urllib.request.urlopen(request1)
				datajson1 = json.loads(data1.read().decode(data1.info().get_param('charset') or 'utf-8'))
				print("Ahora viene datajson de la habilidad")
				#print(datajson1["flavor_text_entries"]) DESCRIPCIONES DE LA HABILIDAD
				#print(datajson1["effect_entries"])  EFECTO SECUNDARIO EN INGLES
				print(datajson1["names"][2]["name"])
				habo = datajson1["names"][2]["name"]
				
				url1 = 'http://pokeapi.co/api/v2/ability/' + s0
				request1 = urllib.request.Request(url1)
				request1.add_header('User-Agent',"cheese")
				data1 = urllib.request.urlopen(request1)
				datajson1 = json.loads(data1.read().decode(data1.info().get_param('charset') or 'utf-8'))
				print("Ahora viene datajson de la habilidad")
				#print(datajson1["flavor_text_entries"]) DESCRIPCIONES DE LA HABILIDAD
				#print(datajson1["effect_entries"])  EFECTO SECUNDARIO EN INGLES
				print(datajson1["names"][2]["name"])
				hab1 = datajson1["names"][2]["name"]
				
				url1 = 'http://pokeapi.co/api/v2/ability/' + s1
				request1 = urllib.request.Request(url1)
				request1.add_header('User-Agent',"cheese")
				data1 = urllib.request.urlopen(request1)
				datajson1 = json.loads(data1.read().decode(data1.info().get_param('charset') or 'utf-8'))
				print("Ahora viene datajson de la habilidad")
				#print(datajson1["flavor_text_entries"]) DESCRIPCIONES DE LA HABILIDAD
				#print(datajson1["effect_entries"])  EFECTO SECUNDARIO EN INGLES
				print(datajson1["names"][2]["name"])
				hab2 = datajson1["names"][2]["name"]
#				c.execute("INSERT INTO POKEMON (idpkmn,Ndex,Nombre,Linkfoto,hp,atk,defe,atksp,defsp,spd,hab1,hab2,habo,tipo1,tipo2,evhp,evatk,evdefe,evatksp,evdefsp,evspd) VALUES (NULL, "+ str(npkmn) + ", '" + name + "', '" + imgpkm + "', " + str(hp) + ", " + str(atk) + ", " + str(defe) + ", " + str(atksp) + ", " + str(defsp) + ", " + str(spd) + ", '" + hab1 + "', '" + hab2 + "', '" + habo + "', '" + tipo1 + "', '" + tipo2 + "', " + str(evhp) + ", " + str(evatk) + ", " + str(evdefe) + ", " + str(evatksp) + ", " + str(evdefsp) + ", " + str(evspd) + ")")
			elif f==3:
				url1 = 'http://pokeapi.co/api/v2/ability/' + s0
				request1 = urllib.request.Request(url1)
				request1.add_header('User-Agent',"cheese")
				data1 = urllib.request.urlopen(request1)
				datajson1 = json.loads(data1.read().decode(data1.info().get_param('charset') or 'utf-8'))
				print("Ahora viene datajson de la habilidad")
				#print(datajson1["flavor_text_entries"]) DESCRIPCIONES DE LA HABILIDAD
				#print(datajson1["effect_entries"])  EFECTO SECUNDARIO EN INGLES
				print(datajson1["names"][2]["name"])
				hab1 = datajson1["names"][2]["name"]				

				url1 = 'http://pokeapi.co/api/v2/ability/' + s1
				request1 = urllib.request.Request(url1)
				request1.add_header('User-Agent',"cheese")
				data1 = urllib.request.urlopen(request1)
				datajson1 = json.loads(data1.read().decode(data1.info().get_param('charset') or 'utf-8'))
				print("Ahora viene datajson de la habilidad")
				#print(datajson1["flavor_text_entries"]) DESCRIPCIONES DE LA HABILIDAD
				#print(datajson1["effect_entries"])  EFECTO SECUNDARIO EN INGLES
				print(datajson1["names"][2]["name"])
				hab2 = datajson1["names"][2]["name"]
				
				url1 = 'http://pokeapi.co/api/v2/ability/' + s2
				request1 = urllib.request.Request(url1)
				request1.add_header('User-Agent',"cheese")
				data1 = urllib.request.urlopen(request1)
				datajson1 = json.loads(data1.read().decode(data1.info().get_param('charset') or 'utf-8'))
				print("Ahora viene datajson de la habilidad")
				#print(datajson1["flavor_text_entries"]) DESCRIPCIONES DE LA HABILIDAD
				#print(datajson1["effect_entries"])  EFECTO SECUNDARIO EN INGLES
				print(datajson1["names"][2]["name"])
				hab3 = datajson1["names"][2]["name"]				
#				c.execute("INSERT INTO POKEMON (idpkmn,Ndex,Nombre,Linkfoto,hp,atk,defe,atksp,defsp,spd,hab1,hab2,habo,tipo1,tipo2,evhp,evatk,evdefe,evatksp,evdefsp,evspd) VALUES (NULL, "+ str(npkmn) + ", '" + name + "', '" + imgpkm + "', " + str(hp) + ", " + str(atk) + ", " + str(defe) + ", " + str(atksp) + ", " + str(defsp) + ", " + str(spd) + ", '" + hab1 + "', '" + hab2 + "', '" + habo + "', '" + tipo1 + "', '" + tipo2 + "', " + str(evhp) + ", " + str(evatk) + ", " + str(evdefe) + ", " + str(evatksp) + ", " + str(evdefsp) + ", " + str(evspd) + ")")
		print("debería funcionar")
		print("\nTerminado " + name + "\n")
		con.commit()
		time.sleep(10)
		p = open('pokedex.txt', 'a')
		p.write("Terminado " + name + "\n")
		p.close()
print("TODA LA DEX COMPLETA")
	
#for i in c:
#	print ("idpokemon = ", i[0], "nombrepokemon = ", i[1])

#c.execute("SELECT iduser,alias,fc from PKMN ORDER BY alias ASC")

#for i in c:
#	print ("ID = ", i[0], "ALIAS = ", i[1], "- FC = ", i[2], "\n")
	
#print ("Este es el select")

#uid = 9662836

#c.execute("SELECT alias,fc from PKMN WHERE iduser=" + str(uid))
#for i in c:
#	alias_resultado = i[0] + ":  "
#	fc_resultado = i[1]
#	print("vamo a ver el select", fc_resultado, alias_resultado)
#	bot.send_message( cid, "@" + alias_resultado + ": " + fc_resultado, parse_mode = "Markdown")

@bot.message_handler(commands=['stats'])
def command_stats(m):
	cid = m.chat.id
	bot.send_chat_action(cid, "typing")
	nomega = ["venusaur", "blastoise", "Charizard", "alakazam", "gengar", "kaaangaskhan", "pinsir", "gyarados", "aerodactyl", "mewtwo", "ampharos", "scizor", "heracross", "houndoom", "tyranitar", "blaziken", "gardevoir", "mawile", "aggron", "medichamp", "manectric", "banette", "absol", "garchomp", "lucario", "pidgeot", "sharpedo", "salamance", "abomasnow", "beedrill", "slowbro", "steelix", "sceptile", "swampert", "sableye", "camerut", "altaria", "glalie", "metagross", "latios", "latias", "rayquaza", "lopunny", "gallade", "audino", "diancie"]
	alola = ["Rattata", "Raticate", "Raichu", "Sandshrew", "Sandslash", "Vulpix", "Ninetales", "Diglett", "Dugtrio", "Meowth", "Persian", "Geodude", "Graveler", "Golem", "Grimer", "Muk", "Exeggutor", "Marowak"]
	pkmn = m.text.capitalize()
	
	
	if (m.text.lower().split(' ', 2)[2] == "mega"):
		npkmn = m.text.lower().split(' ', 2)[1]
		if(npkmn in nomega):
			print("Sé que pone mega y además tiene mega")
			bot.reply_to(m, "Las megas estarán pronto, ¡lo siento!", reply_markup=markup, parse_mode="Markdown")
		else:
			print("Sé que pone mega y este poke no tiene mega")
			bot.reply_to(m, "Este poke no tiene mega, pedazo troll", reply_markup=markup, parse_mode="Markdown")
	
	elif(m.text.lower().split(' ', 2)[2] == "alola"):
		npkmn = m.text.lower().split(' ', 2)[1]
		if(npkmn in alolaform):
			print("Sé que pone alola y además tiene forma alola")
			dex,name,imgpkm, hp, atk, defe, atksp, defsp, spd, hab1, hab2, habo, tipo1, tipo2, evhp, evatk, evdefe, evatksp, evdefsp, evspd = poke_normal(pkmn)
			dex = dex -10000
			t = hp + atk + defe + atksp +defsp + spd
			cbhp, cbatk, cbdefe, cbatksp, cbdefsp, cbspd = pintar_stats(hp, atk, defe, atksp, defsp, spd)
			etipo = pintar_tipo(tipo1)
			etipo1 = etipo
			etipo = pintar_tipo(tipo2)
			etipo2 = etipo
			
			if (tipo2 is not " "):
				tipos = tipo1 + etipo1 + " " +  tipo2 + etipo2
			else:
				tipos = tipo1 + etipo1
				
			bot.reply_to(m,
			"_#" + dex + "_ - " + "*" + name + "*\n" + tipos + "\n\n`PS`: " + str(cbhp) + str(hp) +
			"\n`Ataque` " + str(cbatk) + str(atk) + "\n`Defensa` " + str(cbdefe)+ str(defe) + "\n`Atk. Especial` " + str(cbatksp) + str(atksp) + 
			"\n`Def. Especial` " + str(cbdefsp) + str(defsp) + "\n`Velocidad` " + str(cbspd) + str(spd) + "\n`Total` " + str(t) + 
			"\n\n`Habilidad 1` " + str(hab1) + "\n`Habilidad 2` " + str(hab2) + "\n`Hab. Oculta` " + str(habo) + "[ ](" + imgpkm 
			+ "\n\n["+name+ " en Smogon](http://www.smogon.com/dex/xy/pokemon/" + name + ")",reply_markup=markup, parse_mode = "Markdown")

			
		else:
			print("Sé que pone alola y este poke no tiene forma alola")
			bot.reply_to(m, "Este poke no tiene forma alola, pedazo troll", reply_markup=markup, parse_mode="Markdown")
		
	else:
		print("No pone mega ni pone alola")
		dex,name,imgpkm, hp, atk, defe, atksp, defsp, spd, hab1, hab2, habo, tipo1, tipo2, evhp, evatk, evdefe, evatksp, evdefsp, evspd = poke_normal(pkmn)
		cbhp, cbatk, cbdefe, cbatksp, cbdefsp, cbspd = pintar_stats(hp, atk, defe, atksp, defsp, spd)
		etipo = pintar_tipo(tipo1)
		etipo1 = etipo
		etipo = pintar_tipo(tipo2)
		etipo2 = etipo
		bot.reply_to(m,
		"_#" + dex + "_ - " + "*" + name + "*\n" + tipos + "\n\n`PS`: " + str(cbhp) + str(hp) +
		"\n`Ataque` " + str(atk) + "\n`Defensa` " + str(defe) + "\n`Atk. Especial` " + str(atksp) + 
		"\n`Def. Especial` " + str(defsp) + "\n`Velocidad` " + str(spd) + "\n`Total` " + str(t) + 
		"\n\n`Habilidad 1` " + str(s1) + "\n`Habilidad 2` " + str(s0) + "\n`Hab. Oculta` " + str(sh) + "[ ](" + imgpkm 
		+ "\n\n["+name+ " en Smogon](http://www.smogon.com/dex/xy/pokemon/" + name + ")",reply_markup=markup, parse_mode = "Markdown")



def poke_normal(pkmn):
	print("entro en la función de poke normal")
#	c.execute("SELECT Ndex,Nombre,Linkfoto,hp,atk,defe,atksp,defsp,spd,hab1,hab2,habo,tipo1,tipo2,evhp,evatk,evdefe,evatksp,evdefsp,evspd from POKEMON WHERE Nombre='" + str(pkmn)+ "'")
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
		
	return dex,name,imgpkm, hp, atk, defe, atksp, defsp, spd, hab1, hab2, habo, tipo1, tipo2, evhp, evatk, evdefe, evatksp, evdefsp, evspd

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
		defe = "📒"
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
		defsp = "📒"
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
	
	
	
def pintar_tipo(tipo):
	if(tipo == "Acero"):
		etipo = "⚙"
	elif(tipo == "Agua"):
		etipo = "💦"
	elif(tipo == "Bicho"):
		etipo = "🐛"
	elif(tipo == "Dragón"):
		etipo = "🐉"
	elif(tipo == "Eléctrico"):
		etipo = "⚡️"
	elif(tipo == "Fantasma"):
		etipo = "👻"
	elif(tipo == "Fuego"):
		etipo = "🔥"
	elif(tipo == "Hada"):
		etipo = "🌸"
	elif(tipo == "Hielo"):
		etipo = "❄️"
	elif(tipo == "Lucha"):
		etipo = "💪"
	elif(tipo == "Normal"):
		etipo = "🐕"
	elif(tipo == "Planta"):
		etipo = "🍃"
	elif(tipo == "Psíquico"):
		etipo = "🔮"
	elif(tipo == "Roca"):
		etipo = "🗿"
	elif(tipo == "Siniestro"):
		etipo = "👤"
	elif(tipo == "Tierra"):
		etipo = "🌎"
	elif(tipo == "Veneno"):
		etipo = "🍄"
	elif(tipo == "Volador"):
		etipo = "u\u1F32A"

	return etipo


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


con.commit()

con.close()





#for item in my_list:
#  c.execute('insert into tablename values (?,?,?)', item)
