import os

BOT_TOKEN = os.getenv("BOT_TOKEN")
CHAT_ID = os.getenv("CHAT_ID")
GOLD_API_KEY = os.getenv("GOLD_API_KEY")
USD_API_URL = os.getenv("USD_API_URL")
START_HOUR = int(os.getenv("START_HOUR", 10))
END_HOUR = int(os.getenv("END_HOUR", 19))
