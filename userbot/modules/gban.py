#by:koala @mixiologist 
#copyright: @danish_00 dark cobra

from userbot import bot, CMD_HELP
from telethon.tl.functions.contacts import BlockRequest, UnblockRequest
from userbot.events import register
import html
from telethon import events
from telethon.tl.functions.photos import GetUserPhotosRequest
from telethon.tl.functions.users import GetFullUserRequest
from telethon.tl.types import MessageEntityMentionName


async def get_full_user(event):  
    args = event.pattern_match.group(1).split(':', 1)
    extra = None
    if event.reply_to_msg_id and not len(args) == 2:
        previous_message = await event.get_reply_message()
        user_obj = await event.client.get_entity(previous_message.sender_id)
        extra = event.pattern_match.group(1)
    elif len(args[0]) > 0:
        user = args[0]
        if len(args) == 2:
            extra = args[1]
        if user.isnumeric():
            user = int(user)
        if not user:
            await event.edit("`Itz not possible without an user ID`")
            return
        if event.message.entities is not None:
            probable_user_mention_entity = event.message.entities[0]
            if isinstance(probable_user_mention_entity,
                          MessageEntityMentionName):
                user_id = probable_user_mention_entity.user_id
                user_obj = await event.client.get_entity(user_id)
                return user_obj
        try:
            user_obj = await event.client.get_entity(user)
        except Exception as err:
            return await event.edit("Error... Please report at @Dark_cobra_support_group", str(err))           
    return user_obj, extra


async def get_user_from_id(user, event):
    if isinstance(user, str):
        user = int(user)
    try:
        user_obj = await event.client.get_entity(user)
    except (TypeError, ValueError) as err:
        await event.edit(str(err))
        return None
    return user_obj



@register(outgoing=True, pattern="^.gban(?: |$)(.*)")
async def gben(userbot):
    dc = userbot
    sender = await dc.get_sender()
    me = await dc.client.get_me()
    if not sender.id == me.id:
        dark = await dc.reply("Gbanning anak kontol nih !")
    else:
        dark = await dc.edit("Proses Gban jan maen jan maen.....")
    me = await userbot.client.get_me()
    await dark.edit(f"Trying to ban you globally..weit nd watch you nub nibba")
    my_mention = "[{}](tg://user?id={})".format(me.first_name, me.id)
    f"@{me.username}" if me.username else my_mention
    await userbot.get_chat()
    a = b = 0
    if userbot.is_private:
        user = userbot.chat
        reason = userbot.pattern_match.group(1)
    else:
        userbot.chat.title
    try:
        user, reason = await get_full_user(userbot)
    except:
        pass
    try:
        if not reason:
            reason = "Private"
    except:
        return await dark.edit(f"**Something W3NT Wrong 🤔**")
    if user:
        if user.id == 1289422521:
            return await dark.edit(
                f"**You nub nibba..I can't gben my creator..**"
            )
        try:
            from userbot.modules.sql_helper.gmute_sql import gmute
        except:
            pass
        try:
            await userbot.client(BlockRequest(user))
        except:
            pass
        testuserbot = [
            d.entity.id
            for d in await userbot.client.get_dialogs()
            if (d.is_group or d.is_channel)
        ]
        for i in testuserbot:
            try:
                await userbot.client.edit_permissions(i, user, view_messages=False)
                a += 1
                await dark.edit(f"**Globally banned suksess support Koala 🐨 Total Affected Chats **: `{a}`")
            except:
                b += 1
    else:
        await dark.edit(f"**Reply to a user you dumbo !!**")
    try:
        if gmute(user.id) is False:
            return await dark.edit(f"**Error! User already gbanned.**")
    except:
        pass
    return await dark.edit(
        f"**Globally banned Sukses Anjeng xixi [{user.first_name}](tg://user?id={user.id}) Affected Chats😏 : {a} **"
    )



@register(outgoing=True, pattern="^.ungban(?: |$)(.*)")
async def gunben(userbot):
    dc = userbot
    sender = await dc.get_sender()
    me = await dc.client.get_me()
    if not sender.id == me.id:
        dark = await dc.reply("`Wait Let Me ungban this nub nibba again😂`")
    else:
        dark = await dc.edit("Weit nd watch ! ")
    me = await userbot.client.get_me()
    await dark.edit(f"Trying To Ungban User !")
    my_mention = "[{}](tg://user?id={})".format(me.first_name, me.id)
    f"@{me.username}" if me.username else my_mention
    await userbot.get_chat()
    a = b = 0
    if userbot.is_private:
        user = userbot.chat
        reason = userbot.pattern_match.group(1)
    else:
        userbot.chat.title
    try:
        user, reason = await get_full_user(userbot)
    except:
        pass
    try:
        if not reason:
            reason = "Private"
    except:
        return await dark.edit("Someting Went Wrong 🤔")
    if user:
        if user.id == 1289422521:
            return await dark.edit("**You nub nibba..can't gban or ungban my creator... !**")
        try:
            from userbot.modules.sql_helper.gmute_sql import ungmute
        except:
            pass
        try:
            await userbot.client(UnblockRequest(user))
        except:
            pass
        testuserbot = [
            d.entity.id
            for d in await userbot.client.get_dialogs()
            if (d.is_group or d.is_channel)
        ]
        for i in testuserbot:
            try:
                await userbot.client.edit_permissions(i, user, send_messages=True)
                a += 1
                await dark.edit(f"**Ungbaning this nub nibba.. AFFECTED CHATS - {a} **")
            except:
                b += 1
    else:
        await dark.edit("**Reply to a user you dumbo**")
    try:
        if ungmute(user.id) is False:
            return await dark.edit("**Error! User already ungbanned.**")
    except:
        pass
    return await dark.edit(
        f"**Ungbanned this noon nibba..getting him another chance... ; USER - [{user.first_name}](tg://user?id={user.id}) CHATS : {a} **"
    )




CMD_HELP.update({
    "gban": "\
`.gban`\
\nUsage: Globally Ban users from all the Group Administrations bots where you are SUDO.\
\n\n`.ungban reason`\
\nUsage: Globally unBan users from all the Group Administrations bots where you are SUDO"
})
