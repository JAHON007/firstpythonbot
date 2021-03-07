import telebot
from PIL import Image, ImageFilter, ImageDraw, ImageFont
from PIL.ImageFilter import BLUR, CONTOUR, DETAIL, EDGE_ENHANCE, EDGE_ENHANCE_MORE, EMBOSS, FIND_EDGES, SMOOTH, SMOOTH_MORE, SHARPEN
bot = telebot.TeleBot("1217020105:AAGaGhpje3BXs_yacQVcu2PtlGriEk-PUkY")

@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'Salom '+str(message.from_user.first_name)+'\nMenga rasm yuboring va effektni tanlang')

@bot.message_handler(commands=['help'])
def help(message):
		bot.send_message(message.chat.id,f"""Assalomu alaykum hyrmatli foydalanuvchi!\n \n 
			help, ya\'ni **yordam** bo‘limi quyidagilardan iborat:
			\n/id ~ bu sizning telegramda id raqamingizni aniqlab beradi.
			\nBotdan foydalanish:
			\nBotga rasm yuboring va tugmalardan birini bosing.\n
			Shunda bot sizga yangi filterlangan surat yuboradi.\nBot yangilanib turiladi.""")
			    #=====================
@bot.message_handler(commands=['id'])
def id_know(message):
	    bot.send_message(message.chat.id,f'{message.chat.id}')
		    #=====================
# @bot.message_handler()
# def eco_message(message):
# 		if 'tentak' in message.text:
# 			bot.send_message(message.chat.id,"o‘zing tentak")
# 		# else:
# 		# 	bot.send_message(message.chat.id,message.text)


@bot.message_handler(content_types=['text', 'photo'])
def main(message):
    if(message.text != 'BLUR' and message.text != 'CONTOUR' and
    message.text != 'DETAIL' and message.text != 'EDGE_ENHANCE' and
    message.text != 'EDGE_ENHANCE_MORE' and message.text != 'EMBOSS' and
    message.text != 'EMBOSS' and message.text != 'FIND_EDGES' and
    message.text != 'SMOOTH' and message.text != 'SMOOTH_MORE' and
    message.text != 'SMOOTH_MORE' and message.text != 'SHARPEN'):
        fileID = message.photo[-1].file_id
        file_info = bot.get_file(fileID)
        image = bot.download_file(file_info.file_path)
        with open("image.png", 'wb') as new_file:
            new_file.write(image)
    keyboard = telebot.types.ReplyKeyboardMarkup(True, True)
    keyboard.row('BLUR', 'CONTOUR')
    keyboard.row('DETAIL', 'EDGE_ENHANCE')
    keyboard.row('EDGE_ENHANCE_MORE', 'EMBOSS')
    keyboard.row('FIND_EDGES', 'SMOOTH')
    keyboard.row('SMOOTH_MORE', 'SHARPEN')
    bot.send_message(message.chat.id, '✅❇️✅', reply_markup=keyboard)
    #======================
    if(message.text == 'BLUR'):        
        open_file = Image.open("image.png")
        img = open_file.filter(BLUR)
        img.save("out.png")
        bot.send_chat_action(message.chat.id, 'upload_photo')  
        bot.send_photo(message.chat.id, open("out.png", 'rb'), caption='@KIMGADIR_FOYDALI')
    #======================
    elif(message.text == 'CONTOUR'):        
        open_file = Image.open("image.png")
        img = open_file.filter(CONTOUR)
        img.save("out.png")
        bot.send_chat_action(message.chat.id, 'upload_photo')  
        bot.send_photo(message.chat.id, open("out.png", 'rb'), caption='@KIMGADIR_FOYDALI')
    #======================
    elif(message.text == 'DETAIL'):        
        open_file = Image.open("image.png")
        img = open_file.filter(DETAIL)
        img.save("out.png")
        bot.send_chat_action(message.chat.id, 'upload_photo')  
        bot.send_photo(message.chat.id, open("out.png", 'rb'), caption='@KIMGADIR_FOYDALI')
    #======================
    elif(message.text == 'EDGE_ENHANCE'):        
        open_file = Image.open("image.png")
        img = open_file.filter(EDGE_ENHANCE)
        img.save("out.png")
        bot.send_chat_action(message.chat.id, 'upload_photo')  
        bot.send_photo(message.chat.id, open("out.png", 'rb'), caption='@KIMGADIR_FOYDALI')
    #======================
    elif(message.text == 'EDGE_ENHANCE_MORE'):        
        open_file = Image.open("image.png")
        img = open_file.filter(EDGE_ENHANCE_MORE)
        img.save("out.png")
        bot.send_chat_action(message.chat.id, 'upload_photo')  
        bot.send_photo(message.chat.id, open("out.png", 'rb'), caption='@KIMGADIR_FOYDALI')
    #======================
    elif(message.text == 'EMBOSS'):        
        open_file = Image.open("image.png")
        img = open_file.filter(EMBOSS)
        img.save("out.png")
        bot.send_chat_action(message.chat.id, 'upload_photo')  
        bot.send_photo(message.chat.id, open("out.png", 'rb'), caption='@KIMGADIR_FOYDALI')
    #======================
    elif(message.text == 'FIND_EDGES'):        
        open_file = Image.open("image.png")
        img = open_file.filter(FIND_EDGES)
        img.save("out.png")
        bot.send_chat_action(message.chat.id, 'upload_photo')  
        bot.send_photo(message.chat.id, open("out.png", 'rb'), caption='@KIMGADIR_FOYDALI')
    #======================
    elif(message.text == 'SMOOTH'):        
        open_file = Image.open("image.png")
        img = open_file.filter(SMOOTH)
        img.save("out.png")
        bot.send_chat_action(message.chat.id, 'upload_photo')  
        bot.send_photo(message.chat.id, open("out.png", 'rb'), caption='@KIMGADIR_FOYDALI')
    #======================
    elif(message.text == 'SMOOTH_MORE'):        
        open_file = Image.open("image.png")
        img = open_file.filter(SMOOTH_MORE)
        img.save("out.png")
        bot.send_chat_action(message.chat.id, 'upload_photo')  
        bot.send_photo(message.chat.id, open("out.png", 'rb'), caption='@KIMGADIR_FOYDALI')
    #======================
    elif(message.text == 'SHARPEN'):        
        open_file = Image.open("image.png")
        img = open_file.filter(SHARPEN)
        img.save("out.png")
        bot.send_chat_action(message.chat.id, 'upload_photo')  
        bot.send_photo(message.chat.id, open("out.png", 'rb'), caption='@KIMGADIR_FOYDALI')
    #======================

# @bot.message_handler(commands=['help'])
# def help(message):
# 		bot.send_message(message.chat.id,f"""Assalomu alaykum hyrmatli foydalanuvchi!\n \n 
# 			help, ya\'ni **yordam** bo‘limi quyidagilardan iborat:
# 			\n/id ~ bu sizning telegramda id raqamingizni aniqlab beradi.
# 			\nBotdan foydalanish:
# 			\nBotga rasm yuboring va tugmalardan birini bosing.\n
# 			Shunda bot sizga yangi filterlangan surat yuboradi.\nBot yangilanib turiladi.""")
# 			    #=====================
# @bot.message_handler(commands=['id'])
# def id_know(message):
# 	    bot.send_message(message.chat.id,f'{message.chat.id}')
# 		    #=====================
# @bot.message_handler()
# def eco_message(message):
# 		if 'tentak' in message.text:
# 			bot.send_message(message.chat.id,"o‘zing tentak")
# 		else:
# 			bot.send_message(message.chat.id,message.text)


if __name__ == '__main__':
    bot.polling(none_stop=True)
  
