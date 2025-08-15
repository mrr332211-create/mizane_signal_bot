import os

BOT_TOKEN = os.getenv("BOT_TOKEN")
CHAT_ID = os.getenv("CHAT_ID")
INTERVAL = int(os.getenv("INTERVAL", 300))  # فاصله زمانی (ثانیه)
HISTORY_FILE = "history.csv"               # محل ذخیره تاریخچه
