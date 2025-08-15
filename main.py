import time
from datetime import datetime
import requests
from config import BOT_TOKEN, CHAT_ID, START_HOUR, END_HOUR
from modules.fetch_data import fetch_data
from modules.indicators import calculate_indicators
from modules.smc import detect_smc_signals

# ارسال پیام تلگرام
def send_telegram_message(text):
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    payload = {"chat_id": CHAT_ID, "text": text}
    resp = requests.post(url, json=payload)
    return resp

# --- پیام تست اتصال ---
try:
    send_telegram_message("✅ تست اتصال ربات AbrakiSignal موفق بود.")
    print("پیام تست اولیه ارسال شد.")
except Exception as e:
    print("❌ خطا در ارسال پیام تست:", e)
    exit(1)

# --- حلقه اصلی ---
while True:
    now = datetime.now()
    if START_HOUR <= now.hour < END_HOUR:
        try:
            df = fetch_data()
            df = calculate_indicators(df)
            signal = detect_smc_signals(df)

            if signal:
                send_telegram_message(signal)
        except Exception as e:
            print("خطا در اجرای ربات:", e)
    else:
        print("⏳ خارج از ساعت کاری هستیم.")

    time.sleep(60)  # هر یک دقیقه
