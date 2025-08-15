import time
from datetime import datetime
from modules.fetch_data import fetch_data
from modules.indicators import calculate_indicators
from modules.smc import detect_smc_signals
from config import BOT_TOKEN, CHAT_ID, START_HOUR, END_HOUR
import requests

# تابع ارسال پیام به تلگرام
def send_telegram_message(text):
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    payload = {"chat_id": CHAT_ID, "text": text}
    resp = requests.post(url, json=payload)
    return resp.json()

# ===== پیام تست اولیه =====
try:
    resp = send_telegram_message("✅ تست اتصال ربات سیگنال AbrakiSignal موفق بود.")
    print("پیام تست ارسال شد:", resp)
except Exception as e:
    print("❌ خطا در ارسال پیام تست:", e)
    exit(1)  # اگر پیام تست نرفت، برنامه رو متوقف می‌کنیم


# ===== حلقه اجرای اصلی =====
while True:
    now = datetime.now()
    current_hour = now.hour

    if START_HOUR <= current_hour < END_HOUR:
        try:
            # 1. گرفتن دیتا
            df = fetch_data()

            # 2. محاسبه اندیکاتورها
            df = calculate_indicators(df)

            # 3. تشخیص سیگنال SMC
            signal = detect_smc_signals(df)

            # 4. اگر سیگنال Buy یا Sell پیدا شد → ارسال پیام
            if signal:
                send_telegram_message(signal)

        except Exception as e:
            print(f"خطا در اجرای ربات: {e}")

    else:
        print("⏳ خارج از ساعت کاری ربات هستیم...")

    # تاخیر بین هر چک (می‌توانی تغییرش دهی)
    time.sleep(60)
    
