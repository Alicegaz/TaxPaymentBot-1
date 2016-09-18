# -*- coding: utf-8 -*-

import config
import telebot 
from telebot import types
import time
import requests
import subprocess
import string
import json

bot = telebot.TeleBot(config.token)




def pay():
	markup = types.ReplyKeyboardMarkup()
	markup.row('Pay')





@bot.message_handler(commands=['start', 'help'])
def handle_start_help(message):
	bot.send_message(message.chat.id, "Abandon all hope, ye who enter here")

@bot.message_handler(commands=['pay'])
def handle_start_help(message):
	bot.send_message(message.chat.id, "Your balance is 31801 rubles. You have no debts. Have a good day!")

"""s
@bot.message_handler(func=lambda message: True, content_types=['text'])
def echo_msg(message):
	
	#bot.send_message(message.chat.id, message.text)
	#bot.send_message(message.chat.id, "Choose letter: ", reply_markup=markup)
	"""

@bot.message_handler(content_types=["photo"])
def save_msg(message):
	
	file_id = message.photo[2].file_id
	file_info = bot.get_file(file_id)
	downloaded_file = bot.download_file(file_info.file_path)
	
	with open("img.jpg", 'wb') as new_file:
		new_file.write(downloaded_file)
	lol = subprocess.check_output('python getqr.py img.jpg', shell=True)

	#
	#kek = str(lol)
	#res = json.loads(kek)
	#res = json.loads('{"name": "Alex","surname": "Kott","balance": "13432","electricity": "356","gas": "234","water": "120"}')


	#lol = subprocess.check_output('python paybill.py img.jpg', shell=True)
	bot.send_message(message.chat.id, lol)

	markup = types.ReplyKeyboardMarkup()
	markup.row('/pay')

	if message.from_user.id == 5844335:
		bot.send_message(message.chat.id, "Your balance is 32410 rubles. Debts: electricity - 132 r, gas - 425 r, water - 52 r. Do you want to pay?", reply_markup=markup)
		#bot.send_message(message.chat.id, reply_markup=markup)

	else:
		bot.send_message(message.chat.id, "You are not authorized user")


	#bot.send_message(message.chat.id, message.from_user.id)




if __name__ == '__main__':
	bot.polling(none_stop=True)