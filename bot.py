# coding=utf-8

import telepot
import time
import random

TOKEN = "1930823211:AAGfu5Nm08lt396Apl6vNIpKGTFIY4OMxyA"

def handle(msg):
    content_type, chat_type, chat_id = telepot.glance(msg)
    if content_type == 'text':
            cmd = msg['text'].split("\n")
            if cmd[0] == '/start':
                bot.sendMessage(chat_id, "Hi, send me something; one item for line:")
            else:
                bot.sendMessage(chat_id, "That's my choice: " +  random.choice(cmd))

bot = telepot.Bot(TOKEN)
bot.message_loop(handle)

while 1:
    time.sleep(3)
