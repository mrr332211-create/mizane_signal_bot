import os

# --- توکن‌ها و کلیدها ---
BOT_TOKEN = os.getenv("8318356221:AAFvx_EXM2EoIHlYh_l9AvxkzVXxJZK_tm0")
CHAT_ID = os.getenv("-1002256481234")
GOLD_API_KEY = os.getenv("GOLD_API_KEY")
USD_API_URL = os.getenv("USD_API_URL")

# --- ساعت اجرای ربات ---
START_HOUR = int(os.getenv("START_HOUR", 10))
END_HOUR = int(os.getenv("END_HOUR", 19))

# --- اعتبارسنجی اولیه ---
required_vars = {
    "BOT_TOKEN": BOT_TOKEN,
    "CHAT_ID": CHAT_ID,
    "GOLD_API_KEY": GOLD_API_KEY,
    "USD_API_URL": USD_API_URL
}

missing = [k for k, v in required_vars.items() if not v]
if missing:
    raise ValueError(f"❌ Environment variables missing: {', '.join(missing)}")
    
