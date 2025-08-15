import time
import datetime
from config import START_HOUR, END_HOUR, CHAT_ID
from modules.fetch_data import get_price_data
from modules.indicators import calculate_indicators
from modules.smc import detect_smc
from telegram import Bot

bot = Bot(token=BOT_TOKEN)

def send_signal(message):
    bot.send_message(chat_id=CHAT_ID, text=message)

while True:
    now = datetime.datetime.now().hour
    if START_HOUR <= now < END_HOUR:
        df = get_price_data()
        df = calculate_indicators(df)
        smc_info = detect_smc(df)
        if smc_info['signal'] in ['buy', 'sell']:
            send_signal(f"Signal: {smc_info['signal'].upper()}\nDetails:\n{smc_info['details']}")
    time.sleep(60)
    
