def detect_swing_highs_lows(df, lookback=5):
    highs, lows = [], []
    for i in range(lookback, len(df)-lookback):
        if df['ha_close'].iloc[i] == max(df['ha_close'].iloc[i-lookback:i+lookback+1]):
            highs.append(i)
        if df['ha_close'].iloc[i] == min(df['ha_close'].iloc[i-lookback:i+lookback+1]):
            lows.append(i)
    return highs, lows

def detect_bos_choch(df, highs, lows):
    signal = None
    if len(highs) >= 2 and df['ha_close'].iloc[highs[-1]] > df['ha_close'].iloc[highs[-2]]:
        signal = "BOS_up"
    elif len(lows) >= 2 and df['ha_close'].iloc[lows[-1]] < df['ha_close'].iloc[lows[-2]]:
        signal = "BOS_down"
    return signal

def detect_order_block(df):
    ob_type = None
    atr = (df['close'].rolling(14).max() - df['close'].rolling(14).min()).iloc[-1]
    if df['close'].iloc[-1] - df['close'].iloc[-4] > 2 * atr:
        ob_type = "Bullish_OB"
    elif df['close'].iloc[-4] - df['close'].iloc[-1] > 2 * atr:
        ob_type = "Bearish_OB"
    return ob_type

def detect_liquidity_grab(df):
    lg_type = None
    if df['high'].iloc[-1] > df['high'].shift(1).max() and df['ha_close'].iloc[-1] < df['open'].iloc[-1]:
        lg_type = "Buy_side_LG"
    if df['low'].iloc[-1] < df['low'].shift(1).min() and df['ha_close'].iloc[-1] > df['open'].iloc[-1]:
        lg_type = "Sell_side_LG"
    return lg_type

def detect_smc(df):
    highs, lows = detect_swing_highs_lows(df)
    ms_signal = detect_bos_choch(df, highs, lows)
    ob_signal = detect_order_block(df)
    lg_signal = detect_liquidity_grab(df)

    ema_filter = df['ema20'].iloc[-1] > df['ema50'].iloc[-1]
    rsi_filter = 40 < df['rsi'].iloc[-1] < 70
    macd_filter = df['macd'].iloc[-1] > df['macd_signal'].iloc[-1]

    signal = "none"
    details = []

    if ms_signal == "BOS_up" and ob_signal == "Bullish_OB" and ema_filter and macd_filter:
        signal = "buy"
        details.append("BOS_up + Bullish_OB confirmed with EMA & MACD")
    elif ms_signal == "BOS_down" and ob_signal == "Bearish_OB" and not ema_filter and not macd_filter:
        signal = "sell"
        details.append("BOS_down + Bearish_OB confirmed with EMA & MACD")

    if lg_signal:
        details.append(f"Liquidity Grab: {lg_signal}")

    if signal == "none" and (ms_signal or ob_signal or lg_signal):
        details.append(f"Pattern detected but not confirmed: ms={ms_signal}, ob={ob_signal}, lg={lg_signal}")

    return {"signal": signal, "details": "\n".join(details) if details else "No pattern detected."}
  
