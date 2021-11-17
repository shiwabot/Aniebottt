from firebot import CMD_HELP
from Aniebot.utils import admin_cmd, sudo_cmd


@boy.on(sudo_cmd(pattern="ahelp ?(.*)", allow_sudo=True))
@bot.on(admin_cmd(pattern="ahelp ?(.*)"))
async def _(event):
    args = event.pattern_match.group(1).lower()
    if args:
        if args in CMD_HELP:
            await event.edit(f"Here is some help for the {CMD_HELP[args]}")
        else:
            await event.edit(
                f"Help string for {args} not found! Type `.help` to see valid module names."
            )
    else:
        string = ""
        for i in CMD_HELP.values():
            string += f"`{str(i[0])}`, "
        string = string[:-2]
        await event.edit(
            "Please specify which module you want help for!\n\n" f"{string}"
        )
