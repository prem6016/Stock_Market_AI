import sys

import yfinance as yf
import pandas as pd
from ai_analysis import get_ai_analysis
from ta.trend import SMAIndicator, MACD
from ta.momentum import RSIIndicator

from analysis import (
    interpret_rsi,
    interpret_trend,
    interpret_macd
)
from ai_analysis import get_ai_analysis

def get_stock_data(symbol):

    stock = yf.Ticker(symbol)

    data = stock.history(period="1y")

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

    # Get data
    data = get_stock_data(symbol)

    # Calculate indicators
    data = calculate_indicators(data)

    # Get latest trading day
    latest = data.iloc[-1]

    price = latest["Close"]
    sma20 = latest["SMA20"]
    sma50 = latest["SMA50"]
    sma200 = latest["SMA200"]

    rsi = latest["RSI"]

    macd = latest["MACD"]
    macd_signal = latest["MACD_SIGNAL"]

    daily_return = latest["Daily_Return"]
    volume_change = latest["Volume_Change"]

    # Interpret indicators
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

    # Display report
    print("\n====================================")
    print("        TECHNICAL ANALYSIS")
    print("====================================")

    print(f"\nSymbol: {symbol}")
    print(f"Price: ₹{price:.2f}")

    print("\n--- Moving Averages ---")

    print(f"SMA20:  ₹{sma20:.2f}")
    print(f"SMA50:  ₹{sma50:.2f}")
    print(f"SMA200: ₹{sma200:.2f}")

    print("\n--- Momentum ---")

    print(f"RSI: {rsi:.2f}")
    print(f"RSI Status: {rsi_status}")

    print(f"\nMACD: {macd:.2f}")
    print(f"MACD Signal: {macd_signal:.2f}")
    print(f"MACD Status: {macd_status}")

    print("\n--- Price / Volume ---")

    print(f"Daily Return: {daily_return:.2f}%")
    print(f"Volume Change: {volume_change:.2f}%")

    print("\n--- Overall ---")

    print(f"Trend: {trend}")

    print("\n====================================")

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

        "trend": trend
    }
if len(sys.argv) > 1:
    symbol = sys.argv[1].upper()
else:
    symbol = "HFCL.NS"

    analysis = analyze_stock(symbol)

    print("\n====================================")
    print("           AI ANALYSIS")
    print("====================================")

    ai_result = get_ai_analysis(analysis)

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