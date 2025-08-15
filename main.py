import os
import time
import requests
import pandas as pd
from datetime import datetime
from modules.fetch_data import get_mozane
from modules.indicators import calculate_indicators
from modules.smc import analyze_smc
from config import BOT_TOKEN, CHAT_ID, START_HOUR, END_HOUR

# ایجاد دیتافریم اولیه
df = pd.DataFrame(columns=['open', 'high', 'low', 'close'])

def send_telegram_message(message):
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    payload = {
        "chat_id": CHAT_ID,
        "text": message
    }
    requests.post(url, json=payload)

while True:
    now = datetime.now()
    curr_time = now.replace(second=0, microsecond=0)
    hour = now.hour

    try:
        mozane = get_mozane()
    except Exception as e:
        print("خطا در دریافت مظنه:", e)
        time.sleep(10)
        continue

    # اگر دیتافریم خالی است
    if df.empty:
        df = pd.DataFrame([{
            'open': mozane,
            'high': mozane,
            'low': mozane,
            'close': mozane
        }], index=[curr_time])
    else:
        # آپدیت کندل فعلی یا ساخت کندل جدید
        if df.index[-1] == curr_time:
            df.loc[df.index[-1], 'high'] = max(df.iloc[-1]['high'], mozane)
            df.loc[df.index[-1], 'low'] = min(df.iloc[-1]['low'], mozane)
            df.loc[df.index[-1], 'close'] = mozane
        else:
            df = pd.concat([
                df,
                pd.DataFrame([{
                    'open': mozane,
                    'high': mozane,
                    'low': mozane,
                    'close': mozane
                }], index=[curr_time])
            ])

    # محاسبه اندیکاتورها فقط در ساعات مجاز
    if START_HOUR <= hour < END_HOUR:
        try:
            ha_df, ema20, ema50, rsi, macd_line, signal_line = calculate_indicators(df)
            smc_signals = analyze_smc(df)

            # شرط خرید
            if (ema20 > ema50 and rsi < 30 and macd_line > signal_line and 
                ha_df.iloc[-1]['close'] > ha_df.iloc[-1]['open'] and
                ('BOS_UP' in smc_signals or 'Buy_Liquidity_Grab' in smc_signals)):
                
                message = f"📈 BUY Scalping + SMC\n⏱ {now.strftime('%H:%M')}\nمظنه: {mozane:,} IRR\nEMA20>EMA50 ✅ | RSI={int(rsi)} ✅ | MACD Bullish ✅ | HA سبز ✅\nSMC: {', '.join(smc_signals)}"
                send_telegram_message(message)

            # شرط فروش
            elif (ema20 < ema50 and rsi > 70 and macd_line < signal_line and 
                  ha_df.iloc[-1]['close'] < ha_df.iloc[-1]['open'] and
                  ('BOS_DOWN' in smc_signals or 'Sell_Liquidity_Grab' in smc_signals)):

                message = f"📉 SELL Scalping + SMC\n⏱ {now.strftime('%H:%M')}\nمظنه: {mozane:,} IRR\nEMA20<EMA50 ✅ | RSI={int(rsi)} ✅ | MACD Bearish ✅ | HA قرمز ✅\nSMC: {', '.join(smc_signals)}"
                send_telegram_message(message)

            else:
                send_telegram_message("⏳ صبر کنید... هنوز سیگنال سودده شناسایی نشده")

        except Exception as e:
            print("خطا در اجرای آنالیز:", e)

    else:
        send_telegram_message("⏳ بازار خارج از ساعات کاری است...")

    time.sleep(300)  # هر 5 دقیقه
                    
