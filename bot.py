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
    {"date": datetime(2025, 4, 26, 11, 0), "message": "🚀 The countdown begins for something huge — Cue Coin is launching soon!
Our smart contract deployment is just around the corner. Get ready for a new era in crypto! #CueCoin #CryptoRevolution"},
    {"date": datetime(2025, 4, 27, 11, 0), "message": "🔒 We’re getting closer to launching the Cue Coin smart contract!
The team is working hard behind the scenes. It’s time to prepare for a major shift in the crypto world. Stay tuned! 💥"},
    {"date": datetime(2025, 4, 28, 11, 0), "message": "⏳ Only a few days left! The Cue Coin smart contract deployment is almost here.
We are about to change the game. Are you ready for Cue Coin? #Crypto #Blockchain #SmartContract"},
    {"date": datetime(2025, 4, 29, 11, 0), "message": "📅 Mark your calendars — the Cue Coin smart contract goes LIVE in just 2 days!
This is the moment we’ve all been waiting for. Don’t miss out on the next big thing in crypto. Let’s make history together!"},
    {"date": datetime(2025, 4, 30, 11, 0), "message": "🔥 Just 1 day left! The Cue Coin smart contract will be deployed tomorrow!
Get ready for the revolution. This is the moment we’ve all been working toward. Let’s make it epic! 💎"},
    {"date": datetime(2025, 5, 1, 11, 0), "message": "🚀 IT’S TIME! The Cue Coin smart contract is officially deployed today!
The future of crypto is here. Stay tuned for more updates as we take the next steps towards creating a powerful community and ecosystem. #CueCoin #SmartContract #Crypto"},
    {"date": datetime(2025, 5, 1, 20, 0), "message": "💥 Cue Coin smart contract is LIVE!
The journey has officially begun, and the possibilities are endless. Stay with us for exciting developments, airdrops, and much more. Thank you for being part of this journey! 🌍🚀"},
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
