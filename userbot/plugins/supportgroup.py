"""Emoji
Available Commands:
.support
Credits to @pureindialover
"""

from telethon import events

import asyncio

from Aniebot.utils import admin_cmd

@bot.on(admin_cmd("Support"))
async def _(event):
    if event.fwd_from:
        return
    animation_interval = 0.1
    animation_ttl = range(0,36)
    #input_str = event.pattern_match.group(1)
   # if input_str == "support":
    await event.edit("for our support group")
    animation_chars = [
            "Click here",
            "[Deploy your own bot](https://github.com/Anieteam/Aniebots)"
         ]
            

    for i in animation_ttl:
        	
        await asyncio.sleep(animation_interval)
        await event.edit(animation_chars[i % 18])
