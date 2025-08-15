import requests, os

BOT_TOKEN = os.getenv("BOT_TOKEN")
CHAT_ID = os.getenv("CHAT_ID")

url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
resp = requests.post(url, json={"chat_id": CHAT_ID, "text": "✅ ارتباط با تلگرام برقرار شد"})
print(resp.json())
