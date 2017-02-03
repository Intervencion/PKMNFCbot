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

#c.execute("UPDATE POKEMON SET 'Nombre' = 'Código cero' WHERE Ndex = 772" )
#c.execute("UPDATE POKEMON SET 'Nombre' = 'Tapu koko' WHERE Ndex = 785" )
#c.execute("UPDATE POKEMON SET 'Nombre' = 'Tapu lulu' WHERE Ndex = 786" )
#c.execute("UPDATE POKEMON SET 'Nombre' = 'Tapu bulu' WHERE Ndex = 787" )
#c.execute("UPDATE POKEMON SET 'Nombre' = 'Tapu fini' WHERE Ndex = 788" )
#c.execute("UPDATE POKEMON SET 'atk' = 95  WHERE Ndex = 24" )
#c.execute("UPDATE POKEMON SET 'atk' = 100  WHERE Ndex = 51" )
#c.execute("UPDATE POKEMON SET 'spd' = 110  WHERE Ndex = 85" )
#c.execute("UPDATE POKEMON SET 'spd' = 150  WHERE Ndex = 101" )
#c.execute("UPDATE POKEMON SET 'defsp' = 75  WHERE Ndex = 103" )
#c.execute("UPDATE POKEMON SET 'atksp' = 86  WHERE Ndex = 164" )
#c.execute("UPDATE POKEMON SET 'defsp' = 70  WHERE Ndex = 168" )
#c.execute("UPDATE POKEMON SET 'defe' = 85  WHERE Ndex = 211" )
#c.execute("UPDATE POKEMON SET 'atksp' = 90  WHERE Ndex = 219" )
#c.execute("UPDATE POKEMON SET 'hp' = 65, 'defe' = 95, 'defsp' = 95 WHERE Ndex = 222" )
#c.execute("UPDATE POKEMON SET 'hp' = 85  WHERE Ndex = 226" )
#c.execute("UPDATE POKEMON SET 'defe' = 75  WHERE Ndex = 277" )
#c.execute("UPDATE POKEMON SET 'defe' = 95  WHERE Ndex = 279" )
#c.execute("UPDATE POKEMON SET 'defe' = 100, 'spd' = 80  WHERE Ndex = 284" )
#c.execute("UPDATE POKEMON SET 'spd' = 90  WHERE Ndex = 301" )
#c.execute("UPDATE POKEMON SET 'defe' = 75, 'defsp' = 85  WHERE Ndex = 313" )
#c.execute("UPDATE POKEMON SET 'defe' = 75, 'defsp' = 85  WHERE Ndex = 314" )
#c.execute("UPDATE POKEMON SET 'hp' = 90  WHERE Ndex = 337" )
#c.execute("UPDATE POKEMON SET 'hp' = 90  WHERE Ndex = 338" )
#c.execute("UPDATE POKEMON SET 'hp' = 75, 'defsp' = 90, 'defe' = 80  WHERE Ndex = 358" )
#c.execute("UPDATE POKEMON SET 'hp' = 65  WHERE Ndex = 527" )
#c.execute("UPDATE POKEMON SET 'atk' = 105  WHERE Ndex = 558" )
#c.execute("UPDATE POKEMON SET 'defe' = 130  WHERE Ndex = 614" )
#c.execute("UPDATE POKEMON SET 'hp' = 80, 'defe' = 50  WHERE Ndex = 614" )

#c.execute("UPDATE POKEMON SET 'hab1' = 'Cuerpo maldito'  WHERE Ndex = 94" )
#c.execute("UPDATE POKEMON SET 'habo' = 'Foco interno'  WHERE Ndex = 243" )
#c.execute("UPDATE POKEMON SET 'habo' = 'Foco interno'  WHERE Ndex = 244" )
#c.execute("UPDATE POKEMON SET 'habo' = 'Foco interno'  WHERE Ndex = 245" )
#c.execute("UPDATE POKEMON SET 'hab2' = 'Hidratación'  WHERE Ndex = 278" )
#c.execute("UPDATE POKEMON SET 'hab2' = 'Llovizna'  WHERE Ndex = 279" )
#c.execute("UPDATE POKEMON SET 'hab2' = 'Sequía'  WHERE Ndex = 324" )
#c.execute("UPDATE POKEMON SET 'hab2' = 'Armadura frágil'  WHERE Ndex = 524" )
#c.execute("UPDATE POKEMON SET 'hab2' = 'Armadura frágil'  WHERE Ndex = 525" )
#c.execute("UPDATE POKEMON SET 'hab2' = 'Chorro arena'  WHERE Ndex = 526" )
#c.execute("UPDATE POKEMON SET 'hab2' = 'Manto níveo'  WHERE Ndex = 582" )
#c.execute("UPDATE POKEMON SET 'hab2' = 'Manto níveo'  WHERE Ndex = 583" )
#c.execute("UPDATE POKEMON SET 'hab2' = 'Nevada'  WHERE Ndex = 584" )
#c.execute("UPDATE POKEMON SET 'hab2' = 'Quitanieves'  WHERE Ndex = 613" )
#c.execute("UPDATE POKEMON SET 'hab2' = 'Quitanieves'  WHERE Ndex = 614" )

#c.execute("UPDATE POKEMON SET 'tipo2' = 'Volador' WHERE Ndex = 10774" )

# PARA CAMBIAR LOS SPRITES
#k = 723
#for i in range(1, k):
#    c.execute("SELECT Linkfoto from POKEMON Where Ndex=" + i)
#    c.commit()
#    for i in c:
#        print("El link de la foto es ", i[0])
#        url = i[0]
#    url = url.replace("png","gif")
#   c.execute("UPDATE POKEMON SET 'Linkfoto' ='" + url + "Where Ndex =" + i)
#   c.commit()

# PARA CAMBIAR LOS SPRITES DE ALOLAS, MEGAS Y OTRAS FORMAS
#k = 10105
#for i in range(10019, k):
#   try:
    #    c.execute("SELECT Linkfoto from POKEMON Where Ndex=" + i)
    #    c.commit()
    #    for i in c:
    #        print("El link de la foto es ", i[0])
    #        url = i[0]
    #    url = url.replace("png","gif")
    #   c.execute("UPDATE POKEMON SET 'Linkfoto' ='" + url + "Where Ndex =" + i)
    #   c.commit()
#   except:
#        print("este número no tiene poke")



c.execute("SELECT idpkmn,Ndex,Nombre,Linkfoto,hp,atk,defe,atksp,defsp,spd,hab1,hab2,habo,tipo1,tipo2,evhp,evatk,evdefe,evatksp,evdefsp,evspd from POKEMON") #WHERE Ndex = 000003
for i in c:
    print("Ndex = " , i[1], "Nombre = ", i[2])
 #   print("\n" , i[0] ,"\n" , i[1] ,"\n" , i[2] ,"\n" , i[3] ,"\n" , i[4] ,"\n" , i[5] ,"\n" , i[6] ,"\n" , i[7] ,"\n" , i[8] ,"\n" , i[9] ,"\n" , i[10] ,"\n" , i[11] ,"\n" , i[12] ,"\n" , i[13] ,"\n" , i[14] ,"\n" , i[15] ,"\n" , i[16] ,"\n" , i[17] ,"\n" , i[18] ,"\n" , i[19] ,"\n" , i[20])



c.execute("SELECT Linkfoto from POKEMON Where Ndex= 10105")
for i in c:
    print("El link de la foto es ", i[0])
    url = i[0]
url = url.replace("png","gif")
print(url)



			

con.commit()


con.close()