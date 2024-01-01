from pyrogram import Client, filters
from pyrogram.errors import FloodWait
import asyncio
import datetime
import pytz
import os

app = Client(
    name = "botstatus_pratheek",
    api_id = int(os.environ["API_ID"]),
    api_hash = os.environ["API_HASH"],
    session_string = os.environ["SESSION_STRING"]
)
TIME_ZONE = os.environ["TIME_ZONE"]
BOT_LIST = [i.strip() for i in os.environ.get("BOT_LIST").split(' ')]
CHANNEL_OR_GROUP_ID = int(os.environ["CHANNEL_OR_GROUP_ID"])
MESSAGE_ID = int(os.environ["MESSAGE_ID"])
BOT_ADMIN_IDS = [int(i.strip()) for i in os.environ.get("BOT_ADMIN_IDS").split(' ')]

async def main_FilmySpot_Movies():
    async with app:
            while True:
                print("Checking...")
                FilmySpot = f"📊 | 𝗟𝗜𝗩𝗘 𝗕𝗢𝗧 𝗦𝗧𝗔𝗧𝗨𝗦"
                for bot in BOT_LIST:
                    try:
                        yyy_pratheek = await app.send_message(bot, "/start")
                        aaa = yyy_pratheek.id
                        await asyncio.sleep(10)
                        zzz_pratheek = app.get_chat_history(bot, limit = 1)
                        async for ccc in zzz_pratheek:
                            bbb = ccc.id
                        if aaa == bbb:
                            FilmySpot += f"\n\n🤖  @{bot}\n        └ **🅳︎🅾️︎🆆︎🅽︎** ❌"
                            for bot_admin_id in BOT_ADMIN_IDS:
                                try:
                                    await app.send_message(int(bot_admin_id), f"🚨 **Beep! Beep!! @{bot} is down** ❌")
                                except Exception:
                                    pass
                            await app.read_chat_history(bot)
                        else:
                            FilmySpot += f"\n\n🤖  @{bot}\n        └ **🅰️︎🅻︎🅸︎🆅︎🅴︎** ✅"
                            await app.read_chat_history(bot)
                    except FloodWait as e:
                        await asyncio.sleep(e.x)            
                time = datetime.datetime.now(pytz.timezone(f"{TIME_ZONE}"))
                last_update = time.strftime(f"%d %b %Y at %I:%M %p")
                FilmySpot += f"\n\n✔️ 𝐋𝐚𝐬𝐭 𝐜𝐡𝐞𝐜𝐤𝐞𝐝 𝐨𝐧: {last_update} ({TIME_ZONE})\n\n**♻️ 𝐑𝐞𝐟𝐫𝐞𝐬𝐡𝐞𝐬 𝐚𝐮𝐭𝐨𝐦𝐚𝐭𝐢𝐜𝐚𝐥𝐥𝐲: 𝐏𝐨𝐰𝐞𝐫𝐞𝐝 𝐁𝐲 𝐅𝐢𝐥𝐦𝐲𝐒𝐩𝐨𝐭 𝐌𝐨𝐯𝐢𝐞𝐬**"
                await app.edit_message_text(int(CHANNEL_OR_GROUP_ID), MESSAGE_ID, FilmySpot)
                print(f"𝐋𝐚𝐬𝐭 𝐜𝐡𝐞𝐜𝐤𝐞𝐝 𝐨𝐧: {last_update}")                
                await asyncio.sleep(6300)
                        
app.run(main_FilmySpot_Movies())
