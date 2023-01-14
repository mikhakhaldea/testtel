import os
import telegram
from telegram.ext import Updater, CommandHandler
import numpy as np
import openai
import pandas as pd
import pickle
import tiktoken

MODEL = "text-davinci-003"
EMBEDDING_MODEL = "text-embedding-ada-002"
openai.api_key = "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"
MAX_TOKENS = 476
RANDOMNESS = 0

# --- init ---

TOKEN = "5607116930:AAFvxzihrrofZyfagOGJxvrnQxJTLCM2Xfc"

updater = Updater(TOKEN, use_context=True)
dispatcher = updater.dispatcher

# --- commands ---

def start(update, context):
    print('text:', update.message.text)   # /start something
    print('args:', context.args)          # ['something']
    pertanya= ''
    for item in context.args:
        pertanya = pertanya +" "+item
    print(pertanya)
    if len(pertanya)>0:
        context.bot.send_message(chat_id=update.effective_chat.id,text=tanya(pertanya.lstrip()))
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
    print((masha.choices[0].text))
    return (masha.choices[0].text)

dispatcher.add_handler(CommandHandler('jarvis', start))

# --- start ---


    
updater.start_polling()
updater.idle()