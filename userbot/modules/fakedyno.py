import codecs
import heroku3
import aiohttp
import math
import os
import requests
import asyncio

from userbot import (
    HEROKU_APP_NAME,
    HEROKU_API_KEY,
    BOTLOG,
    BOTLOG_CHATID,
    CMD_HELP)
from userbot.events import register



@register(outgoing=True, pattern=r"^.usange(?: |$)")
async def dyno_usage(dyno):
    """
        Get your account Dyno Usage
    """
    await dyno.edit("`Getting Information...`")
    useragent = (
        'Mozilla/5.0 (Linux; Android 10; SM-G975F) '
        'AppleWebKit/537.36 (KHTML, like Gecko) '
        'Chrome/81.0.4044.117 Mobile Safari/537.36'
    )
    user_id = Heroku.account().id
    headers = {
        'User-Agent': useragent,
        'Authorization': f'Bearer {HEROKU_API_KEY}',
        'Accept': 'application/vnd.heroku+json; version=3.account-quotas',
    }
    path = "/accounts/" + user_id + "/actions/get-quota"
    async with aiohttp.ClientSession() as session:
        async with session.get(heroku_api + path, headers=headers) as r:
            if r.status != 200:
                await dyno.client.send_message(
                    dyno.chat_id,
                    f"`{r.reason}`",
                    reply_to=dyno.id
                )
                await dyno.edit("`Can't get information...`")
                return False
            result = await r.json()
            quota = result['account_quota']
            quota_used = result['quota_used']

            """ - User Quota Limit and Used - """
            remaining_quota = quota - quota_used
            percentage = math.floor(remaining_quota / quota * 100)
            minutes_remaining = remaining_quota / 60
            hours = math.floor(minutes_remaining / 60)
            minutes = math.floor(minutes_remaining % 60)

            """ - User App Used Quota - """
            Apps = result['apps']
            for apps in Apps:
                if apps.get('app_uuid') == app.id:
                    AppQuotaUsed = apps.get('quota_used') / 60
                    AppPercentage = math.floor(
                        apps.get('quota_used') * 100 / quota)
                    break
            else:
                AppQuotaUsed = 0
                AppPercentage = 0

            AppHours = math.floor(AppQuotaUsed / 60)
            AppMinutes = math.floor(AppQuotaUsed % 60)

            await dyno.edit(
                "**Kampang Usage 🐨**:\n\n╭━━━━━━━━━━━━━━━━━━━━╮\n"
                f"-> `Penggunaan Kealayan `  **{app.name}**:\n"
                f"    •**0 jam - "
                f"0 menit  -  0%**"
                "\n ◐━─━─━─━─━──━─━─━─━─━◐\n"
                "-> `Sisa Alay Bulan Ini`:\n"
                f"    •**9999 jam - 9999 menit  "
                f"-  0%**\n"
                "╰━━━━━━━━━━━━━━━━━━━━╯"
            )
            await asyncio.sleep(20)
            await dyno.delete()
            return True

CMD_HELP.update({
    "fakedyno":
    "`.usange` [Fake Dyno]\
\nUsage: Ini cuma tipu tipu anjing"
})
