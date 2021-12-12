# COPYRIGHT (C) 2021 BY LEGENDX22 AND PROBOYX

"""
(((((((((((((((((((((((@LEGENDX22)))))))))))))))))))))))))))
(((((((((((((((((((((((@LEGENDX22)))))))))))))))))))))))))))
(((((((((((((((((((((((@LEGENDX22)))))))))))))))))))))))))))
(((((((((((((((((((((((@LEGENDX22)))))))))))))))))))))))))))
                 MADE BY LEGENDX22 AND PROBOYX
                   CREDITS #TEAMLEGEND 
                PLEASE DON'T REMOVE CREDITS
"""


from telethon import events, Button, custom
import re, os
from userbot import bot
from userbot import Anietelethon
PHOTO = "https://telegra.ph/file/fe58623891803d36979f7.jpg"
@tgbot.on(events.InlineQuery(pattern="alive_x"))
async def awake(event):
  builder = event.builder
  aniex = event.sender.first_name
  DENVIL_PRO =  f"**__----Aniebot Status----__**\n"
  DENVIL_PRO += f"**ALL System ok\n\n"
  DENVIL_PRO += f"**➬ Telethon :**{Anietelethon}\n"
  DENVIL_PRO += f"**MY Master :**{aniex} ☺️\n\n"
  DENVIL_PRO += "f"**Full upgrade :**\n\n"
  DENVIL_PRO += f"**Anie :** 1.19.5 LATEST\n\n"
  DENVIL_PRO += f"**thanks for using me/n"
  BUTTON = [[Button.url("MASTER", "https://t.me/denvil_pro"), Button.url("DEVLOPER", "https://t.me/Denvil_pro")]]
  BUTTON += [[custom.Button.inline("REPOSITORYS", data="DENVIL_PRO")]]
  result = builder.photo(
                    PHOTO,
                    text=DENVIL_PRO,
                    buttons=BUTTON,
                    link_preview=False
                )
  await event.answer([result])




@tgbot.on(events.callbackquery.CallbackQuery(data=re.compile(b"DENVIL_PRO")))
async def callback_query_handler(event):
# inline by  LEGENDX22 And DENVIL🔥
  PROBOYX = [[Button.url("REPO-ANIE", "https://github.com/ANIETEAM/Aniebots"), Button.url("REPO-GROUP BOT", "https://github.com/Anieteam/AnieRobot")]]
  PROBOYX +=[[Button.url("DEPLOY-ANIE", "https://dashboard.heroku.com/new?button-url=https%3A%2F%2Fgithub.com%2FAnieteam%2FAniebots&template=https%3A%2F%2Fgithub.com%2FAnietEAM%2FAniebots%2FLE"), Button.url("DEPLOY-ANIE GROUP BOT", "https://dashboard.heroku.com/new?button-url=https%3A%2F%2Fgithub.com%2ANIETEAM%2FANIEROBOT&template=https%3A%2F%2Fgithub.com%2FANIETEAM%2FANIEROBOT")]]
  PROBOYX +=[[Button.url("TUTORIAL", "https://youtu.be/T9ojWwGYBtw"), Button.url("STRING-SESSION", "https://repl.it/@denvilop/Aniebots#main.py")]]
  PROBOYX +=[[Button.url("API_ID & HASH", "https://t.me/usetgxbot"), Button.url("REDIS", "https://redislabs.com")]]
  PROBOYX +=[[Button.url("SUPPORT CHANNEL", "https://t.me/ANIEBOTS"), Button.url("SUPPORT GROUP", "https://t.me/Aniebotsupports")]]
  PROBOYX +=[[custom.Button.inline("ALIVE", data="PROBOY")]]
  await event.edit(text=f"ALL DETAILS OF REPOS", buttons=PROBOYX)


@tgbot.on(events.callbackquery.CallbackQuery(data=re.compile(b"PROBOY")))
async def callback_query_handler(event):
  global PHOTO
  legendx = event.sender.first_name
# inline by LEGENDX22 🔥
  LEGENDX22 = f"**__----Aniebot Status----__**\n"
  LEGENDX22 += f"**ALL System ok:**\n\n"
  LEGENDX22 += f"**Anie os :** 3.8 LATEST\n\n"
  LEGENDX22 += f"**My master:**{legendx} ☺️\n\n"
  LEGENDX22 += f"**fully updated :**\n\n"
  LEGENDX22 += f"**telethon : 1.19.5 LATEST\n\n"
  LEGENDX22 += "THANKS FOR USING ME"
  BUTTONS = [[Button.url("MASTER", "https://t.me/DENVIL_PRO"), Button.url("DEVLOPER", "https://t.me/NOOBANON")]]
  BUTTONS += [[custom.Button.inline("REPOSITORYS", data="LEGENDX22")]]
  await event.edit(text=LEGENDX22, buttons=BUTTONS)

@bot.on(events.NewMessage(pattern=".alive", outgoing=True))
async def repo(event):
    if event.fwd_from:
        return
    ULTRAX = (await tgbot.get_me()).username
    response = await bot.inline_query(ULTRAX, "alive_x")
    await response[0].click(event.chat_id)
    await event.delete()
