# updated by madboy482
# updated by madboy482
# updated by madboy482
from telethon import events, Button, custom
from userbot import bot
from userbot import bot
# updated by madboy482
# updated by madboy482
# updated by madboy482
import os,re
from telethon.tl.custom import Button 
from telethon import events, errors, custom, functions
@bot.on(events.InlineQuery(pattern=r"repo"))
async def inline_id_handler(event: events.InlineQuery.Event):
 # updated by madboy482
 # updated by madboy482
 # updated by madboy482
 LEGENDX = event.builder
 X= [[custom.Button.inline("🔥 Cʟɪᴄᴋ Hᴇʀᴇ 🔥",data="obhai")]]
 query = event.text
 # updated by madboy482
 # updated by madboy482
 # updated by madboy482
 result = LEGENDX.article("UʟᴛʀᴀX",text="**Anie's Rᴇᴘᴏ, Dᴇᴘʟᴏʏ ᴀɴᴅ Sᴜᴘᴘᴏʀᴛ\n\n© @Aniebots**",buttons=X,link_preview=False)
 # updated by madboy482
 # updated by madboy482
 # updated by madboy482
 await event.answer([result])
@bot.on(events.callbackquery.CallbackQuery(data=re.compile(b"obhai")))
# updated by madboy482
# updated by madboy482
# updated by madboy482
async def callback_query_handler(event):
# inline by ANIETEAM, TEAMULTRAX
  await event.edit(text=f"**ANIE's Rᴇᴘᴏ, Dᴇᴘʟᴏʏ ᴀɴᴅ Gʀᴏᴜᴘ Lɪɴᴋ\n\n© @ANIEBOTS**",buttons=[
   # updated by madboy482
   # updated by madboy482
   # updated by madboy482
                [
                    Button.url(f"⚜️ Rᴇᴘᴏ ⚜️", url="https://github.com/Anieteam/Aniebots"),
                 # updated by madboy482
                 # updated by madboy482
                 # updated by madboy482
                    Button.url(f"🌚 Sᴜᴘᴘᴏʀᴛ Cʜᴀᴛ 🌝", url="https://t.me/Aniebotsupports")],
   # updated by madboy482
   # updated by madboy482
   # updated by madboy482
                    [Button.url(f"🔰 Dᴇᴘʟᴏʏ 🔰", url="https://dashboard.heroku.com/new?button-url=https%3A%2F%2Fgithub.com%2FAnieteam%2FHEROKU&template=https%3A%2F%2Fgithub.com%2FAnieteam%2FHEROKU"),
                     Button.url(f"💠 Sᴛʀɪɴɢ 💠", url="https://replit.com/@Denvilop/Aniebots#main.py"),
                ]
            ]
                   # updated by madboy482
                   # updated by madboy482
                   # updated by madboy482
                  )
