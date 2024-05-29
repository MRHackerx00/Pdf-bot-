import telebot
from googlesearch import search
import os


bot = telebot.TeleBot("7127683041:AAHki1ezesTJzqnDLRDCQXX-xFD_avrSRpY")
@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
 bot.reply_to(message.chat.id,"""
hi, this bot send learning PDF

use:
```
search: <you topis>
``
🗒️🚨 note: use small charter use search:

*owner : @MR_Hacker_000*""", parse_mode="Markdown")

@bot.message_handler(func=lambda message: True)
def handle_user_input(message):
    if message.text.startswith('search: '):
        sech = message.text.split('search: ', 1)[1].strip()
        for j in search(f"{sech} filetype; pdf", num=3, stop=3, pause=2):
#          text = f"* this is pdf download  link :-*  [link]({j})"
#          bot.send_message(message.chat.id, text , parse_mode="Markdown")
          try:
               bot.send_document(message.chat.id, j, caption=sech)
          except:
               text = f"* this is pdf download  link :-*  [link]({j})"
               bot.send_message(message.chat.id, text, parse_mode="Markdown")
    else:
        bot.reply_to(message, "I'm sorry, I don't understand that command.")

bot.infinity_polling()
