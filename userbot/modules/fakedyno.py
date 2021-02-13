from time import sleep
from platform import uname
from userbot import ALIVE_NAME, CMD_HELP
from userbot.events import register

# ================= CONSTANT =================
DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else uname().node
# ============================================

@register(outgoing=True, pattern='^kntl(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    sleep(1)
    await typew.edit(f"**LU KONTOL**")
    sleep(3)
    await typew.edit("`KONTOL KONTOL KONTOL!!!`") 
    sleep(3)
    await typew.edit("`DASAR KEPALA KONTOL!!!`")
# Owner @Si_Dian

@register(outgoing=True, pattern='^G(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    sleep(1)
    await typew.edit(f"**JAKA SEMBUNG BAWA GOLOK**")
    sleep(3)
    await typew.edit("`NIMBRUNG GOBLOKK!!!`")
# Owner @Si_Dian


@register(outgoing=True, pattern='^.g(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    sleep(1)
    await typew.edit(f"**JAKA SEMBUNG BAWA GOLOK**")
    sleep(3)
    await typew.edit("`NIMBRUNG GOBLOKK!!!`")
# Owner @Si_Dian


@register(outgoing=True, pattern='^P(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    sleep(1)
    await typew.edit(f"**Hallo KIMAAKK SAYA {DEFAULTUSER}**")
    sleep(2)
    await typew.edit("`KONTOLLL.....`")
# Owner @Si_Dian


@register(outgoing=True, pattern='^p(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    sleep(1)
    await typew.edit(f"**Hallo KIMAKK SAYA {DEFAULTUSER}**")
    sleep(2)
    await typew.edit("`KONTOLLL.....`")
# Owner @Si_Dian


@register(outgoing=True, pattern='^.usange(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    sleep(1)
    await typew.edit("`Getting Information...`")
    sleep(1)
    await typew.edit("**Kampang Usage 🐨**:\n\n╭━━━━━━━━━━━━━━━━━━━━╮\n" f"-> `Penggunaan Kealayan ` **koalabot**:\n" f" •**0 jam - " f"0 menit - 0%**" "\n ◐━─━─━─━─━──━─━─━─━─━◐\n" "-> `Sisa Alay Bulan Ini`:\n" f" •**9999 jam - 9999 menit " f"- 100%**\n" "╰━━━━━━━━━━━━━━━━━━━━╯"
)
# Owner @Si_Dian

@register(outgoing=True, pattern='^.usange(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    sleep(1)
    await typew.edit("`Getting Information...`")
    sleep(1)
    await typew.edit("**Kampang Usage 🐨**:\n\n╭━━━━━━━━━━━━━━━━━━━━╮\n" f"-> `Penggunaan Kealayan ` **koalabot**:\n" f" •**0 jam - " f"0 menit - 0%**" "\n ◐━─━─━─━─━──━─━─━─━─━◐\n" "-> `Sisa Alay Bulan Ini`:\n" f" •**9999 jam - 9999 menit " f"- 100%**\n" "╰━━━━━━━━━━━━━━━━━━━━╯"
)
# Owner @Si_Dian


CMD_HELP.update({
    "fakedyno":
    "`.usange`\
\nUsage: tipu tipu anjeeeng.\
\n\n`L`\
\nUsage: Untuk Menjawab Salam."
})
