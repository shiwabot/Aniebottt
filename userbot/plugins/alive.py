from userbot import ALIVE_NAME
from userbot.utils import admin_cmd

name = str(ALIVE_NAME)
ANIEBOT_IS_ALIVE = (
    "**Apun Zinda He Sarr ^.^** \n`🇮🇳BOT Status : ` **☣Hot**\n\n"
    f"`My peru owner`: {name}\n\n"
    "`ANIEBOT Bot Version:` **3.8.7**\n`Python:` **3.8.5**\n"
    "`Database Status:` **😀ALL OK**\n\n`Always with you, my master!\n`"
    "**Bot Creator:** [🇮🇳DENVIL](t.me/D3NVIL)\n"
    "**Co-Owner:** [🇮🇳Anon](t.me/Noobanon)\n\n"
    "     [🇮🇳Deploy This Aniebot🇮🇳](https://github.com/Anieteam/Aniebots)"
)


@borg.on(admin_cmd(pattern="alive"))
async def amireallyalive(alive):
    chat = await alive.get_chat()
    await alive.delete()
    await borg.send_message(chat, ANIEBOT_IS_ALIVE, link_preview=False)
