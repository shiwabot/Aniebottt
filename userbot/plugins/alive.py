# For @Aniebotsupports 
"""Check if your userbot is working."""
from datetime import datetime
from io import BytesIO

import requests
from PIL import Image

from userbot import ALIVE_NAME, CMD_HELP, Anieversion
from userbot.__init__ import StartTime
from Aniebot.utils import *
from userbot import Config

# ======CONSTANTS=========#
ALIVE_MSG = (
    Config.ALIVE_MSG
    if Config.ALIVE_MSG
    else "Hey! I'm alive. All systems online and functioning normally!"
)
ALV_PIC = Config.ALIVE_PIC if Config.ALIVE_PIC else None
Aniemoji = Config.CUSTOM_ALIVE_EMOJI if Config.CUSTOM_ALIVE_EMOJI else "**✵**"
if Config.SUDO_USERS:
    sudo = "Enabled"
else:
    sudo = "Disabled"
# ======CONSTANTS=========#


def get_readable_time(seconds: int) -> str:
    count = 0
    ping_time = ""
    time_list = []
    time_suffix_list = ["s", "m", "h", "days"]

    while count < 4:
        count += 1
        if count < 3:
            remainder, result = divmod(seconds, 60)
        else:
            remainder, result = divmod(seconds, 24)
        if seconds == 0 and remainder == 0:
            break
        time_list.append(int(result))
        seconds = int(remainder)

    for x in range(len(time_list)):
        time_list[x] = str(time_list[x]) + time_suffix_list[x]
    if len(time_list) == 4:
        ping_time += time_list.pop() + ", "

    time_list.reverse()
    ping_time += ":".join(time_list)

    return ping_time


DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else "@Aniebotsupports"


@bot.on(admin_cmd(pattern="alive"))
@bot.on(sudo_cmd(pattern="alive", allow_sudo=True))
async def amireallyalive(alive):
    start = datetime.now()
    myid = bot.uid
    """ For .alive command, check if the bot is running.  """
    end = datetime.now()
    (end - start).microseconds / 1000
    uptime = get_readable_time((time.time() - StartTime))
    if ALV_PIC:
        tele = f"**Welcome To Aniebot **\n\n"
        tele += f"`{CUSTOM_ALIVE}`\n\n"
        tele += (
            f"{Aniemoji} **Telethon version**: `1.17`\n{Aniemoji} **Python**: `3.8.3`\n"
        )
        tele += f"{Aniemoji} **Aniebots Version**: `{Anieversion}`\n"
        tele += f"{Aniemoji} **More Info**: @Aniebotsupports \n"
        tele += f"{Aniemoji} **Sudo** : `{sudo}`\n"
        tele += f"{Aniemoji} **Anie Uptime**: `{uptime}`\n"
        tele += f"{Aniemoji} **Database Status**: `All OK 👌!`\n"
        tele += (
            f"{Aniemoji} **My pro owner** : [{DEFAULTUSER}](tg://user?id={myid})\n\n"
        )
        tele += "    [✨ GitHub Repository ✨](https://github.com/Anieteam/Aniebots)"
        await alive.get_chat()
        await alive.delete()
        """ For .alive command, check if the bot is running.  """
        await borg.send_file(alive.chat_id, ALV_PIC, caption=tele, link_preview=False)
        await alive.delete()
        return
    req = requests.get("https://telegra.ph/file/28c979a7a36c344da3e07.jpg")
    req.raise_for_status()
    file = BytesIO(req.content)
    file.seek(0)
    img = Image.open(file)
    with BytesIO() as sticker:
        img.save(sticker, "webp")
        sticker.name = "sticker.webp"
        sticker.seek(0)
        await borg.send_message(
            alive.chat_id,
            f"**Welcome To Aniebot **\n\n"
            f"`{CUSTOM_ALIVE}`\n\n"
            f"{Aniemoji} **Telethon version**: `1.17`\n{Aniemoji} **Python**: `3.8.3`\n"
            f"{Aniemoji} **Aniebot Version**: `{Anieversion}`\n"
            f"{Aniemoji} **More Info**: @Aniebotsupports \n"
            f"{Aniemoji} **Sudo** : `{sudo}`\n"
            f"{Aniemoji} **Aniebots Uptime**: `{uptime}`\n"
            f"{Aniemoji} **Database Status**: `All OK 👌!`\n"
            f"{Aniemoji} **My pro owner** : [{DEFAULTUSER}](tg://user?id={myid})\n\n"
            "    [✨ GitHub Repository ✨](https://github.com/Anieteam/Aniebots)",
            link_preview=False,
        )
        await borg.send_file(alive.chat_id, file=sticker)
        await alive.delete()


CMD_HELP.update({"alive": "➟ `.alive`\nUse - Check if your bot is working."})
