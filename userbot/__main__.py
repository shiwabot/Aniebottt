from userbot import bot
from sys import argv
import sys
from telethon.errors.rpcerrorlist import PhoneNumberInvalidError
import os
from telethon import TelegramClient
from var import Var
from userbot.Config import Config
from telethon.tl.functions.channels import InviteToChannelRequest, JoinChannelRequest
from userbot.utils import load_module, start_assistant
from userbot import LOAD_PLUG, LOGS, LEGENDversion
from pathlib import Path
import asyncio
import telethon.utils
os.system("pip install -U telethon")

l2= Config.SUDO_COMMAND_HAND_LER
LEGEND_PIC = Config.ALIVE_PIC or "https://telegra.ph/file/75e1eda1498620f0030ea.jpg"
l1 = Config.COMMAND_HAND_LER


LOAD_USERBOT = os.environ.get("LOAD_USERBOT", True)
LOAD_ASSISTANT = os.environ.get("LOAD_ASSISTANT", True)    

async def add_bot(bot_token):
    try:
        await bot.start(bot_token)
        bot.me = await bot.get_me()
        bot.uid = telethon.utils.get_peer_id(bot.me)
    except Exception as e:
        print(f"LEGEND_STRING - {str(e)}")
        sys.exit()
        
        
if len(sys.argv) not in (1, 3, 4):
    bot.disconnect()
else:
    bot.tgbot = None
    if Var.BOT_USERNAME is not None:
        print("Initiating Inline Bot")
        bot.tgbot = TelegramClient(
            "BOT_TOKEN",
            api_id=Var.APP_ID,
            api_hash=Var.API_HASH
        ).start(bot_token=Var.BOT_TOKEN)
        print("Initialisation finished with no errors")
        print("Starting Userbot")
        bot.loop.run_until_complete(add_bot(Var.BOT_USERNAME))
        print("Startup Completed")
    else:
        bot.start()


import glob
path = 'userbot/plugins/*.py'
files = glob.glob(path)
for name in files:
    with open(name) as f:
        path1 = Path(f.name)
        shortname = path1.stem
        load_module(shortname.replace(".py", ""))

if LOAD_ASSISTANT == True:
    path = "userbot/plugins/assistant/*.py"
    files = glob.glob(path)
    for name in files:
        with open(name) as f:
            path1 = Path(f.name)
            shortname = path1.stem
            try:
                start_assistant(shortname.replace(".py", ""))
            except Exception as er:
                print(er)

print(f""" B O T 🔱』➙𖤍࿐ IS ON!!! Anie VERSION :- {anieversion}
TYPE :- " .gpromote @Denvil_pro " OR .Anie OR .ping CHECK IF I'M ON!
╔════❰ANIEBOT❱═❍⊱❁۪۪
║┣⪼ OWNER - Anie
║┣⪼{LEGEND_PIC}
║┣⪼ CREATOR -@Denvil_pro
║┣⪼ TELETHON - 1.2.0
║┣⪼ ✨ 『🔱ANIE 🔱』𝐔𝐬𝐞𝐫𝐛𝐨𝐭✨
║╰━━━━━━━━━━━━━━━➣
╚══════════════════❍⊱""")

async def legend_is_on():
    try:
        if Config.LOGGER_ID != 0:
            await bot.send_file(
                Config.LOGGER_ID,
                LEGEND_PIC,
                caption=f"#START \n\nDeployed ANIEBOT Successfully\n\n**ANIEBOT- {anieversion}**\n\nType `{l1}op` or `{l1}alive` to check! \n\nJoin [AnieBot Channel](t.me/Aniebots) for Updates & [AnieBot Chat](t.me/Aniebotsupports) for any query regarding AnieBot",
            )
    except Exception as e:
        print(str(e))

# Join anieBot Channel after deploying 🤐😅
    try:
        await bot(JoinChannelRequest("@Aniebots"))
    except BaseException:
        pass

    try:
        await bot(JoinChannelRequest("@Aniebots"))
    except BaseException:
         pass


bot.loop.create_task(legend_is_on())

if len(sys.argv) not in (1, 3, 4):
    bot.disconnect()
else:
    bot.run_until_disconnected()
