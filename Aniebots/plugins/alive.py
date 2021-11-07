from telethon.errors import ChatSendInlineForbiddenError as noin
from telethon.errors.rpcerrorlist import BotMethodInvalidError as dedbot

from Aniebots import *
from Aniebots.cmdhelp import CmdHelp

# -------------------------------------------------------------------------------

mew_pic = Config.ALIVE_PIC or "https://telegra.ph/file/5d7a1a5d027e6c27d6de5.jpg"
alive_c = f"__**😺😺🇦 🇳 🇮 🇪 ɨs օռʟɨռɛ😺😺**__\n\n"
alive_c += f"**━━━━━━━━━━━━━━━━━━━━**\n\n"
alive_c += f"╠⟪Øωηєя⟫╣  ⊱     (Aniebots)[t.me/d3nvil]\n"
alive_c += f"┏━━━━━━━━━━━━━━━━━━━\n"
alive_c += f"┣⧼• тεℓεтнση  ⊱  `[version](1.0)\n"
alive_c += f"┣⧼• 🄰🄽🄸🄴        ⊱  (Anie Userbot)[t.me/Aniebotsupports]\n"
alive_c += f"┣⧼• sυ∂σ           ⊱(false)[t.me/Aniebots]\n"
alive_c += f"┣⧼• cнαηηεℓ     ⊱  (update)[t.me/aniebots]\n"
alive_c += f"┣⧼• ℓιcεηsε     ⊱ (Anie license)[GitHub.com/Anieteam]\n"
alive_c += f"┣⧼• υρтιмε      ⊱ `{uptime}`\n"
alive_c += f"┗━━━━━━━━━━━━━━━━━━━\n"
# -------------------------------------------------------------------------------


@bot.on(mew_cmd(outgoing=True, pattern="alive$"))
@bot.on(sudo_cmd(pattern="alive$", allow_sudo=True))
async def up(Meow):
    if Meow.fwd_from:
        return
    await Meow.get_chat()
    await Meow.delete()
    await bot.send_file(Anie.chat_id, mew_pic, caption=alive_c)
    await Meow.delete()


msg = f"""
**✨ 🄰🄽🄸🄴 ιѕ σиℓιиє ✨**
{Config.ALIVE_MSG}
**🌹 🄰🄽🄸🄴 𝚂𝚝𝚊𝚝𝚞𝚜 🌹**
**тєℓєтнσи:**  `{version}`
**🄰🄽🄸🄴    :**  **{mew_ver}**
**υρтιмє    :**  `{uptime}`
**αвυѕє     :**  **{abuse_m}**
**ѕυ∂σ        :**  **{is_sudo}**
"""
botname = Config.BOT_USERNAME


@bot.on(mew_cmd(pattern="Anie$"))
@bot.on(sudo_cmd(pattern="Anie$", allow_sudo=True))
async def mew_a(event):
    try:
        Meow = await bot.inline_query(botname, "alive")
        await Meow[0].click(event.chat_id)
        if event.sender_id == ForGo10God:
            await event.delete()
    except (noin, dedbot):
        await eor(event, msg)


CmdHelp("alive").add_command(
    "alive", None, "Shows the Default Alive Message"
).add_command("Meow", None, "Shows Inline Alive Menu with more details.").add_warning(
    "✅ Harmless Module"
).add()
