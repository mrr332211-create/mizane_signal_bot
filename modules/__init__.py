
import pandas as pd
import ta

def calculate_indicators(df):
    # EMA
    df['ema20'] = ta.trend.EMAIndicator(df['close'], window=20).ema_indicator()
    df['ema50'] = ta.trend.EMAIndicator(df['close'], window=50).ema_indicator()
    
    # RSI
    df['rsi'] = ta.momentum.RSIIndicator(df['close'], window=14).rsi()
    
    # MACD
    macd = ta.trend.MACD(df['close'])
    df['macd'] = macd.macd()
    df['macd_signal'] = macd.macd_signal()
    
    # Heikin Ashi
    ha_df = heikin_ashi(df)
    df = pd.concat([df, ha_df], axis=1)

    return df

def heikin_ashi(df):
    ha_df = pd.DataFrame(index=df.index)
    ha_df['ha_close'] = (df['open'] + df['high'] + df['low'] + df['close']) / 4
    ha_open = []
    for i in range(len(df)):
        if i == 0:
            ha_open.append(df['open'].iloc[0])
        else:
            ha_open.append((ha_open[-1] + ha_df['ha_close'].iloc[i-1]) / 2)
    ha_df['ha_open'] = ha_open
    ha_df['ha_high'] = df[['high', 'low', 'close']].max(axis=1)
    ha_df['ha_low'] = df[['high', 'low', 'close']].min(axis=1)
    return ha_df
  
