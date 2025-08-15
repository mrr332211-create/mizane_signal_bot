import requests
from config import BOT_TOKEN, CHAT_ID
from keep_alive import keep_alive

def send_message(text):
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    payload = {
        "chat_id": CHAT_ID,
        "text": text
    }
    r = requests.post(url, json=payload)
    return r.json()

if __name__ == "__main__":
    keep_alive()
    # نمونه ارسال پیام هنگام روشن شدن
    send_message("✅ ربات با موفقیت فعال شد و 24/7 روشن می‌ماند!")
    
