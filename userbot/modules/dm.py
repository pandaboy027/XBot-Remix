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
    
    c = d.split(" ")#xixixi

    chat_id = c[0]
    try:  #dc hehe
        chat_id = int(chat_id)
    #koala 🐨🐨🐨
    except BaseException:#lerpelerpeler
        
        pass
  
    msg = ""
    masg = await dc.get_reply_message() #ghanta😒😒
    if dc.reply_to_msg_id:
        await userbot.send_message(chat_id, masg)
        await dc.edit("🐨Pesan Terkirim🐨")
    for i in c[1:]:
        msg += i + " "#impt by koala frm deviiluserbot 
    if msg == "":#kontol
        return
    try:
        await userbot.send_message(chat_id, msg)
        await dc.edit("🐨Pesan Terkirim🐨")
    except BaseException:#hilikintil💩💩
        await dc.edit(".dm (username) (text)")

CMD_HELP.update({
    "dm":
    "`.dm` [username] [text]\
\nUsage: mengirim pesan kepada pengguna memakai bot \
\
"
})
