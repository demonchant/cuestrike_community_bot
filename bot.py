import logging
import asyncio
from telegram import Bot
from telegram.constants import ParseMode
from datetime import datetime, timedelta

# Replace with your bot token
TOKEN = os.getenv("TOKEN")
CHAT_ID =os.getenv("GROUP_ID")

bot = Bot(token=TOKEN)

# Setup logging
logging.basicConfig(level=logging.INFO)

# Define daily schedule (UTC time)
schedule = [
    {"date": datetime(2025, 4, 26, 11, 0), "message": "Cuestrike is rising! The future starts now. CueCoin smart contract deployment is close. Stay alert!"},
    {"date": datetime(2025, 4, 27, 11, 0), "message": "Join the Cuestrike movement early! CueCoin deployment coming. Big rewards for early believers."},
    {"date": datetime(2025, 4, 28, 11, 0), "message": "Cuestrike is building the future. CueCoin smart contract goes live soon. Community-first, always."},
    {"date": datetime(2025, 4, 29, 11, 0), "message": "Only 2 days left until Cuestrike deploys CueCoin’s smart contract. History is being written!"},
    {"date": datetime(2025, 4, 30, 11, 0), "message": "Tomorrow marks a new era. Cuestrike will deploy CueCoin smart contract. True believers win early."},
    {"date": datetime(2025, 5, 1, 11, 0), "message": "Today is the big day. CueCoin smart contract deployed under the Cuestrike brand tonight!"},
    {"date": datetime(2025, 5, 1, 20, 0), "message": "CueCoin smart contract is live! Cuestrike community — prepare for full takeover. Airdrop coming soon!"},
]

async def send_scheduled_messages():
    for item in schedule:
        now = datetime.utcnow()
        wait_seconds = (item["date"] - now).total_seconds()

        if wait_seconds > 0:
            logging.info(f"Waiting {wait_seconds/3600:.2f} hours until next message...")
            await asyncio.sleep(wait_seconds)

        await bot.send_message(chat_id=CHAT_ID, text=item["message"], parse_mode=ParseMode.HTML)
        logging.info(f"Sent message: {item['message']}")

    logging.info("All scheduled messages sent!")

if name == "main":
    asyncio.run(send_scheduled_messages())
