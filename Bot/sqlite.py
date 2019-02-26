# -*- coding: utf-8 -*-
import sys
import re
import telebot
from telebot import types
import time 
import json
import urllib
import random

import sqlite3

con = sqlite3.connect('pkmnbot.db')
c = con.cursor()

print ("La base de datos funciona")


# -------------------- CREACION DE TABLAS ---------------

#c.execute('''CREATE TABLE PKMN (IDUSER INT PRIMARY KEY NOT NULL, ALIAS TEXT NOT NULL, FC TEXT NOT NULL)''')
#c.execute('''CREATE TABLE pruebapoke6 (idPkmn INT(5) ZFILL, nombrePkmn TEXT NOT NULL, PRIMARY KEY (idPkmn)''')
#cid = -1001059767714
#gt = "miyamoto2"

#c.execute("INSERT INTO Grupo (idGrupo,NombreGrup) VALUES('" + str(cid) + "','" + "patata2" + "' )")
#c.execute("INSERT INTO Grupo (idGrupo,NombreGrup) VALUES('" + str(cid) + "','" + gt + "' )")

#c.execute("DELETE FROM UsuGrupo WHERE idUsuarioFK ='9662836' AND idGrupoFK ='-233668616'")

#c.execute("SELECT * FROM Grupo") # where idGrupo ='-1001059767714'")
#for i in c:
#    print(i[0])
#    print(i[1])

#c.execute("SELECT * FROM Usuarios")
#for j in c:
#    print(j[0])
#    print(j[1])
#    print(j[2])

#c.execute("SELECT * FROM UsuGrupo")
#for k in c:
#    print(k[0])
#    print(k[1])

#c.execute("SELECT idUsuario,ALIAS,FC FROM Usuarios INNER JOIN UsuGrupo ON Usuarios.idUsuario = UsuGrupo.idUsuarioFK WHERE UsuGrupo.idGrupoFK =" + str(cid))
#for l in c:
#    print("Este select funciona a la primera?")
#    print(l[0])
#    print(l[1])
#    print(l[2])

#c.execute("INSERT INTO Grupo (idGrupo,NombreGrup) VALUES('" + str(cid) + "','" + m.chat.title + "' )")

#  ------------------ CREACIÓN TABLAS NUEVAS REMODELACIÓN -----------
#c.execute('''CREATE TABLE Usuarios (idUsuario INT PRIMARY KEY NOT NULL, ALIAS TEXT NOT NULL, FC TEXT NOT NULL)''')
#print ("La tabla usuarios se ha creado")
#c.execute('''CREATE TABLE Grupo (idGrupo INT PRIMARY KEY NOT NULL, NombreGrup TEXT NOT NULL)''')
#print ("La tabla grupo se ha creado")
#c.execute('''CREATE TABLE UsuGrupo (idUsuarioFK INT NOT NULL, idGrupoFK INT NOT NULL, FOREIGN KEY(idUsuarioFK) REFERENCES Usuarios(idUsuario),FOREIGN KEY(idGrupoFK) REFERENCES Grupo(idGrupo))''')
#print ("La tabla usu-grupo se ha creado")
#  ------------------ FIN  CREACIÓN TABLAS NUEVAS REMODELACIÓN -----------

#c.execute('''CREATE TABLE POKEMON (idpkmn INT PRIMARY KEY, Ndex TEXT NOT NULL Unique,
#Nombre TEXT NOT NULL, Linkfoto TEXT NOT NULL, hp INT NOT NULL, atk INT NOT NULL, defe INT NOT NULL
#, atksp INT NOT NULL, defsp INT NOT NULL, spd INT NOT NULL, hab1 TEXT NOT NULL, hab2 TEXT NOT NULL
#, habo TEXT NOT NULL, tipo1 TEXT NOT NULL, tipo2 TEXT NOT NULL, evhp INT NOT NULL, evatk INT NOT NULL 
#, evdefe INT NOT NULL, evatksp INT NOT NULL, evdefsp INT NOT NULL, evspd INT NOT NULL)''')

#c.execute("DROP TABLE POKEMON")

print ("Todas las tablas se han creado")

#c.execute("INSERT INTO pruebapoke (idPkmn,nombrePkmn) VALUES (0002,'prueba poke 1')")

#c.execute("INSERT INTO POKEMON (idpkmn,Ndex,Nombre,Linkfoto,hp,atk,defe,atksp,defsp,spd,hab1,hab2,habo,tipo1,tipo2,evhp,evatk,evdefe,evatksp,evdefsp,evspd) VALUES (NULL, 9999999, 'Pokémonprueba', 'http://pokeapi.co/static/do-logo.png', 99999, 99999, 99999, 99999, 99999, 99999, 'Programasdor', 'Haker', 'Shurmano', 'Forero', 'Troll', 0000000, 0000000, 0000000, 0000000, 0000000, 0000000)")

#print ("Se ha insertado la línea")

#c.execute("DELETE FROM PKMN WHERE FC = '0319-1654-1156'")
#c.execute("DELETE FROM PKMN WHERE ALIAS = 'Solonen'")
#c.execute("DELETE FROM PKMN WHERE IDUSER = 100732897")


#c.execute("UPDATE PKMN SET 'alias' = '@Miniadri'  WHERE fc = '4167-4481-7117'")

##### ESTO DE ABAJO VA SIN COMENTAR
#uid = '9662836'
#fc1 = '1111-1111-2222'
## ESTO DE ARRIBA VA SIN COMENTAR

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

c.execute("SELECT name FROM sqlite_master WHERE type='table' ORDER BY name")
available_table=(c.fetchall())

res = c.execute("SELECT name FROM sqlite_master WHERE type='table';")
for name in res:
    print name[0]

#c.execute("SELECT Ndex,Nombre,Puntos_Salud FROM POKEMON" )
#for j in c:
#	print("Número dex: " + str(j[0]) + " Nombre: " + j[1] + " Sus PS son " + str(j[2]))

#c.execute("UPDATE POKEMON SET 'Nombre' = 'Tapu lele' WHERE Ndex = 786" )
#.execute("UPDATE POKEMON SET 'Nombre' = 'Shaymin' WHERE Ndex = 492" )

print ("Los pokes se han introducido correctamente")

con.commit()

con.close()





#for item in my_list:
#  c.execute('insert into tablename values (?,?,?)', item)
