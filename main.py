import time
from config import BOT_TOKEN, CHAT_ID, START_HOUR, END_HOUR
from modules.fetch_data import get_market_data
from modules.smc import analyze_smc
import requests
from datetime import datetime

def send_message(text):
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    requests.post(url, data={"chat_id": CHAT_ID, "text": text})

while True:
    now_hour = datetime.now().hour

    # فقط داخل ساعت‌های تعیین‌شده کار کن
    if START_HOUR <= now_hour < END_HOUR:
        data = get_market_data()
        signal = analyze_smc(data)

        if signal:  # اگر سیگنال معتبر پیدا شد
            send_message(signal)
        else:
            send_message("⏳ صبر کنید... هنوز سیگنال سودده شناسایی نشده")
    else:
        send_message("⏳ بازار خارج از ساعت کاری است")

    time.sleep(300)  # هر 5 دقیقه یک بار
            print("خطا در اجرای ربات:", e)
    else:
        print("⏳ خارج از ساعت کاری هستیم.")

    time.sleep(60)  # هر یک دقیقه
    
