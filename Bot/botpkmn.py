# -*- coding: utf-8 -*-
#!/usr/bin/env python3.6

######## SE LLAMARÁ botpkmn.py #############

from colorclass import Color
print(Color(
    '{autored}[{/red}{autoyellow}+{/yellow}{autored}]{/red} {autocyan}Cargando plugins...{/cyan}'))
    
    
from config import *
import importdir
import sys


importdir.do('NOTOCAR', globals())

print(Color(
    '{autored}[{/red}{autoyellow}+{/yellow}{autored}]{/red} {autocyan}Plugins cargados.{/cyan}'))


try:
    bot.send_message(admins[0], "@PKMNFCbot ha sido encendido")
except Exception as e:
    bot.send_message(admins[0], str(e))
    
#    try:
#    for admin in admins:
#        bot.send_message(admin, "@LoL_bot ha sido encendido")
#except Exception as e:
#    for admin in admins:
#        bot.send_message(admin, str(e))

print(Color(
    '{autored}[{/red}{autoyellow}+{/yellow}{autored}]{/red} {autocyan}@Rotomdex_FC_Bot ha sido encendido.{/cyan}\n'))

bot.skip_pending = True
bot.polling(none_stop=True)