import html
from math import ceil
from re import compile

from telethon import Button, custom, functions
from telethon.errors.rpcerrorlist import UserNotParticipantError
from telethon.events import InlineQuery, callbackquery
from telethon.sync import custom
from telethon.tl.functions.channels import GetParticipantRequest
from telethon.tl.functions.messages import ExportChatInviteRequest
from telethon.tl.functions.users import GetFullUserRequest

from userbot import *
from userbot.cmdhelp import *
from Aniebot.utils import *
from userbot.Config import Config

Anie_row = Config.BUTTONS_IN_HELP
Anie_emoji = Config.EMOJI_IN_HELP
ALV_PIC = Config.ALIVE_PIC

PM_WARNS = {}
PREV_REPLY_MESSAGE = {}

mybot = Config.TG_BOT_USER_NAME_BF_HER
if mybot.startswith("@"):
    botname = mybot
else:
    botname = f"@{mybot}"
LOG_GP = Config.PRIVATE_GROUP_ID
mssge = (
    str(CUSTOM_PMPERMIT)
    if CUSTOM_PMPERMIT
    else "**You Have Trespassed To My Master's PM!\nDo not spam here, else you will be blocked automatically.**"
)

USER_BOT_WARN_ZERO = (
    "Enough Of Your Flooding In My Master's PM!! \n\n**🚫 Blocked and Reported**"
)

ANIE_FIRST = (
    "**🔥Ⱨҽყ ƚɦιʂ ιʂ Aniebot P͆M̾ Sêçürïty 🔥**\n\nThis is to inform you that "
    "{} is currently unavailable.\nThis is an automated message.\n\n"
    "{}\n\n**Please Choose Why You Are Here!!**"
)

alive_txt = """
**🔥 bot ιѕ σиℓιиє 🔥**
{}
**⚡ Anie 𝚂𝚝𝚊𝚝𝚞𝚜 ⚡**

**тєℓєтнσи :**  `{}`
**anie     :**  **{}**
**υρтιмє   :**  `{}`
**αвυѕє    :**  **{}**
**ѕυ∂σ     :**  **{}**
"""


def button(page, modules):
    Row = Anie_row

    modules = sorted([modul for modul in modules if not modul.startswith("_")])
    pairs = list(map(list, zip(modules[::2], modules[1::2])))
    if len(modules) % 2 == 1:
        pairs.append([modules[-1]])
    max_pages = ceil(len(pairs) / Row)
    pairs = [pairs[i : i + Row] for i in range(0, len(pairs), Row)]
    buttons = []
    for pairs in pairs[page]:
        buttons.append(
            [
                custom.Button.inline(
                    f"{Anie_emoji} " + pair + f" {Anie_emoji}",
                    data=f"Information[{page}]({pair})",
                )
                for pair in pairs
            ]
        )

    buttons.append(
        [
            custom.Button.inline(
                f"◀️ Back {Anie_emoji}",
                data=f"page({(max_pages - 1) if page == 0 else (page - 1)})",
            ),
            custom.Button.inline(f"• 🔙 •", data="close"),
            custom.Button.inline(
                f"{Anie_emoji} Next ▶️",
                data=f"page({0 if page == (max_pages - 1) else page + 1})",
            ),
        ]
    )
    return [max_pages, buttons]

    modules = CMD_HELP


if Config.TG_BOT_USER_NAME_BF_HER is not None and tgbot is not None:

    @tgbot.on(InlineQuery)  # pylint:disable=E0602
    async def inline_handler(event):
        builder = event.builder
        result = None
        query = event.text
        if event.query.user_id == bot.uid and query == "Aniebot_help":
            rev_text = query[::-1]
            veriler = button(0, sorted(CMD_HELP))
            apn = []
            for x in CMD_LIST.values():
                for y in x:
                    apn.append(y)
            result = await builder.article(
                f"Hey! Only use .help please",
                text=f"🇮🇳 **{DEFAULTUSER} **\n\n💐 __No.of Plugins__ : `{len(CMD_HELP)}` \n🌹 __Commands__ : `{len(apn)}`\n📍 __Page__ : 1/{veriler[0]}",
                buttons=veriler[1],
                link_preview=False,
            )
        elif event.query.user_id == bot.uid and query.startswith("fsub"):
            hunter = event.pattern_match.group(1)
            Meow = hunter.split("+")
            user = await bot.get_entity(int(Meow[0]))
            channel = await bot.get_entity(int(Meow[1]))
            msg = f"**👋 Welcome** [{user.first_name}](tg://user?id={user.id}), \n\n**📍 You need to Join** {channel.title} **to chat in this group.**"
            if not channel.username:
                link = (await bot(ExportChatInviteRequest(channel))).link
            else:
                link = "https://t.me/" + channel.username
            result = [
                await builder.article(
                    title="force_sub",
                    text=msg,
                    buttons=[
                        [Button.url(text="Channel", url=link)],
                        [custom.Button.inline("🔓 Unmute Me", data=unmute)],
                    ],
                )
            ]

        elif event.query.user_id == bot.uid and query == "alive":
            me_ow = alive_txt.format(
                Config.ALIVE_MSG, tel_ver, mew_ver, uptime, abuse_m, is_sudo
            )
            alv_btn = [
                [Button.url(f"{ANIE_USER}", f"tg://openmessage?user_id={ForGo10God}")],
                [
                    Button.url("My Channel", f"https://t.me/{my_channel}"),
                    Button.url("My Group", f"https://t.me/{my_group}"),
                ],
            ]
            if ALV_PIC and ALV_PIC.endswith((".jpg", ".png")):
                result = builder.photo(
                    ALV_PIC,
                    text=me_ow,
                    buttons=alv_btn,
                    link_preview=False,
                )
            elif ALV_PIC:
                result = builder.document(
                    ALV_PIC,
                    text=me_ow,
                    title="Anie Alive",
                    buttons=alv_btn,
                    link_preview=False,
                )
            else:
                result = builder.article(
                    text=me_ow,
                    title="Anie Alive",
                    buttons=alv_btn,
                    link_preview=False,
                )

        elif event.query.user_id == bot.uid and query == "pm_warn":
            Anie_w = Anie_FIRST.format(DEFAULTUSER, mssge)
            result = builder.photo(
                file=Anie_pic,
                text=Anie_w,
                buttons=[
                    [
                        custom.Button.inline("📌 Request 📌", data="req"),
                        custom.Button.inline("🌹 Chat 🌹", data="chat"),
                    ],
                    [custom.Button.inline("💥 Spam 💥", data="heheboi")],
                    [custom.Button.inline("Curious ✨", data="pmclick")],
                ],
            )

        elif event.query.user_id == bot.uid and query == "repo":
            result = builder.article(
                title="Repository",
                text=f"**✨ ʟɛɢɛռ∂ѕ σf Anie ✨**",
                buttons=[
                    [Button.url("📑 Repo 📑", "https://github.com/Anieteam/Aniebots")],
                    [
                        Button.url(
                            "🚀 Deploy 🚀",
                            "https://dashboard.heroku.com/new?button-url=https%3A%2F%2Fgithub.com%2FAnieteam%2FAniebots&template=https%3A%2F%2Fgithub.com%2FAnieteam%2FAniebots",
                        )
                    ],
                ],
            )

        elif query.startswith("http"):
            part = query.split(" ")
            result = builder.article(
                "File uploaded",
                text=f"**File uploaded successfully to {part[2]} site.\n\nUpload Time : {part[1][:3]} second\n[‏‏‎ ‎]({part[0]})",
                buttons=[[custom.Button.url("URL", part[0])]],
                link_preview=True,
            )

    @tgbot.on(callbackquery.CallbackQuery(data=compile(b"pmclick")))
    async def on_pm_click(event):
        if event.query.user_id == bot.uid:
            reply_pop_up_alert = "This is for Other Users..."
            await event.answer(reply_pop_up_alert, cache_time=0, alert=True)
        else:
            await event.edit(
                f"🌹 This is Anie ρɱ Security for {DEFAULTUSER}  to keep away unwanted retards from spamming PM..."
            )

    @tgbot.on(callbackquery.CallbackQuery(data=compile(b"req")))
    async def on_pm_click(event):
        if event.query.user_id == bot.uid:
            reply_pop_up_alert = "This is for other users!"
            await event.answer(reply_pop_up_alert, cache_time=0, alert=True)
        else:
            await event.edit(
                f"🌿 **Request Registered** \n\n{DEFAULTUSER}  will now decide to look for your request or not.\n😐 Till then wait patiently and don't spam!!"
            )
            target = await event.client(GetFullUserRequest(event.query.user_id))
            first_name = html.escape(target.user.first_name)
            ok = event.query.user_id
            if first_name is not None:
                first_name = first_name.replace("\u2060", "")
            tosend = f"**👀 Hey {DEFAULTUSER}  !!** \n\n⚜️ You Got A Request From [{first_name}](tg://user?id={ok}) In PM!!"
            await bot.send_message(LOG_GP, tosend)

    @tgbot.on(callbackquery.CallbackQuery(data=compile(b"chat")))
    async def on_pm_click(event):
        event.query.user_id
        if event.query.user_id == bot.uid:
            reply_pop_up_alert = "This is for other users!"
            await event.answer(reply_pop_up_alert, cache_time=0, alert=True)
        else:
            await event.edit(
                f"Ahh!! You here to do chit-chat!!\n\nPlease wait for {DEFAULTUSER}  to come. Till then keep patience and don't spam."
            )
            target = await event.client(GetFullUserRequest(event.query.user_id))
            ok = event.query.user_id
            first_name = html.escape(target.user.first_name)
            if first_name is not None:
                first_name = first_name.replace("\u2060", "")
            tosend = f"**👀 Hey {DEFAULTUSER}  !!** \n\n⚜️ You Got A PM from  [{first_name}](tg://user?id={ok})  for random chats!!"
            await bot.send_message(LOG_GP, tosend)

    @tgbot.on(callbackquery.CallbackQuery(data=compile(b"heheboi")))
    async def on_pm_click(event):
        if event.query.user_id == bot.uid:
            reply_pop_up_alert = "This is for other users!"
            await event.answer(reply_pop_up_alert, cache_time=0, alert=True)
        else:
            await event.edit(f"😏 **Jaa Na Bagad Bille\nDubara Mat dikh jaana**")
            await bot(functions.contacts.BlockRequest(event.query.user_id))
            target = await event.client(GetFullUserRequest(event.query.user_id))
            ok = event.query.user_id
            first_name = html.escape(target.user.first_name)
            if first_name is not None:
                first_name = first_name.replace("\u2060", "")
            first_name = html.escape(target.user.first_name)
            await bot.send_message(
                LOG_GP,
                f"**Blocked**  [{first_name}](tg://user?id={ok}) \n\nReason:- Spam",
            )

    @tgbot.on(callbackquery.CallbackQuery(data=compile(b"unmute")))
    async def on_pm_click(event):
        hunter = (event.data_match.group(1)).decode("UTF-8")
        Meow = hunter.split("+")
        if not event.sender_id == int(Meow[0]):
            return await event.answer("This Ain't For You!!", alert=True)
        try:
            await bot(GetParticipantRequest(int(Meow[1]), int(Meow[0])))
        except UserNotParticipantError:
            return await event.answer("You need to join the channel first.", alert=True)
        await bot.edit_permissions(
            event.chat_id, int(Meow[0]), send_message=True, until_date=None
        )
        await event.edit("Yay! You can Anie now !!")

    @tgbot.on(callbackquery.CallbackQuery(data=compile(b"reopen")))
    async def reopn(event):
        if event.query.user_id == bot.uid or event.query.user_id in Config.SUDO_USERS:
            current_page_number = 0
            simp = button(current_page_number, CMD_HELP)
            veriler = button(0, sorted(CMD_HELP))
            apn = []
            for x in CMD_LIST.values():
                for y in x:
                    apn.append(y)
            await event.edit(
                f"🇮🇳 **{DEFAULTUSER} **\n\n🌹 __No.of Plugins__ : `{len(CMD_HELP)}` \n🌷 __Commands__ : `{len(apn)}`\n📌 __Page__ : 1/{veriler[0]}",
                buttons=simp[1],
                link_preview=False,
            )
        else:
            reply_pop_up_alert = "Hoo gya aapka. Kabse Meow Meow dabae jaa rhe ho. Khudka Meow Banao agr aapko bhi chaiye to. © Aniebots ™"
            await event.answer(reply_pop_up_alert, cache_time=0, alert=True)

    @tgbot.on(callbackquery.CallbackQuery(data=compile(b"close")))
    async def on_plug_in_callback_query_handler(event):
        if event.query.user_id == bot.uid or event.query.user_id in Config.SUDO_USERS:
            veriler = custom.Button.inline(
                f"{Anie_emoji} Re-Open Menu {Anie_emoji}", data="reopen"
            )
            await event.edit(
                f"**🌹 Aniebots Mêñû Prõvîdêr ìs ñôw Çlösëd 🌹**\n\n**Bot Of :**  {DEFAULTUSER} \n\n        [©️ Aniebots ™️](t.me/Aniebotsupports)",
                buttons=veriler,
                link_preview=False,
            )
        else:
            reply_pop_up_alert = "Hoo gya aapka. Kabse tapar tapar dabae jaa rhe h. Khudka bna lo na agr chaiye to. © Aniebots ™"
            await event.answer(reply_pop_up_alert, cache_time=0, alert=True)

    @tgbot.on(callbackquery.CallbackQuery(data=compile(b"page\((.+?)\)")))
    async def page(event):
        page = int(event.data_match.group(1).decode("UTF-8"))
        veriler = button(page, CMD_HELP)
        apn = []
        for x in CMD_LIST.values():
            for y in x:
                apn.append(y)
        if event.query.user_id == bot.uid or event.query.user_id in Config.SUDO_USERS:
            await event.edit(
                f"🇮🇳 **{DEFAULTUSER} **\n\n🌹 __No.of Plugins__ : `{len(CMD_HELP)}`\n✨ __Commands__ : `{len(apn)}`\n📌 __Page__ : {page + 1}/{veriler[0]}",
                buttons=veriler[1],
                link_preview=False,
            )
        else:
            return await event.answer(
                "Hoo gya aapka. Kabse Meow Meow dabae jaa rhe ho. Khudka Meow bnalo na agr chaiye to. © Aniebots ™",
                cache_time=0,
                alert=True,
            )

    @tgbot.on(
        callbackquery.CallbackQuery(data=compile(b"Information\[(\d*)\]\((.*)\)"))
    )
    async def Information(event):
        page = int(event.data_match.group(1).decode("UTF-8"))
        commands = event.data_match.group(2).decode("UTF-8")
        try:
            buttons = [
                custom.Button.inline(
                    "✨ " + cmd[0] + " ✨", data=f"commands[{commands}[{page}]]({cmd[0]})"
                )
                for cmd in CMD_HELP_BOT[commands]["commands"].items()
            ]
        except KeyError:
            return await event.answer(
                "No Description is written for this plugin", cache_time=0, alert=True
            )

        buttons = [buttons[i : i + 2] for i in range(0, len(buttons), 2)]
        buttons.append(
            [
                custom.Button.inline(
                    f"{mew_emoji} Main Menu {mew_emoji}", data=f"page({page})"
                )
            ]
        )
        if event.query.user_id == bot.uid or event.query.user_id in Config.SUDO_USERS:
            await event.edit(
                f"**🖍️ File :**  `{commands}`\n**✴️ Number of commands :**  `{len(CMD_HELP_BOT[commands]['commands'])}`",
                buttons=buttons,
                link_preview=False,
            )
        else:
            return await event.answer(
                "Hoo gya aapka. Kabse tapar tapar dabae jaa rhe h. Khudka bna lo na agr chaiye to. © Aniebots ™",
                cache_time=0,
                alert=True,
            )

    @tgbot.on(
        callbackquery.CallbackQuery(data=compile(b"commands\[(.*)\[(\d*)\]\]\((.*)\)"))
    )
    async def commands(event):
        cmd = event.data_match.group(1).decode("UTF-8")
        page = int(event.data_match.group(2).decode("UTF-8"))
        commands = event.data_match.group(3).decode("UTF-8")
        result = f"**🖍️ File :**  `{cmd}`\n"
        if CMD_HELP_BOT[cmd]["info"]["info"] == "":
            if not CMD_HELP_BOT[cmd]["info"]["warning"] == "":
                result += (
                    f"**⚠️ Warning :**  {CMD_HELP_BOT[cmd]['info']['warning']}\n\n"
                )
        else:
            if not CMD_HELP_BOT[cmd]["info"]["warning"] == "":
                result += f"**⚠️ Warning :**  {CMD_HELP_BOT[cmd]['info']['warning']}\n"
            result += f"**♻️ Info :**  {CMD_HELP_BOT[cmd]['info']['info']}\n\n"
        command = CMD_HELP_BOT[cmd]["commands"][commands]
        if command["params"] is None:
            result += f"**❇️ Commands :**  `{COMMAND_HAND_LER[:1]}{command['command']}`\n"
        else:
            result += f"**❇️ Commands :**  `{COMMAND_HAND_LER[:1]}{command['command']} {command['params']}`\n"
        if command["example"] is None:
            result += f"**💟 Explanation :**  `{command['usage']}`\n\n"
        else:
            result += f"**💟 Explanation :**  `{command['usage']}`\n"
            result += f"**💞 For Example :**  `{COMMAND_HAND_LER[:1]}{command['example']}`\n\n"
        if event.query.user_id == bot.uid or event.query.user_id in Config.SUDO_USERS:
            await event.edit(
                result,
                buttons=[
                    custom.Button.inline(
                        f"{Anie_emoji} Return {Anie_emoji}",
                        data=f"Information[{page}]({cmd})",
                    )
                ],
                link_preview=False,
            )
        else:
            return await event.answer(
                "Hoo gya aapka. Kabse Meow Meow dabae jaa rhe h. Khudka Meow bnalo na agr chaiye to. © Aniebots ™",
                cache_time=0,
                alert=True,
            )


# Meowbot
