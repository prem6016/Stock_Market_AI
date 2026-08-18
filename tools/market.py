import yfinance as yf


def _latest_and_previous_close(symbol):
    data = yf.Ticker(symbol).history(period="5d")

    if data.empty or len(data) < 2:
        return None

    return {
        "price": float(data["Close"].iloc[-1]),
        "previous_close": float(data["Close"].iloc[-2])
    }


def get_market_context():
    """Return the latest and previous close for the Nifty 50 and Bank
    Nifty indices, to give broader Indian market context for a stock
    analysis. Returns None for an index if data is temporarily
    unavailable, rather than raising."""

    return {
        "nifty": _latest_and_previous_close("^NSEI"),
        "bank_nifty": _latest_and_previous_close("^NSEBANK")
    }