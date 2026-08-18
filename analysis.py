def interpret_rsi(rsi):

    if rsi >= 70:
        return "Overbought"

    elif rsi <= 30:
        return "Oversold"

    elif rsi >= 50:
        return "Bullish"

    else:
        return "Bearish"


def interpret_trend(price, sma20, sma50, sma200):

    if price > sma20 and sma20 > sma50 and sma50 > sma200:
        return "Strong Uptrend"

    elif price < sma20 and sma20 < sma50 and sma50 < sma200:
        return "Strong Downtrend"

    elif price > sma200:
        return "Long-term Bullish"

    else:
        return "Weak/Mixed"


def interpret_macd(macd, signal):

    if macd > signal:
        return "Bullish"

    elif macd < signal:
        return "Bearish"

    return "Neutral"