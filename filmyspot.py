from pyrogram import Client
from pyrogram.errors import FloodWait
import asyncio
import datetime
import pytz
import os

# Initialize metrics dictionary to store bot performance metrics
metrics = {}

app = Client(
    name="botstatus_pratheek",
    api_id=int(os.environ["API_ID"]),
    api_hash=os.environ["API_HASH"],
    session_string=os.environ["SESSION_STRING"]
)
TIME_ZONE = os.environ["TIME_ZONE"]
BOT_LIST = [i.strip() for i in os.environ.get("BOT_LIST").split(' ')]
CHANNEL_OR_GROUP_ID = int(os.environ["CHANNEL_OR_GROUP_ID"])
MESSAGE_ID = int(os.environ["MESSAGE_ID"])
BOT_ADMIN_IDS = [int(i.strip()) for i in os.environ.get("BOT_ADMIN_IDS").split(' ')]

async def main_FilmySpot_Movies():
    async with app:
        while True:
            print("Checking bot status...")
            status_message = "📊 | 𝗟𝗜𝗩𝗘 𝗕𝗢𝗧 𝗦𝗧𝗔𝗧𝗨𝗦\n"
            for bot in BOT_LIST:
                try:
                    # Send /start command to bot
                    start_time = datetime.datetime.now()
                    yyy_pratheek = await app.send_message(bot, "/start")
                    await asyncio.sleep(10)
                    zzz_pratheek = app.get_chat_history(bot, limit=1)
                    async for ccc in zzz_pratheek:
                        bbb = ccc.id
                    response_time = (datetime.datetime.now() - start_time).total_seconds()

                    if yyy_pratheek.message_id == bbb:
                        # Bot is down
                        status_message += f"\n🤖  @{bot}\n        └ **Status:** ❌ Down\n        └ **Response Time:** {response_time:.2f}s"
                        # Update metrics
                        if bot not in metrics:
                            metrics[bot] = {"status": "down", "response_times": [response_time]}
                        else:
                            metrics[bot]["status"] = "down"
                            metrics[bot]["response_times"].append(response_time)
                    else:
                        # Bot is alive
                        status_message += f"\n🤖  @{bot}\n        └ **Status:** ✅ Alive\n        └ **Response Time:** {response_time:.2f}s"
                        # Update metrics
                        if bot not in metrics:
                            metrics[bot] = {"status": "alive", "response_times": [response_time]}
                        else:
                            metrics[bot]["status"] = "alive"
                            metrics[bot]["response_times"].append(response_time)

                except FloodWait as e:
                    await asyncio.sleep(e.x)

                except Exception as ex:
                    status_message += f"\n🤖  @{bot}\n        └ **Error:** ❗ {str(ex)}"

            # Update status message with last checked time and timezone
            time = datetime.datetime.now(pytz.timezone(f"{TIME_ZONE}"))
            last_update = time.strftime(f"%d %b %Y at %I:%M %p")
            status_message += f"\n\n✔️ Last checked on: {last_update} ({TIME_ZONE})\n\n♻️ Refreshes automatically - Powered By FilmySpot Movies**"

            # Update the message in the channel or group
            await app.edit_message_text(int(CHANNEL_OR_GROUP_ID), MESSAGE_ID, status_message)

            # Sleep for 6300 seconds (approximately 105 minutes) before checking again
            await asyncio.sleep(6300)

app.run(main_FilmySpot_Movies())
