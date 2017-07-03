from config import *

@bot.message_handler(commands=['exec'])
def command_exec(m):
    cid = m.chat.id
    uid = m.from_user.id
    #try:
        #send_udp('exec')
    #except Exception as e:
    #    bot.send_message(1896312, send_exception(e), parse_mode="Markdown")
    if not is_recent(m):
        return None
    if m.from_user.id in admins:
        if len(m.text.split()) == 1:
            bot.send_message(
                cid,
                "Uso: /exec _<code>_ - Ejecuta el siguiente bloque de código.",
                parse_mode="Markdown")
            return
        cout = StringIO()
        sys.stdout = cout
        cerr = StringIO()
        sys.stderr = cerr
        code = ' '.join(m.text.split(' ')[1:])
        try:
            exec(code)
        except Exception as e:
            bot.send_message(cid, send_exception(e), parse_mode="Markdown")
        else:
            if cout.getvalue():
                bot.send_message(cid, str(cout.getvalue()))
        sys.stdout = sys.__stdout__
        sys.stderr = sys.__stderr__
        
@bot.message_handler(commands=['restart'])
def command_restart(m):
	if m.from_user.id in admins:
		try:
			os.execl(sys.executable, sys.executable, *sys.argv)
		except:
			bot.send_message(cid, "Mal código tete")
	else:
		bot.send_message(cid, "Comando reservado a SU.")