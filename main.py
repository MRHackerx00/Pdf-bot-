import telebot
from datetime import datetime
import random
from googlesearch import search
import requests              
import os


bot = telebot.TeleBot("7127683041:AAHwdupfSbVh2BRMPB1Sq1TaGfSzn-qrilw")
channel_id = '@hackerpdfbotlog'

user_id = 1853412532

def broadcast_message(message):
    try:
            bot.send_message(user_id, message)
            print(f"Message sent to {user_id}")
    except Exception as e:
            print(f"Failed to send message to {user_id}: {str(e)}")



@bot.message_handler(commands=['info', 'explainbot'])
def expale(message):
  bot.send_message(message.chat.id, """
this explain how to use hacker pdf bot with screenshot

""")
  bot.send_photo(message.chat.id, "https://t.me/hackermain/5")



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
    if message.text:
        global sech, j
        sech = message.text
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
        bot.reply_to(message, "I'm sorry")


#broadcast_message("bot is testing now ")
bot.infinity_polling()    
