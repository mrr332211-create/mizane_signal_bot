from config import BOT_TOKEN, CHAT_ID
from keep_alive import keep_alive
import requests
import time

def send_message(text):
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    payload = {"chat_id": CHAT_ID, "text": text}
    requests.post(url, json=payload)

keep_alive()

send_message("✅ Mizane Signal Bot is now online!")

while True:
    # Loop for checking and sending signals
    time.sleep(60)
  
