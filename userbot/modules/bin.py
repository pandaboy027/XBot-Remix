
from telethon.errors.rpcerrorlist import YouBlockedUserError
from userbot import bot, CMD_HELP
from userbot.events import register
from asyncio.exceptions import TimeoutError
from userbot import bot import danish_00 as danish


@register(outgoing=True, pattern=r"^\.bin")
async def _(event):
    if event.fwd_from:
        return 
    danish = event.pattern_match.group(1)
    chat = "@Carol5_bot"
    await event.edit("mencari bin tunggu yaa njeeng 🐨...")
    async with event.client.conversation(chat) as conv:
          try:     
              response = conv.wait_event(events.NewMessage(incoming=True,from_users=1247032902))
              await event.client.send_message(chat, "/bin {}".format(danish))
              respond = await response 
          except YouBlockedUserError: 
              await event.reply("unblock si bot @Carol5_bot ")
              return
          if respond.text.startswith(" "):
             await event.edit("bot nya meninggoy beroh hihihi 😂😂")
          else: 
             
             await event.client.send_message(event.chat_id, respond.message)
    await bot(functions.messages.DeleteHistoryRequest(peer=chat, max_id=0))
    await event.delete()
    
@register(outgoing=True, pattern=r"^\.vbv")
async def _(event):
    if event.fwd_from:
        return 
    
    danish = event.pattern_match.group(1)
    chat = "@Carol5_bot"
    await event.edit("Connecting...")
    async with event.client.conversation(chat) as conv:
          try:     
              response = conv.wait_event(events.NewMessage(incoming=True,from_users=1247032902))
              await event.client.send_message(chat, "/vbv {}".format(danish))
              respond = await response 
          except YouBlockedUserError: 
              await event.reply("unblock si bot @Carol5_bot ")
              return
          if respond.text.startswith(" "):
             await event.edit("bot nya meninggoy beroh hihihi 😂😂")
          else: 
              
             await event.client.send_message(event.chat_id, respond.message)
    await bot(functions.messages.DeleteHistoryRequest(peer=chat, max_id=0))
    await event.delete()
    
@register(outgoing=True, pattern=r"^\.key")
async def _(event):
    if event.fwd_from:
        return 
    
    danish = event.pattern_match.group(1)
    chat = "@Carol5_bot"
    await event.edit("Connecting...")
    async with event.client.conversation(chat) as conv:
          try:     
              response = conv.wait_event(events.NewMessage(incoming=True,from_users=1247032902))
              await event.client.send_message(chat, "/key {}".format(danish))
              response = await response 
          except YouBlockedUserError: 
              await event.reply("Boss! Please Unblock @Carol5_bot ")
              return
          if response.text.startswith(" "):
             await event.edit("That bot is dead bro now this cmd is useless 😂😂")
          else: 
             await event.client.send_message(event.chat_id, respond.message)
    await bot(functions.messages.DeleteHistoryRequest(peer=chat, max_id=0))
    await event.delete()
  
@register(outgoing=True, pattern=r"^\.iban")
async def _(event):
    if event.fwd_from:
        return 
    
    danish = event.pattern_match.group(1)
    chat = "@Carol5_bot"
    await event.edit("Connecting...")
    async with event.client.conversation(chat) as conv:
          try:     
              response = conv.wait_event(events.NewMessage(incoming=True,from_users=1247032902))
              await event.client.send_message(chat, "/iban {}".format(danish))
              response = await response 
          except YouBlockedUserError: 
              await event.reply("unblock si bot @Carol5_bot ")
              return
          if response.text.startswith(" "):
             await event.edit("bot nya meninggoy beroh hihihi 😂😂")
          else: 
             await event.client.send_message(event.chat_id, respond.message)
    await bot(functions.messages.DeleteHistoryRequest(peer=chat, max_id=0))
    await event.delete()


CMD_HELP.update(
    {
        "binner": ">`.bin`"
        "\nGet Untuk bin cc asu"
        "\n\n>`.vbv`"
        "\nUsage: Ngajakin vcs kalik yaa."
        "\n\n>`.key`"
        "\nUsage: artinya kunci tololl."
        "\n\n>`.iban`"
        "\nUsage: buat banned mungkin ya kali."."
})
