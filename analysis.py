def interpret_rsi(rsi):

    if rsi is None:
        return "Unavailable"

    if rsi >= 70:
        return "Overbought"

    elif rsi <= 30:
        return "Oversold"

    elif rsi >= 50:
        return "Bullish"

    else:
        return "Bearish"


def interpret_trend(price, sma20, sma50, sma200):

    # SMA200 needs ~200 trading days of history to be defined. For recently
    # listed stocks or short history windows it (and sometimes SMA50) will
    # be missing. Rather than silently mis-classifying the trend, say so.
    if price is None or sma20 is None or sma50 is None:
        return "Insufficient data"

    if sma200 is None:
        if price > sma20 and sma20 > sma50:
            return "Short-term Uptrend (insufficient history for SMA200)"
        elif price < sma20 and sma20 < sma50:
            return "Short-term Downtrend (insufficient history for SMA200)"
        else:
            return "Weak/Mixed (insufficient history for SMA200)"

    if price > sma20 and sma20 > sma50 and sma50 > sma200:
        return "Strong Uptrend"

    elif price < sma20 and sma20 < sma50 and sma50 < sma200:
        return "Strong Downtrend"

    elif price > sma200:
        return "Long-term Bullish"

    else:
        return "Weak/Mixed"


def interpret_macd(macd, signal):

    if macd is None or signal is None:
        return "Unavailable"

    if macd > signal:
        return "Bullish"

    elif macd < signal:
        return "Bearish"

    return "Neutral"