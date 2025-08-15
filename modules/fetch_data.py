import requests
import pandas as pd
from config import GOLD_API_KEY, USD_API_URL

def get_price_data():
    # دریافت قیمت طلا از goldapi.io
    headers = {"x-access-token": GOLD_API_KEY}
    gold_url = "https://www.goldapi.io/api/XAU/USD"
    gold_price = requests.get(gold_url, headers=headers).json()['price']

    # دریافت نرخ دلار
    usd_price = requests.get(USD_API_URL).json()['price']

    # محاسبه مظنه با فرمول
    mozaneh = (gold_price * usd_price) / 4.3318

    # ساخت دیتافریم فرضی برای تست (اینجا باید دیتای واقعی کندل‌ها باشه)
    df = pd.DataFrame({
        "open": [mozaneh - 2, mozaneh - 1],
        "high": [mozaneh + 1, mozaneh + 2],
        "low": [mozaneh - 3, mozaneh - 2],
        "close": [mozaneh, mozaneh + 1]
    })

    return df
  
