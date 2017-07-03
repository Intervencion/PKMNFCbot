from config import *

##############################ENTORNO DE PRUEBAS ##############################
###############################################################################


@bot.message_handler(commands=['btn'])
def command_evs0(m):
	cid = m.chat.id
	markup = types.InlineKeyboardMarkup()
	bttn = types.InlineKeyboardButton("Botón de prueba" , url="https://telegram.me/PKMNFCbot?start=evs")
#	b1 = types.InlineKeyboardButton("Botón de prueba" , url="/evs")
	markup.add(bttn)
	bot.reply_to(m,"Mensaje para botón de prueba", reply_markup=markup)


@bot.message_handler(commands=['pb'])
def command_pb(message):
	ficha = f"_# {dex}_ - *{name}*\n{tipos}\n\n`PS`: str{cbhp}{hp}\n`Ataque`: {cbatk}{atk}\n`Defensa`: {cbdefe}{defe}\n`Atk. Esp.`: {cbatksp}{atksp}\n`Def. Esp.`: {cbdefsp}{defsp}\n`Velocidad`: {cbspd}{spd}\n`Total`: {t}\n\n{habilidades}\n[⁣]({imgpkm}\n[{name} en Smogon](http://www.smogon.com/dex/sm/pokemon/{sname}))"
	markup = types.InlineKeyboardMarkup()
	print("MENSAJE PRIMERO",message.message_id)
	markup.add(types.InlineKeyboardButton("result1", callback_data="data1"))
	bot.send_message(message.chat.id, 'Hihi'+ ficha, reply_markup=markup)
  






	@bot.callback_query_handler(func=lambda call: call.data == 'data1')
	def r1_call_back(call):
		editm = call.message.message_id
		markup = types.InlineKeyboardMarkup()
		markup.add(types.InlineKeyboardButton("result2", callback_data="data2"))
		print("MENSAJE SEGUNDO",editm)
		print(call.message.chat.id)

#		bot.send_message(call.message.chat.id, 'llego al comando')
#		bot.edit_message_text("pole menta", call.from_user.id, call.message.chat.id, call.message.message_id, reply_markup=markup)
		bot.edit_message_text(ficha, call.message.chat.id , editm, reply_markup=markup)
		#bot.send_message(call.message.chat.id, 'llego al comando')
		bot.answer_callback_query(call.id, text="") #Sale en pantalla
		#bot.send_message(call.message.chat.id, 'paso el comando')






@bot.callback_query_handler(func=lambda call: call.data == 'data2')
def r2_call_back(call):
	editm = call.message.message_id
	markup = types.InlineKeyboardMarkup()
	markup.add(types.InlineKeyboardButton("result1", callback_data="data1"))
	print("MENSAJE SEGUNDO",editm)
	print(call.message.chat.id)

#	bot.send_message(call.message.chat.id, 'llego al comando')
#	bot.edit_message_text("pole menta", call.from_user.id, call.message.chat.id, call.message.message_id, reply_markup=markup)
	bot.edit_message_text("Amapolas", call.message.chat.id , editm, reply_markup=markup)
	#bot.send_message(call.message.chat.id, 'llego al comando')
	bot.answer_callback_query(call.id, text="")
	#bot.send_message(call.message.chat.id, 'paso el comando')

@bot.callback_query_handler(func=lambda call: call.data == pkmn)
def r0_call_back(call):
	editm = call.message.message_id
	markup = types.InlineKeyboardMarkup()
	markup.add(types.InlineKeyboardButton("entra en el bueno", callback_data="data2"))
	print("MENSAJE SEGUNDO",editm)
	print(call.message.chat.id)

#	bot.send_message(call.message.chat.id, 'llego al comando')
#	bot.edit_message_text("pole menta", call.from_user.id, call.message.chat.id, call.message.message_id, reply_markup=markup)
	bot.edit_message_text("estoy en el bueno ", call.message.chat.id , editm, reply_markup=markup)
	#bot.send_message(call.message.chat.id, 'llego al comando')
	bot.answer_callback_query(call.id, text="") #Sale en pantalla
	#bot.send_message(call.message.chat.id, 'paso el comando')