import requests

def get_mozane():
    try:
        gold_url = "https://api.coingecko.com/api/v3/simple/price?ids=gold&vs_currencies=usd"
        gold_price = requests.get(gold_url, timeout=10).json().get("gold", {}).get("usd")

        usdt_url = "https://api.coingecko.com/api/v3/simple/price?ids=tether&vs_currencies=irr"
        dollar_price = requests.get(usdt_url, timeout=10).json().get("tether", {}).get("irr")
        if dollar_price:
            dollar_price = dollar_price / 10

        if gold_price and dollar_price:
            return round(gold_price * dollar_price * 4.24927, 2)  # مظنه ۱۷ مثقال عیار۹۰۰
    except Exception as e:
        print(f"Error fetching mozane: {e}")
    return None
    
