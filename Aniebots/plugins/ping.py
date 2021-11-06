import datetime

from Aniebots import *
from Aniebots.utils.decorators import mew_cmd, sudo_cmd
from Aniebots import CmdHelp


@bot.on(mew_cmd(pattern="ping$"))
@bot.on(sudo_cmd(pattern="ping$", allow_sudo=True))
async def pong(Meow):
    if Anie.fwd_from:
        return
    start = datetime.datetime.now()
    event = await eor(Anie, "`⊰ քɨռɢ ⊱´")
    end = datetime.datetime.now()
    ms = (end - start).microseconds / 1000
    await event.edit(
        f"•࿙𝖯ØᏁᎶ࿙•\n\n    🌺  `{ms}`\n    🌺  __**Oառҽʀ**__ **:**  {mew_mention}"
    )


CmdHelp("ping").add_command(
    "ping", None, "Checks the ping speed of your 🄰🄽🄸🄴-🅄🅂🄴🅁🄱🄾🅃"
).add_warning("✅ Harmless Module").add()

# Meowbot
