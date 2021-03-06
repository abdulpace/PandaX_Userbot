"""
💐 Commands Available -
•`{i}addclean`
    Clean all Upcoming action msg in added chat like someone joined/left/pin etc.
•`{i}remclean`
    Remove chat from database.
•`{i}listclean`
   To get list of all chats where its activated.
"""

from PandaX_Userbot.functions.clean_db import *

from . import *


@ilhammansiz_cmd(pattern="addclean$", admins_only=True)
async def _(e):
    add_clean(e.chat_id)
    await eod(e, "Added Clean Action Setting For this Chat")
    async for x in petercordpanda_bot.iter_messages(e.chat_id, limit=3000):
        if x.action:
            await x.delete()


@ilhammansiz_cmd(pattern="remclean$")
async def _(e):
    rem_clean(e.chat_id)
    await eod(e, "Removed Clean Action Setting For this Chat")


@ilhammansiz_cmd(pattern="listclean$")
async def _(e):
    k = udB.get("CLEANCHAT")
    if k:
        k = k.split(" ")
        o = ""
        for x in k:
            try:
                title = (await petercordpanda_bot.get_entity(int(x))).title
            except BaseException:
                title = "`Invalid ID`"
            o += x + " " + title + "\n"
        await eor(e, o)
    else:
        await eod(e, "`No Chat Added`")


@petercordpanda_bot.on(events.ChatAction())
async def _(event):
    if is_clean_added(event.chat_id):
        try:
            await event.delete()
        except BaseException:
            pass
