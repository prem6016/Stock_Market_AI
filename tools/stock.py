import yfinance as yf
import math


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


def get_stock_price(symbol: str):

    stock = yf.Ticker(symbol)

    data = stock.history(period="5d")

    if data.empty:
        return {
            "symbol": symbol,
            "status": "unavailable",
            "reason": "No market data returned"
        }

    # Remove rows where Close is missing
    data = data.dropna(subset=["Close"])

    if data.empty:
        return {
            "symbol": symbol,
            "status": "unavailable",
            "reason": "No valid closing price returned"
        }

    latest = data.iloc[-1]

    price = clean_number(latest["Close"])
    volume = clean_number(latest["Volume"])

    if price is None:
        return {
            "symbol": symbol,
            "status": "unavailable",
            "reason": "Latest price is unavailable"
        }

    return {
        "symbol": symbol,
        "status": "success",
        "price": price,
        "volume": int(volume) if volume is not None else None,
        "date": str(data.index[-1])
    }