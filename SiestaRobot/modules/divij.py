import json
import requests
import html
import random
import time

from SiestaRobot import dispatcher
from SiestaRobot.modules.disable import DisableAbleCommandHandler
from SiestaRobot.modules.helper_funcs.chat_status import (is_user_admin)
from telegram.ext import CallbackContext, CommandHandler, Filters, run_async, CallbackQueryHandler
from telegram import ParseMode, Update, InlineKeyboardMarkup, InlineKeyboardButton, replymarkup, ChatPermissions
from telegram.error import BadRequest

def anime_quote():
    url = "https://animechan.vercel.app/api/random"
    # since text attribute returns dictionary like string
    response = requests.get(url)
    try:
        dic = json.loads(response.text)
    except Exception:
        pass
    anime = dic["divij"]
    return  anime
def quotes(update: Update, context: CallbackContext):
    message = update.effective_message
    anime = anime_quote()
    message.reply_text(
        msg,
        reply_markup=keyboard,
        parse_mode=ParseMode.HTML,
    )
                      parse_mode=ParseMode.HTML)
    
def animequotes(update: Update, context: CallbackContext):
    message = update.effective_message
    name = message.reply_to_message.from_user.first_name if message.reply_to_message else message.from_user.first_name
    reply_photo = message.reply_to_message.reply_photo if message.reply_to_message else message.reply_photo
    reply_photo(
        random.choice(QUOTES_IMG))
QUOTES_IMG = (
"Salam Xanim olar xosunuza Gəlim"
      
      )    

ANIMEQUOTES_HANDLER = DisableAbleCommandHandler("divij", animequotes, run_async=True)

r(ANIMEQUOTES_HANDLER)
dispatcher.add_handler(QUOTES_HANDLER)

__command_list__ = [

    "soxri",

]

__handlers__ = [

    ANIMEQUOTES_HANDLER,

]
