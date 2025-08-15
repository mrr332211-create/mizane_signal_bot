import requests
from config import BOT_TOKEN, CHAT_ID  # استفاده از مقادیر پروژه

url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
payload = {
    "chat_id": CHAT_ID,
    "text": "📢 پیام تست: AbrakiSignal Bot — بررسی اتصال مستقیم به تلگرام"
}

try:
    resp = requests.post(url, json=payload)
    print("Status Code:", resp.status_code)
    print("Response:", resp.text)
except Exception as e:
    print("❌ خطا در ارسال پیام:", e)
  
