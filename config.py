import os

# توکن ربات تلگرام
BOT_TOKEN = os.getenv("BOT_TOKEN")  # مثال: 123456789:ABCDEF...

# شناسه چت تلگرام برای ارسال پیام
CHAT_ID = os.getenv("CHAT_ID")  # مثال: 123456789 یا @username

# کلید API برای دریافت قیمت طلا از goldapi.io
GOLD_API_KEY = os.getenv("GOLD_API_KEY")

# URL برای دریافت قیمت دلار (باید JSON برگردونه یا adapt شده به fetch_data)
USD_API_URL = os.getenv("USD_API_URL")

# ساعت شروع و پایان اجرای ربات (به وقت سرور)
START_HOUR = int(os.getenv("START_HOUR", 10))  # پیش‌فرض 10 صبح
END_HOUR = int(os.getenv("END_HOUR", 19))      # پیش‌فرض 7 عصر

# اعتبارسنجی اولیه برای جلوگیری از خطا در صورت نبود مقادیر
required_vars = {
    "BOT_TOKEN": BOT_TOKEN,
    "CHAT_ID": CHAT_ID,
    "GOLD_API_KEY": GOLD_API_KEY,
    "USD_API_URL": USD_API_URL
}

missing = [k for k, v in required_vars.items() if not v]
if missing:
    raise ValueError(f"❌ Environment variables missing: {', '.join(missing)}")
  
