import time
import csv
import os
import requests
from datetime import datetime
from modules.fetch_data import get_mozane
from modules.indicators import calculate_signal
from config import BOT_TOKEN, CHAT_ID, INTERVAL, HISTORY_FILE

def send_telegram_message(text):
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    try:
        resp = requests.post(url, json={"chat_id": CHAT_ID, "text": text})
        print(f"Telegram status: {resp.status_code}")
    except Exception as e:
        print(f"Telegram error: {e}")

def save_history(timestamp, price, signal):
    file_exists = os.path.isfile(HISTORY_FILE)
    with open(HISTORY_FILE, mode="a", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        if not file_exists:
            writer.writerow(["time", "price", "signal"])
        writer.writerow([timestamp, price, signal])

send_telegram_message("✅ ربات فعال شد - هر ۵ دقیقه مظنه و سیگنال را می‌فرستد")

while True:
    now = datetime.utcnow()
    try:
        mozane = get_mozane()
        if mozane:
            signal = calculate_signal(mozane)
            ts = now.strftime("%Y-%m-%d %H:%M:%S")
            message = f"{ts} UTC\n💰 مظنه: {mozane:,} تومان\n📊 سیگنال: {signal}"
            send_telegram_message(message)
            save_history(ts, mozane, signal)
        else:
            send_telegram_message("❌ دریافت قیمت ناموفق")
    except Exception as e:
        send_telegram_message(f"Error: {e}")
    time.sleep(INTERVAL)
    
