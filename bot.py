# -*- coding: utf-8 -*-

import config
import telebot 
from telebot import types
import time
import requests
import subprocess

bot = telebot.TeleBot(config.token)


markup = types.ReplyKeyboardMarkup()
markup.row('a', 'b')
markup.row('c', 'd')


@bot.message_handler(commands=['start', 'help'])
def handle_start_help(message):
	bot.send_message(message.chat.id, "Abandon all hope, ye who enter here")

@bot.message_handler(func=lambda message: True, content_types=['text'])
def echo_msg(message):
	
	bot.send_message(message.chat.id, message.text)
	#bot.send_message(message.chat.id, "Choose letter: ", reply_markup=markup)

@bot.message_handler(content_types=["photo"])
def save_msg(message):
	
	file_id = message.photo[2].file_id
	file_info = bot.get_file(file_id)
	downloaded_file = bot.download_file(file_info.file_path)
	
	with open("img.jpg", 'wb') as new_file:
		new_file.write(downloaded_file)
	#lol = subprocess.check_output('ls', shell=True)
	lol = subprocess.check_output('python getqr.py img.jpg', shell=True)
	#file_id = message.photo[2].file_id
	#file_name = message.photo[2].file_id
	#file_name = file_name+".png"
	#file_info = bot.get_file(file_id)
	bot.send_message(message.chat.id, lol)

	#"""

	#bot.send_message(message.chat.id, "ok")

	"""

	downloaded_file = bot.download_file(file_info.file_path)
	with open(file_name, 'wb') as new_file:
		new_file.write(downloaded_file)
	#bot.send_message(message.chat.id, message.photo[2])

	
	path = raw+'.jpg'
	file_info = bot.get_file(raw)
	downloaded_file = bot.download_file(file_info.file_path)
	qr.decode(downloaded_file)
	with open(path, 'wb') as new_file:
		new_file.write(downloaded_file)
	
	#file_info = bot.get_file(file_id)
	#bot.send_message(message.chat.id, file_info)
	#bot.send_photo(message.chat.id, open('barcode.png', 'rb'))

	#file = requests.get('https://api.telegram.org/file/bot{0}/{1}'.format(config.token, file_info.file_path))
	#bot.send_message(message.chat.id, img)"""


if __name__ == '__main__':
	bot.polling(none_stop=True)