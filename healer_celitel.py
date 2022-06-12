from pyrogram import Client, filters
from pyrogram.errors import FloodWait
import time
from time import sleep

from time import sleep
from collections import defaultdict

app = Client("my_account")

@app.on_message(filters.regex('я за целителя') & filters.me)
def ghoul_spam_handler(client, message):
    i = 10000
    while i > 0:
        try:
            #привет если хочется кинуть гифку надо будет подумать
            #app.send_video(" тут id чата скину во время рейда ", "твоя гифка которую надо скачать))")
            #крч тут тоже самое
            #app.send_sticker("id тоже кину", "@idstickerbot боту кинешь стикер и н тебе отправит ")
            app.send_video("-1001715091530", "85GG.gif")
            app.send_sticker("-1001715091530", "CAACAgQAAxkBAAEFBVxipjnGczEMrvxfIvx8KWew79C-5wAC3QkAAjANOVOxYze4AAFC2rckBA")
            client.send_message(message.chat.id, f'привет от целителя \n привет от целителя')
        except FloodWait as e:
            sleep(e.x)

        i -= 7
        sleep(0.05) 
app.run()
