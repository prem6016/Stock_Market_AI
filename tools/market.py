import yfinance as yf


def get_market_context():

    nifty = yf.Ticker("^NSEI")
    bank_nifty = yf.Ticker("^NSEBANK")

    nifty_data = nifty.history(period="5d")
    bank_data = bank_nifty.history(period="5d")

    return {
        "nifty": {
            "price": float(nifty_data["Close"].iloc[-1]),
            "previous_close": float(nifty_data["Close"].iloc[-2])
        },
        "bank_nifty": {
            "price": float(bank_data["Close"].iloc[-1]),
            "previous_close": float(bank_data["Close"].iloc[-2])
        }
    }