from stock_agent import get_stock_data, calculate_indicators
import math

from analysis import (
    interpret_rsi,
    interpret_trend,
    interpret_macd
)

def clean_number(value):

    if value is None:
        return None

    try:
        value = float(value)

        if math.isnan(value) or math.isinf(value):
            return None

        return value

    except (TypeError, ValueError):
        return None
    
def get_technical_analysis(symbol: str):

    data = get_stock_data(symbol)

    data = calculate_indicators(data)

    latest = data.iloc[-1]

    price = clean_number(latest["Close"])
    sma20 = clean_number(latest["SMA20"])
    sma50 = clean_number(latest["SMA50"])
    sma200 = clean_number(latest["SMA200"])

    rsi = clean_number(latest["RSI"])

    macd = clean_number(latest["MACD"])
    macd_signal = clean_number(latest["MACD_SIGNAL"])

    daily_return = clean_number(latest["Daily_Return"])
    volume_change = clean_number(latest["Volume_Change"])
    avg_volume_20 = clean_number(latest["AVG_VOLUME_20"])
    volume_vs_avg = clean_number(latest["Volume_vs_Avg"])
    trend = interpret_trend(
        price,
        sma20,
        sma50,
        sma200
    )

    rsi_status = interpret_rsi(rsi)

    macd_status = interpret_macd(
        macd,
        macd_signal
    )

    return {
        "symbol": symbol,
        "price": round(price, 2),

        "sma20": round(sma20, 2),
        "sma50": round(sma50, 2),
        "sma200": round(sma200, 2),

        "rsi": round(rsi, 2),
        "rsi_status": rsi_status,

        "macd": round(macd, 2),
        "macd_signal": round(macd_signal, 2),
        "macd_status": macd_status,

        "daily_return": round(daily_return, 2),

        "volume_change": round(volume_change, 2),
        "avg_volume_20": round(avg_volume_20),
        "volume_vs_avg": round  (volume_vs_avg, 2),

        "trend": trend
    }