from pyrogram import Client, filters
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
            print("Checking...")
            status_message = "📊 | 𝗟𝗜𝗩𝗘 𝗕𝗢𝗧 𝗦𝗧𝗔𝗧𝗨𝗦\n"
            for bot in BOT_LIST:
                try:
                    # Start time to measure response time
                    start_time = datetime.datetime.now()

                    # Send /start command to bot
                    yyy_pratheek = await app.send_message(bot, "/start")
                    aaa = yyy_pratheek.id
                    await asyncio.sleep(10)
                    zzz_pratheek = app.get_chat_history(bot, limit=1)
                    async for ccc in zzz_pratheek:
                        bbb = ccc.id
                    if aaa == bbb:
                        # Bot is down
                        status_message += f"\n🤖  @{bot}\n        └ **Down** ❌"
                        # Update metrics
                        if bot not in metrics:
                            metrics[bot] = {"down_count": 1, "up_count": 0}
                        else:
                            metrics[bot]["down_count"] += 1
                    else:
                        # Bot is alive
                        status_message += f"\n🤖  @{bot}\n        └ **Alive** ✅"
                        # Update metrics
                        if bot not in metrics:
                            metrics[bot] = {"down_count": 0, "up_count": 1}
                        else:
                            metrics[bot]["up_count"] += 1

                    # Calculate response time
                    end_time = datetime.datetime.now()
                    response_time = (end_time - start_time).total_seconds()

                    # Update metrics with response time
                    if bot in metrics:
                        if "response_times" not in metrics[bot]:
                            metrics[bot]["response_times"] = []
                        metrics[bot]["response_times"].append(response_time)

                    # Append metrics to status message
                    if bot in metrics:
                        status_message += f"\n        ⌊ {metrics[bot]}"

                except FloodWait as e:
                    await asyncio.sleep(e.x)

            # Update status message with last checked time and timezone
            time = datetime.datetime.now(pytz.timezone(f"{TIME_ZONE}"))
            last_update = time.strftime(f"%d %b %Y at %I:%M %p")
            status_message += f"\n\n✔️ Last checked on: {last_update} ({TIME_ZONE})\n\n♻️ Refreshes automatically - Powered By FilmySpot Movies**"

            # Update the message in the channel or group
            await app.edit_message_text(int(CHANNEL_OR_GROUP_ID), MESSAGE_ID, status_message)

            # Print metrics
            print("Metrics:", metrics)

            # Sleep for 6300 seconds (approximately 105 minutes) before checking again
            await asyncio.sleep(6300)

app.run(main_FilmySpot_Movies())
