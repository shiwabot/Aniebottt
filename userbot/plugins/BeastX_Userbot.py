from . import *

tgbotusername = Var.TG_BOT_USER_NAME_BF_HER

from userbot import ALIVE_NAME, CMD_LIST, lang

from Aniebot.utils import admin_cmd

from userbot import 

@admin_cmd(pattern=".repo ?(.*)")

async def repohand(event):

    results = await beast.inline_query(tgbotusername,'repo')

    await results[0].click(event.chat_id)
