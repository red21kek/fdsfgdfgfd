from pyrogram import Client, filters
from pyrogram.errors import FloodWait
import time
from time import sleep

from time import sleep
from collections import defaultdict

app = Client("my_account")

from pyrogram import Client, filters
from pyrogram.errors import FloodWait
import time
from typing import Union
from time import sleep
import random
from time import sleep
from collections import defaultdict
from subprocess import check_output
from pyrogram.types import InputMediaPhoto, InputMediaVideo, InputMediaAudio
app = Client("my_account")

@app.on_message(filters.regex('за масон') & filters.me)
def ghoul_spam_handler(client, message):
    i = 10000
    while i > 0:
        try:
            
            client.send_message(message.chat.id, f'Слава Отцу! DEUS VULT! AVE MARIA! СМЕРТЬ СОДОМИТАМ! \n Слава Отцу! DEUS VULT! AVE MARIA! СМЕРТЬ СОДОМИТАМ!')
            app.send_sticker("-1001555594476", "CAACAgIAAxkBAAEFETtirHozEZGRXugNXBnlRx4mqf04OgACTBMAAmkm6EvdZsG93QtzZiQE")
        except FloodWait as e:
            sleep(e.x)

        i -= 7
        sleep(0.05)           
@app.on_message(filters.regex('цел') & filters.me)
def ghoul_spam_handler(client, message):
    i = 10000
    while i > 0:
        try:
            app.send_animation("-1001555594476", "85GG.gif", unsave=True)
        except FloodWait as e:
            sleep(e.x)

        i -= 7
        sleep(0.05)
app.run()
