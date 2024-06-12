import telebot
from datetime import datetime
import random
from googlesearch import search
import requests              
import PyPDF2
from pypdf import PdfReader
from io import BytesIO
import os


bot = telebot.TeleBot("7127683041:AAGO9nVDbDDeeiLMD59ewIeo7D9GJY4SU9I")
channel_id = '@hackerpdfbotlog'

@bot.message_handler(commands=['info', 'explainbot'])
def expale(message):
  bot.send_message(message.chat.id, """
this explain how to use hacker pdf bot with screenshot

""")
  bot.send_photo(message.chat.id, "https://t.me/hackermain/4")



@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):

  bot.send_message(message.chat.id, f"""
*hi, @{message.from_user.username} 
this bot send learning PDF*

use:
```use
search: <you topis search > 
```
*🗒️🚨 note: use small charter use search:*

*owner : @MR_Hacker_000*""", parse_mode="Markdown")
  id = message.from_user.id                                             
  first_name = message.from_user.first_name
  last_name = message.from_user.last_name                               
  username = message.from_user.username
  bot.send_message(channel_id, f"""    
*@{username}
This started bot

id - {id}
name - {first_name}
last name - {last_name}
username - @{username}

🖕🖕🖕🖕🖕🖕🖕🖕🖕🖕🖕
*

""", parse_mode="Markdown")

@bot.message_handler(func=lambda message: True)
def handle_user_input(message):
    if message.text.startswith('search: '):
        global sech, j
        sech = message.text.split('search: ', 1)[1].strip()
        for j in search(f"{sech} filetype; pdf", num=3, stop=3, pause=2):


          global username, last_name, first_name, id
          id = message.from_user.id
          first_name = message.from_user.first_name
          last_name = message.from_user.last_name
          username = message.from_user.username
  
          
          try:
            bot.send_document(message.chat.id, j, caption=sech) 
            bot.send_message(channel_id, f"""
*doc log
id - {id}
name - {first_name}
last name - {last_name}
username - @{username}
search - {sech}
link - {j}  
*

""", parse_mode="Markdown")
          except:
               global text
               text = f"* this is pdf download  link :-*  [link]({j})"
               bot.send_message(message.chat.id, text, parse_mode="Markdown")
               # Send a message to the channel_id

               bot.send_message(channel_id, f"""
*text log
id - {id}
name - {first_name} 
last name - {last_name}
username - @{username}
search - {sech}
link - {j}

*

""", parse_mode="Markdown")


              

    else:
        bot.reply_to(message, "I'm sorry, I don't und	erstand that command.")




bot.infinity_polling()
