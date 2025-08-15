def calculate_signal(price):
    if price and price > 150_000_000:
        return "📈 خرید"
    elif price and price < 145_000_000:
        return "📉 فروش"
    return "⏳ انتظار"
    
