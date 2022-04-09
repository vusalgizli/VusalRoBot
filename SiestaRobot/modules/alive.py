import os
import re
from platform import python_version as kontol
from telethon import events, Button
from telegram import __version__ as telever
from telethon import __version__ as tlhver
from pyrogram import __version__ as pyrover
from SiestaRobot.events import register
from SiestaRobot import telethn as tbot


PHOTO = "https://telegra.ph//file/e9be41d54fce7c2462c2c.mp4"

@register(pattern=("/alive"))
async def awake(event):
  TEXT = f"**Salam [{event.sender.first_name}](tg://user?id={event.sender.id}), Mən Fidan Robotam.** \n\n"
  TEXT += "💠 **Mən düzgün işləyirəm** \n\n"
  TEXT += f"💠 **Mənim Sahibim : [HUSEYN](https://t.me/HuseynH)** \n\n"
  TEXT += f"💠 **Kitabxana Versiyası :** `{telever}` \n\n"
  TEXT += f"💠 **Telefon Versiyası :** `{tlhver}` \n\n"
  TEXT += f"💠 **Pyrogram Versiyası :** `{pyrover}` \n\n"
  TEXT += "**Məni bura əlavə etdiyiniz üçün təşəkkürlər ❤️**"
  BUTTON = [[Button.url("Kanal", "https://t.me/Fidowunkanali"), Button.url("Qrupumuz", "https://t.me/FidaninDunyasi")]]
  await tbot.send_file(event.chat_id, PHOTO, caption=TEXT,  buttons=BUTTON)
