import glob
import sys
from pathlib import Path

import telethon.utils
from telethon import TelegramClient
from telethon.tl.functions.channels import JoinChannelRequest

from Aniebots import LOGS, bot, tbot
from .Config import Config
from Aniebots.utils import load_module
from Aniebots.version import __mew__ as mewver

hl = Config.HANDLER
MEOW_PIC = Config.ALIVE_PIC or "https://telegra.ph/file/5d7a1a5d027e6c27d6de5.jpg"

# let's get the bot ready
async def mew_bot(bot_token):
    try:
        await bot.start(bot_token)
        bot.me = await bot.get_me()
        bot.uid = telethon.utils.get_peer_id(bot.me)
    except Exception as e:
        LOGS.error(f"ANIEBOTS_SESSION - {str(e)}")
        sys.exit()


# Meowbot starter...
if len(sys.argv) not in (1, 3, 4):
    bot.disconnect()
else:
    bot.tgbot = None
    try:
        if Config.BOT_USERNAME is not None:
            LOGS.info("Checking Telegram Bot Username...")
            bot.tgbot = TelegramClient(
                "BOT_TOKEN", api_id=Config.APP_ID, api_hash=Config.API_HASH
            ).start(bot_token=Config.BOT_TOKEN)
            LOGS.info("Checking Completed. Proceeding to next step...")
            LOGS.info("🔰 Starting Aniebots 🔰")
            bot.loop.run_until_complete(mew_bot(Config.BOT_USERNAME))
            LOGS.info("🔥 Aniebots Startup Completed 🔥")
        else:
            bot.start()
    except Exception as e:
        LOGS.error(f"BOT_TOKEN - {str(e)}")
        sys.exit()

# imports plugins...
path = "Aniebots/plugins/*.py"
files = glob.glob(path)
for name in files:
    with open(name) as f:
        path1 = Path(f.name)
        shortname = path1.stem
        load_module(shortname.replace(".py", ""))


# let the party begin...
LOGS.info("Starting Bot Mode !")
tbot.start()
LOGS.info("⚡ Your Aniebots Now Working ⚡")
LOGS.info(
    "Head to @Aniebotsupports for Updates. Also join chat group to get help regarding to Aniebots."
)

# that's life...
async def mew_is_on():
    try:
        if Config.LOGGER_ID != 0:
            await bot.send_file(
                Config.LOGGER_ID,
                MEOW_PIC,
                caption=f"#START \n\nDeployed 🄰🄽🄸🄴-🅄🅂🄴🅁🄱🄾🅃 Successfully\n\n**🄰🄽🄸🄴-🅄🅂🄴🅁🄱🄾🅃 - {mewver}**\n\nType `{hl}ping` or `{hl}alive` to check! \n\nJoin [🄰🄽🄸🄴-🅄🅂🄴🅁🄱🄾🅃 Channel](t.me/Aniebots) for Updates & [🄰🄽🄸🄴-🅄🅂🄴🅁🄱🄾🅃 Chat](t.me/Aniebotsupports) for any query regarding 🄰🄽🄸🄴-🅄🅂🄴🅁🄱🄾🅃",
            )
    except Exception as e:
        LOGS.info(str(e))

    # Join Aniebots Channel after deploying 🤐😅
    try:
        await bot(JoinChannelRequest("@Aniebots"))
    except BaseException:
        pass


# Why not come here and chat??
#    try:
#        await bot(JoinChannelRequest("@Aniebotsupports"))
#    except BaseException:
#        pass


bot.loop.create_task(mew_is_on())

if len(sys.argv) not in (1, 3, 4):
    bot.disconnect()
else:
    bot.tgbot = None
    bot.run_until_disconnected()

# Aniebot
