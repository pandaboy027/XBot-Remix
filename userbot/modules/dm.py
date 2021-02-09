#by @mixiologist koala
import os
import re
from telethon import *
from userbot import bot
from userbot.events import register
from userbot import CMD_HELP
#Imprt by koala from deviluserbot 
@register(outgoing=True, pattern="^.dm(?: |$)(.*)")
async def _(dc):
 
     d = dc.pattern_match.group(1)
    
    

    
        pass
  
    msg = ""
    masg = await dc.get_reply_message() #ghanta😒😒
    if dc.reply_to_msg_id:
        await userbot.send_message(chat_id, masg)
        await dc.edit("⚜️Message Delivered! Sar⚜️")
    for i in c[1:]:
        msg += i + " "#Fixed by @deviluserbot 
    if msg == "":#hoho
        return
    try:
        await userbot.send_message(chat_id, msg)
        await dc.edit("⚜️Message Delivered!⚜️")
    except BaseException:#hmmmmmmmmm🤔🤔
        await dc.edit(".dm (username) (text)")

CMD_HELP.update({
    "dm":
    "`.dm` [username] [text]\
\nUsage: mengirim pesan kepada pengguna memakai bot \
\
"
})
