import os
import telegram
from telegram.ext import Updater, CommandHandler
import numpy as np
import openai
import pandas as pd
import pickle
import tiktoken
import PIL
import io
import requests
from gtts import gTTS
from pydub import AudioSegment



MODEL = "text-davinci-003"
EMBEDDING_MODEL = "text-embedding-ada-002"
openai.api_key = 
MAX_TOKENS = 476
RANDOMNESS = 0

# --- init ---

TOKEN = "5607116930:AAFvxzihrrofZyfagOGJxvrnQxJTLCM2Xfc"

updater = Updater(TOKEN, use_context=True)
dispatcher = updater.dispatcher

# --- commands ---

def start(update, context):
    #print('text:', update.message.text)   # /start something
    #print('args:', context.args)          # ['something']
    pertanya= ''
    for item in context.args:
        pertanya = pertanya +" "+item
        #print(pertanya)
    if len(pertanya)>0:
        context.bot.send_message(chat_id=update.effective_chat.id,text=tanya(pertanya.lstrip()))
    else:
        context.bot.send_message(chat_id=update.effective_chat.id,text=tanya('jarvis apakah kamu siap?'))

def img(update, context):
    pertanya= ''
    for item in context.args:
        pertanya = pertanya +" "+item
    
    if len(pertanya)>0:
    
        response = openai.Image.create(
                    prompt=pertanya,
                    n=1,
                    size="1024x1024"
                    )
        url = response['data'][0]['url']
        #img = Image.open(url)

# save image in memory
        #img_bytes = io.BytesIO()
        #img.save(img_bytes, format="PNG")
        #img_bytes.seek(0)


        #files = {"photo": img_bytes}
        #python testele2.pyupdate.message.reply_text(url)
        context.bot.send_photo(chat_id=update.effective_chat.id,photo = url)
    else:
        pass

def suoro(update, context):
    pertanya= ''
    for item in context.args:
        pertanya = pertanya +" "+item
        #print(pertanya)
    if len(pertanya)>0:
        txt = tanya(pertanya.lstrip())
        tts = gTTS(txt, lang='id', tld='com.au')
        tts.save('jawab.mp3')
        suara = AudioSegment.from_mp3('jawab.mp3')
        suara.export('jawab.ogg',format='ogg')

        context.bot.send_audio(chat_id=update.effective_chat.id,audio=open('jawab.ogg', 'rb'))
    else:
        context.bot.send_message(chat_id=update.effective_chat.id,text=tanya('jarvis apakah kamu siap?'))
   

            
def tanya(pesan):
    prompt = str(pesan)

    masha = openai.Completion.create(
            model=MODEL,
            prompt=prompt,
            max_tokens=MAX_TOKENS,
            temperature=RANDOMNESS,
        )
    #print((masha.choices[0].text))
    return (masha.choices[0].text)


dispatcher.add_handler(CommandHandler('jarvis', start))
dispatcher.add_handler(CommandHandler('gambar', img))
dispatcher.add_handler(CommandHandler('jarvus', suoro))


# --- start ---


    
updater.start_polling()
updater.idle()