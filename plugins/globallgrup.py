"""
💐 Commands Available -
• `{i}gban <reply user/ username>`
• `{i}ungban`
    Ban/Unban pengguna secara global.
• `{i}gstat <reply to user/userid/username>`
   periksa apakah pengguna di gbanned atau tidak.
• `{i}listgban`
   list semua pengguna yang di gbanned.
• `{i}gmute <reply user/ username>`
• `{i}ungmute`
   Mute/UnMute pengguna secara global.
• `{i}gkick <reply user/ username>`
   kick pengguna secara global.
• `{i}gcast <Message>`
   kirimkan pesan ke semua grup secara global.
• `{i}gucast <Message>`
   kirimkan pesan ke semua pengguna di private chat mu secara global.
•`{i}gpromote <reply to user> <channel/group/all> <rank>`
    globally promote user where you are admin.
    You can also set where To promote only groups or only channels or in all.
    Like. `gpromote group boss` ~ it promote repied user in all groups.
    Or. `gpromote @username all sar` ~ it promote the users in all group and channel.
•`{i}gdemote`
    Same function as gpromote.
"""

import os

from telethon import events
from telethon.tl.functions.channels import EditAdminRequest
from telethon.tl.functions.contacts import BlockRequest, UnblockRequest
from telethon.tl.types import ChatAdminRights

from . import *

_gpromote_rights = ChatAdminRights(
    add_admins=False,
    invite_users=True,
    change_info=False,
    ban_users=True,
    delete_messages=True,
    pin_messages=True,
)

_gdemote_rights = ChatAdminRights(
    add_admins=False,
    invite_users=False,
    change_info=False,
    ban_users=False,
    delete_messages=False,
    pin_messages=False,
)


@ilhammansiz_cmd(
    pattern="gpromote ?(.*)",
)
async def _(e):
    if not e.out and not is_fullsudo(e.sender_id):
        return await eod(e, "`perintah ini dibatasi untuk anggota sudo.`")
    x = e.pattern_match.group(1)
    if not x:
        return await eod(e, "`Incorrect Format`")
    user = await e.get_reply_message()
    if user:
        ev = await eor(e, "`mempromosikan pengguna yang dibalas secara global...`")
        ok = e.text.split()
        key = "all"
        if len(ok) > 1:
            if ("group" in ok[1]) or ("channel" in ok[1]):
                key = ok[1]
        rank = "AdMin"
        if len(ok) > 2:
            rank = ok[2]
        c = 0
        if e.is_private:
            user.id = user.peer_id.user_id
        else:
            user.id = user.from_id.user_id
        async for x in petercordpanda_bot.iter_dialogs():
            if "group" in key.lower():
                if x.is_group:
                    try:
                        await petercordpanda_bot(
                            EditAdminRequest(
                                x.id,
                                user.id,
                                _gpromote_rights,
                                rank,
                            ),
                        )
                        c += 1
                    except BaseException:
                        pass
            elif "channel" in key.lower():
                if x.is_channel:
                    try:
                        await petercordpanda_bot(
                            EditAdminRequest(
                                x.id,
                                user.id,
                                _gpromote_rights,
                                rank,
                            ),
                        )
                        c += 1
                    except BaseException:
                        pass
            else:
                if x.is_group or x.is_channel:
                    try:
                        await petercordpanda_bot(
                            EditAdminRequest(
                                x.id,
                                user.id,
                                _gpromote_rights,
                                rank,
                            ),
                        )
                        c += 1
                    except Exception as er:
                        LOGS.info(er)
        return await eor(
            ev, f"mempromosikan pengguna yang dibalas dengan total : {c} {key} obrolan"
        )
    else:
        k = e.text.split()
        if not k[1]:
            return await eod(e, "`berikan username/id pengguna atau balas ke pengguna.")
        user = k[1]
        if user.isdigit():
            user = int(user)
        try:
            name = await petercordpanda_bot.get_entity(user)
        except BaseException:
            return await eod(e, f"`No User Found Regarding {user}`")
        ev = await eor(e, f"`mempromosikan {name.first_name} secara global...`")
        key = "all"
        if len(k) > 2:
            if ("group" in k[2]) or ("channel" in k[2]):
                key = k[2]
        rank = "AdMin"
        if len(k) > 3:
            rank = k[3]
        c = 0
        async for x in petercordpanda_bot.iter_dialogs():
            if "group" in key.lower():
                if x.is_group:
                    try:
                        await petercordpanda_bot(
                            EditAdminRequest(
                                x.id,
                                user,
                                _gpromote_rights,
                                rank,
                            ),
                        )
                        c += 1
                    except BaseException:
                        pass
            elif "channel" in key.lower():
                if x.is_channel:
                    try:
                        await ultroid_bot(
                            EditAdminRequest(
                                x.id,
                                user,
                                _gpromote_rights,
                                rank,
                            ),
                        )
                        c += 1
                    except BaseException:
                        pass
            else:
                if x.is_group or x.is_channel:
                    try:
                        await petercordpanda_bot(
                            EditAdminRequest(
                                x.id,
                                user,
                                _gpromote_rights,
                                rank,
                            ),
                        )
                        c += 1
                    except BaseException:
                        pass
        return await eor(
            ev,
            f"berhasil mempromosikan {name.first_name} dalam total : {c} {key} obrolan.",
        )


@ilhammansiz_cmd(
    pattern="gdemote ?(.*)",
)
async def _(e):
    if not e.out and not is_fullsudo(e.sender_id):
        return await eod(e, "`perintah ini dibatasi untuk anggota sudo.`")
    x = e.pattern_match.group(1)
    if not x:
        return await eod(e, "`Incorrect Format`")
    user = await e.get_reply_message()
    if user:
        if e.is_private:
            user.id = user.peer_id.user_id
        else:
            user.id = user.from_id.user_id
        ev = await eor(e, "`menurunkan pengguna yang dibalas secara global`")
        ok = e.text.split()
        key = "all"
        if len(ok) > 1:
            if ("group" in ok[1]) or ("channel" in ok[1]):
                key = ok[1]
        rank = "Not AdMin"
        c = 0
        async for x in petercordpanda_bot.iter_dialogs():
            if "group" in key.lower():
                if x.is_group:
                    try:
                        await petercordpanda_bot(
                            EditAdminRequest(
                                x.id,
                                user.id,
                                _gdemote_rights,
                                rank,
                            ),
                        )
                        c += 1
                    except BaseException:
                        pass
            elif "channel" in key.lower():
                if x.is_channel:
                    try:
                        await petercordpanda_bot(
                            EditAdminRequest(
                                x.id,
                                user.id,
                                _gdemote_rights,
                                rank,
                            ),
                        )
                        c += 1
                    except BaseException:
                        pass
            else:
                if x.is_group or x.is_channel:
                    try:
                        await petercordpanda_bot(
                            EditAdminRequest(
                                x.id,
                                user.id,
                                _gdemote_rights,
                                rank,
                            ),
                        )
                        c += 1
                    except BaseException:
                        pass
        return await eor(
            ev, f"menurunkan pengguna yang dibalas dalam total: {c} {key} obrolan"
        )
    else:
        k = e.text.split()
        if not k[1]:
            return await eod(e, "`berikan username/id atau balas ke pengguna.")
        user = k[1]
        if user.isdigit():
            user = int(user)
        try:
            name = await petercordpanda_bot.get_entity(user)
        except BaseException:
            return await eod(e, f"`No User Found Regarding {user}`")
        ev = await eor(e, f"`menurunkan {name.first_name} secara global...`")
        key = "all"
        if len(k) > 2:
            if ("group" in k[2]) or ("channel" in k[2]):
                key = k[2]
        rank = "Not AdMin"
        c = 0
        async for x in petercordpanda_bot.iter_dialogs():
            if "group" in key.lower():
                if x.is_group:
                    try:
                        await petercordpanda_bot(
                            EditAdminRequest(
                                x.id,
                                user,
                                _gdemote_rights,
                                rank,
                            ),
                        )
                        c += 1
                    except BaseException:
                        pass
            elif "channel" in key.lower():
                if x.is_channel:
                    try:
                        await petercordpanda_bot(
                            EditAdminRequest(
                                x.id,
                                user,
                                _gdemote_rights,
                                rank,
                            ),
                        )
                        c += 1
                    except BaseException:
                        pass
            else:
                if x.is_group or x.is_channel:
                    try:
                        await petercordpanda_bot(
                            EditAdminRequest(
                                x.id,
                                user,
                                _gdemote_rights,
                                rank,
                            ),
                        )
                        c += 1
                    except BaseException:
                        pass
        return await eor(
            ev,
            f"berhasil menurunkan {name.first_name} dalam total : {c} {key} obrolan.",
        )


@ilhammansiz_cmd(
    pattern="ungban ?(.*)",
)
async def _(e):
    xx = await eor(e, "`ungbanning...`")
    if e.reply_to_msg_id:
        userid = (await e.get_reply_message()).sender_id
    elif e.pattern_match.group(1):
        userid = await get_user_id(e.pattern_match.group(1))
    elif e.is_private:
        userid = (await e.get_chat()).id
    else:
        return await eod(xx, "`balas ke sebuah pesan atau berikan id nya.`", time=5)
    name = (await e.client.get_entity(userid)).first_name
    chats = 0
    if not is_gbanned(userid):
        return await eod(xx, "`pengguna tidak di gbanned.`", time=3)
    async for ggban in e.client.iter_dialogs():
        if ggban.is_group or ggban.is_channel:
            try:
                await e.client.edit_permissions(ggban.id, userid, view_messages=True)
                chats += 1
            except BaseException:
                pass
    try:
        ungban(userid)
        delete_gban_reason(userid)
        await e.client(UnblockRequest(int(userid)))
    except Exception as ex:
        return await eor(xx, str(ex))
    await xx.edit(
        f"`ungbanned` [{name}](tg://user?id={userid}) `di {chats} obrolan.\ndihapus dari gbanwatch.`",
    )


@ilhammansiz_cmd(
    pattern="gban ?(.*)",
)
async def _(e):
    if not e.out and not is_fullsudo(e.sender_id):
        return await eor(e, "`perintah ini dibatasi untuk anggota sudo.`")
    xx = await eor(e, "`gbanning...`")
    reason = ""
    if e.reply_to_msg_id:
        userid = (await e.get_reply_message()).sender_id
        try:
            reason = e.text.split(" ", maxsplit=1)[1]
        except IndexError:
            reason = ""
    elif e.pattern_match.group(1):
        usr = e.text.split(" ", maxsplit=2)[1]
        userid = await get_user_id(usr)
        try:
            reason = e.text.split(" ", maxsplit=2)[2]
        except IndexError:
            reason = ""
    elif e.is_private:
        userid = (await e.get_chat()).id
        try:
            reason = e.text.split(" ", maxsplit=1)[1]
        except IndexError:
            reason = ""
    else:
        return await eod(xx, "`balas ke sebuah pesan atau berikan id nya.`", tome=5)
    name = (await e.client.get_entity(userid)).first_name
    chats = 0
    if userid == petercordpanda_bot.uid:
        return await eod(
            xx, "`saya tidak bisa melakukan gban terhadap diri sendiri.`", time=3
        )
    if str(userid) in DEVLIST:
        return await eod(xx, "`saya tidak bisa gban developer saya.`", time=3)
    if is_gbanned(userid):
        return await eod(
            xx,
            "`pengguna sudah di gbanned dan ditambahkan ke gbanwatch.`",
            time=4,
        )
    async for ggban in e.client.iter_dialogs():
        if ggban.is_group or ggban.is_channel:
            try:
                await e.client.edit_permissions(ggban.id, userid, view_messages=False)
                chats += 1
            except BaseException:
                pass
    try:
        gban(userid)
        add_gban_reason(userid, reason)
        await e.client(BlockRequest(int(userid)))
    except Exception as ex:
        return await eor(xx, str(ex))
    gb_msg = f"**#Gbanned** [{name}](tg://user?id={userid}) `di {chats} obrolan dan ditambahkan ke gbanwatch!`"
    if reason != "":
        gb_msg += f"\n**Karena** - {reason}"
    await xx.edit(gb_msg)


@ilhammansiz_cmd(
    pattern="gcast ?(.*)",
)
async def gcast(event):
    if not event.out and not is_fullsudo(event.sender_id):
        return await eor(event, "`perintah ini dibatasi untuk anggota sudo.`")
    xx = event.pattern_match.group(1)
    if not xx:
        return eor(event, "`berikan sebuah pesan untuk global broadcast!`")
    tt = event.text
    msg = tt[6:]
    kk = await eor(event, "`melakukan broadcast secara global...`")
    er = 0
    done = 0
    async for x in petercordpanda_bot.iter_dialogs():
        if x.is_group:
            chat = x.id
            try:
                done += 1
                await petercordpanda_bot.send_message(chat, msg)
            except BaseException:
                er += 1
    await kk.edit(f"berhasil di {done} obrolan, gagal di {er} obrolan(s)")


@ilhammansiz_cmd(
    pattern="gucast ?(.*)",
)
async def gucast(event):
    if not event.out and not is_fullsudo(event.sender_id):
        return await eor(event, "`perintah ini dibatasi untuk anggota sudo.`")
    xx = event.pattern_match.group(1)
    if not xx:
        return eor(event, "`berikan sebuah pesan untuk global broadcast!`")
    tt = event.text
    msg = tt[7:]
    kk = await eor(event, "`melakukan global broadcast...`")
    er = 0
    done = 0
    async for x in petercordpanda_bot.iter_dialogs():
        if x.is_user and not x.entity.bot:
            chat = x.id
            try:
                done += 1
                await petercordpanda_bot.send_message(chat, msg)
            except BaseException:
                er += 1
    await kk.edit(f"berhasil di {done} obrolan, gagal di {er} obrolan(s)")


@ilhammansiz_cmd(
    pattern="gkick ?(.*)",
)
async def gkick(e):
    xx = await eor(e, "`gkicking...`")
    if e.reply_to_msg_id:
        userid = (await e.get_reply_message()).sender_id
    elif e.pattern_match.group(1):
        userid = await get_user_id(e.pattern_match.group(1))
    elif e.is_private:
        userid = (await e.get_chat()).id
    else:
        return await eod(xx, "`Reply to some msg or add their id.`", time=5)
    name = (await e.client.get_entity(userid)).first_name
    chats = 0
    if userid == petercordpanda_bot.uid:
        return await eod(xx, "`I can't gkick myself.`", time=3)
    if str(userid) in DEVLIST:
        return await eod(xx, "`I can't gkick my Developers.`", time=3)
    async for gkick in e.client.iter_dialogs():
        if gkick.is_group or gkick.is_channel:
            try:
                await petercordpanda_bot.kick_participant(gkick.id, userid)
                chats += 1
            except BaseException:
                pass
    await xx.edit(f"`Gkicked` [{name}](tg://user?id={userid}) `in {chats} chats.`")


@ilhammansiz_cmd(
    pattern="gmute ?(.*)",
)
async def _(e):
    if not e.out and not is_fullsudo(e.sender_id):
        return await eor(e, "`This Command Is Sudo Restricted.`")
    xx = await eor(e, "`Gmuting...`")
    if e.reply_to_msg_id:
        userid = (await e.get_reply_message()).sender_id
    elif e.pattern_match.group(1):
        userid = await get_user_id(e.pattern_match.group(1))
    elif e.is_private:
        userid = (await e.get_chat()).id
    else:
        return await eod(xx, "`Reply to some msg or add their id.`", tome=5)
    name = (await e.client.get_entity(userid)).first_name
    chats = 0
    if userid == petercordpanda_bot.uid:
        return await eod(xx, "`I can't gmute myself.`", time=3)
    if str(userid) in DEVLIST:
        return await eod(xx, "`I can't gmute my Developers.`", time=3)
    if is_gmuted(userid):
        return await eod(xx, "`User is already gmuted.`", time=4)
    async for onmute in e.client.iter_dialogs():
        if onmute.is_group:
            try:
                await e.client.edit_permissions(onmute.id, userid, send_messages=False)
                chats += 1
            except BaseException:
                pass
    gmute(userid)
    await xx.edit(f"`Gmuted` [{name}](tg://user?id={userid}) `in {chats} chats.`")


@ilhammansiz_cmd(
    pattern="ungmute ?(.*)",
)
async def _(e):
    xx = await eor(e, "`UnGmuting...`")
    if e.reply_to_msg_id:
        userid = (await e.get_reply_message()).sender_id
    elif e.pattern_match.group(1):
        userid = await get_user_id(e.pattern_match.group(1))
    elif e.is_private:
        userid = (await e.get_chat()).id
    else:
        return await eod(xx, "`Reply to some msg or add their id.`", time=5)
    name = (await e.client.get_entity(userid)).first_name
    chats = 0
    if not is_gmuted(userid):
        return await eod(xx, "`User is not gmuted.`", time=3)
    async for hurr in e.client.iter_dialogs():
        if hurr.is_group:
            try:
                await e.client.edit_permissions(hurr.id, userid, send_messages=True)
                chats += 1
            except BaseException:
                pass
    ungmute(userid)
    await xx.edit(f"`Ungmuted` [{name}](tg://user?id={userid}) `in {chats} chats.`")


@petercordpanda_bot.on(events.ChatAction)
async def _(e):
    if e.user_joined or e.added_by:
        user = await e.get_user()
        chat = await e.get_chat()
        if is_gbanned(str(user.id)):
            if chat.admin_rights:
                try:
                    await e.client.edit_permissions(
                        chat.id,
                        user.id,
                        view_messages=False,
                    )
                    reason = get_gban_reason(user.id)
                    gban_watch = f"#GBanned_User Joined.\n\n**User** - [{user.first_name}](tg://user?id={user.id})\n"
                    if reason is not None:
                        gban_watch += f"**Reason**: {reason}\n\n"
                    gban_watch += f"`User Banned.`"
                    await e.reply(gban_watch)
                except BaseException:
                    pass


@ilhammansiz_cmd(
    pattern="listgban",
)
async def list_gengbanned(event):
    users = gbanned_user()
    x = await eor(event, get_string("com_1"))
    msg = ""
    if not udB.get("GBAN"):
        return await x.edit("`You haven't GBanned anyone!`")
    for i in users:
        try:
            name = (await petercordpanda.get_entity(int(i))).first_name
        except BaseException:
            name = i
        msg += f"**User**: {name}\n"
        reason = get_gban_reason(i)
        if reason is not None or "":
            msg += f"**Reason**: {reason}\n\n"
        else:
            msg += "\n"
    gbanned_users = f"**List of users GBanned by {OWNER_NAME}**:\n\n{msg}"
    if len(gbanned_users) > 4096:
        f = open("gbanned.txt", "w")
        f.write(gbanned_users.replace("`", "").replace("*", ""))
        f.close()
        await x.reply(
            file="gbanned.txt",
            caption=f"List of users GBanned by [{OWNER_NAME}](tg://user?id={OWNER_ID})",
        )
        os.remove("gbanned.txt")
        await x.delete()
    else:
        await x.edit(gbanned_users)


@ilhammansiz_cmd(
    pattern="gstat ?(.*)",
)
async def gstat_(e):
    xx = await eor(e, get_string("com_1"))
    if e.is_private:
        userid = (await e.get_chat()).id
    elif e.reply_to_msg_id:
        userid = (await e.get_reply_message()).sender_id
    elif e.pattern_match.group(1):
        if (e.pattern_match.group(1)).isdigit():
            try:
                userid = (await e.client.get_entity(int(e.pattern_match.group(1)))).id
            except ValueError as err:
                return await eod(xx, f"{str(err)}", time=5)
        else:
            try:
                userid = (await e.client.get_entity(str(e.pattern_match.group(1)))).id
            except ValueError as err:
                return await eod(xx, f"{str(err)}", time=5)
    else:
        return await eod(xx, "`Reply to some msg or add their id.`", time=5)
    name = (await e.client.get_entity(userid)).first_name
    msg = "**" + name + " is "
    is_banned = is_gbanned(userid)
    reason = get_gban_reason(userid)
    if is_banned:
        msg += "Globally Banned"
        if reason:
            msg += f" with reason** `{reason}`"
        else:
            msg += ".**"
    else:
        msg += "not Globally Banned.**"
    await xx.edit(msg)
