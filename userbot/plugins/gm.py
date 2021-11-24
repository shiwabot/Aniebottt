from telethon import events
@bot.on(events.NewMessage(incoming=True, pattern=".gm"))
async def gm(event):
  await event.edit("Having a sweet morning, a cup of coffee, a day with your loved ones is what sets your “Good Morning” have a nice day!")
