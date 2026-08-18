import sys
import math

import yfinance as yf
from ta.trend import SMAIndicator, MACD
from ta.momentum import RSIIndicator

from analysis import (
    interpret_rsi,
    interpret_trend,
    interpret_macd
)
from ai_analysis import get_ai_analysis
from config import DEFAULT_SYMBOL


def clean_number(value):
    """Convert a pandas/numpy scalar to a plain float, or None if it is
    missing, NaN, or infinite (e.g. an SMA200 value before 200 days of
    history exist)."""

    if value is None:
        return None

    try:
        value = float(value)

        if math.isnan(value) or math.isinf(value):
            return None

        return value

    except (TypeError, ValueError):
        return None


def get_stock_data(symbol, period="1y"):
    """Fetch historical OHLCV data for a symbol.

    Raises ValueError if no data is returned (e.g. invalid symbol or a
    Yahoo Finance outage) instead of letting a later .iloc[-1] fail with an
    obscure IndexError.
    """

    stock = yf.Ticker(symbol)
    data = stock.history(period=period)

    if data.empty:
        raise ValueError(
            f"No historical data returned for symbol '{symbol}'. "
            "Check that the symbol is correct (e.g. use the '.NS' suffix "
            "for NSE-listed stocks)."
        )

    return data


def calculate_indicators(data):

    # Moving averages
    data["SMA20"] = SMAIndicator(
        close=data["Close"],
        window=20
    ).sma_indicator()

    data["SMA50"] = SMAIndicator(
        close=data["Close"],
        window=50
    ).sma_indicator()

    data["SMA200"] = SMAIndicator(
        close=data["Close"],
        window=200
    ).sma_indicator()

    # RSI
    data["RSI"] = RSIIndicator(
        close=data["Close"],
        window=14
    ).rsi()

    # MACD
    macd = MACD(
        close=data["Close"]
    )

    data["MACD"] = macd.macd()
    data["MACD_SIGNAL"] = macd.macd_signal()

    # Daily return
    data["Daily_Return"] = (
        data["Close"].pct_change() * 100
    )

    # Volume change vs previous trading day
    data["Volume_Change"] = (
        data["Volume"].pct_change() * 100
    )

    # 20-day average volume
    data["AVG_VOLUME_20"] = (
        data["Volume"]
        .rolling(window=20)
        .mean()
    )

    # Current volume vs 20-day average
    data["Volume_vs_Avg"] = (
        (data["Volume"] / data["AVG_VOLUME_20"]) - 1
    ) * 100

    return data


def analyze_stock(symbol):
    """Compute technical indicators for the latest trading day and return
    them as a plain dict. This function has no side effects (no printing) -
    use print_technical_report() to display it."""

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

    trend = interpret_trend(price, sma20, sma50, sma200)
    rsi_status = interpret_rsi(rsi)
    macd_status = interpret_macd(macd, macd_signal)

    def r(value, digits=2):
        return None if value is None else round(value, digits)

    return {
        "symbol": symbol,
        "price": r(price),

        "sma20": r(sma20),
        "sma50": r(sma50),
        "sma200": r(sma200),

        "rsi": r(rsi),
        "rsi_status": rsi_status,

        "macd": r(macd),
        "macd_signal": r(macd_signal),
        "macd_status": macd_status,

        "daily_return": r(daily_return),
        "volume_change": r(volume_change),
        "avg_volume_20": r(avg_volume_20, 0),
        "volume_vs_avg": r(volume_vs_avg),

        "trend": trend
    }


def _fmt(value, suffix=""):
    """Format a possibly-None numeric value for display."""
    if value is None:
        return "N/A"
    return f"{value:.2f}{suffix}"


def print_technical_report(analysis):
    """Render a human-readable technical analysis report to stdout."""

    print("\n====================================")
    print("        TECHNICAL ANALYSIS")
    print("====================================")

    print(f"\nSymbol: {analysis['symbol']}")
    print(f"Price: ₹{_fmt(analysis['price'])}")

    print("\n--- Moving Averages ---")
    print(f"SMA20:  ₹{_fmt(analysis['sma20'])}")
    print(f"SMA50:  ₹{_fmt(analysis['sma50'])}")
    print(f"SMA200: ₹{_fmt(analysis['sma200'])}")

    print("\n--- Momentum ---")
    print(f"RSI: {_fmt(analysis['rsi'])}")
    print(f"RSI Status: {analysis['rsi_status']}")

    print(f"\nMACD: {_fmt(analysis['macd'])}")
    print(f"MACD Signal: {_fmt(analysis['macd_signal'])}")
    print(f"MACD Status: {analysis['macd_status']}")

    print("\n--- Price / Volume ---")
    print(f"Daily Return: {_fmt(analysis['daily_return'], '%')}")
    print(f"Volume Change: {_fmt(analysis['volume_change'], '%')}")
    print(f"20-day Avg Volume: {_fmt(analysis['avg_volume_20'])}")
    print(f"Volume vs 20-day Avg: {_fmt(analysis['volume_vs_avg'], '%')}")

    print("\n--- Overall ---")
    print(f"Trend: {analysis['trend']}")

    print("\n====================================")


def print_ai_report(ai_result):
    """Render a human-readable AI analysis report to stdout."""

    print("\n====================================")
    print("           AI ANALYSIS")
    print("====================================")

    print("\nSummary:")
    print(ai_result["summary"])

    print("\nBullish Signals:")
    for signal in ai_result["bullish_signals"]:
        print(f"  + {signal}")

    print("\nBearish Signals:")
    for signal in ai_result["bearish_signals"]:
        print(f"  - {signal}")

    print("\nRisk:")
    print(ai_result["risk"])

    print("\nKey Signals:")
    for signal in ai_result["key_signals"]:
        print(f"  • {signal}")

    print("\nOverall Assessment:")
    print(ai_result["overall_assessment"])

    print(f"\nConfidence: {ai_result['confidence']}/100")

    print("\n====================================")


def main():
    symbol = sys.argv[1].upper() if len(sys.argv) > 1 else DEFAULT_SYMBOL

    try:
        analysis = analyze_stock(symbol)
    except ValueError as exc:
        print(f"Error: {exc}")
        sys.exit(1)

    print_technical_report(analysis)

    try:
        ai_result = get_ai_analysis(analysis)
    except Exception as exc:
        print(f"\nAI analysis unavailable: {exc}")
        sys.exit(1)

    print_ai_report(ai_result)


if __name__ == "__main__":
    main()
