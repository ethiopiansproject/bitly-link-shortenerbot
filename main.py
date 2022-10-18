
import os
import telebot
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton
from telebot.util import user_link
import pyshorteners

bot = telebot.TeleBot(os.getenv('TgBOT_TOKEN'))

markup = InlineKeyboardMarkup()
b1 = InlineKeyboardButton('🦧Official Channel🦧',url='t.me/DevelopersPage')
b2 = InlineKeyboardButton('🦅Official Group🦅',url='t.me/DevelopersChat')
markup.add(b1,b2)

@bot.message_handler(commands=['start'])
def welcome_msg(message):
    user_info = message.from_user
    bot.send_message(message.chat.id,f'Hello dear {user_link(user_info)} welcome to bitly link shortener bot 😊\n send me any link i will make short for you using bitly.com\n Please join Channels and Group\n👇👇\t \t  \t \t \t 👇👇',reply_markup = markup,parse_mode="HTML")
  
@bot.message_handler(func = lambda msg: True)
def make_short(msg):
    link = msg.text
    shortener = pyshorteners.Shortener(api_key = os.getenv('BITLY_TOKEN'))
    link_shortener = shortener.bitly.short(link)
    print(link_shortener)
    bot.reply_to(msg,link_shortener,disable_web_page_preview=True)
    
bot.infinity_polling()
