import os
import re
from platform import python_version as kontol
from telethon import events, Button
from telegram import __version__ as telever
from telethon import __version__ as tlhver
from pyrogram import __version__ as pyrover
from EmikoRobot.events import register
from EmikoRobot import telethn as tbot


PHOTO = "https://telegra.ph/file/719c7766b1dbfe2666d39.jpg"

@register(pattern=("/alive"))
async def awake(event):
  TEXT = f"**👋Salma' [{event.sender.first_name}](tg://user?id={event.sender.id}), I'm Osmani Robot.** \n\n"
  TEXT += "🔥 **I'm Working Properly** \n\n"
  TEXT += f"🔥 **My Master : [Ribaj](https://t.me/meribaj)** \n\n"
  TEXT += f"💧 **Library Version :** `{telever}` \n\n"
  TEXT += f"💧 **Telethon Version :** `{tlhver}` \n\n"
  TEXT += f"✨ **Pyrogram Version :** `{pyrover}` \n\n"
  TEXT += "**Thanks For Adding Me Here ❤️**"
  BUTTON = [[Button.url("Help", "https://t.me/Mosia_Mk_Bot?start=help"), Button.url("Support", "https://t.me/osmanigroupbot")]]
  await tbot.send_file(event.chat_id, PHOTO, caption=TEXT,  buttons=BUTTON)
