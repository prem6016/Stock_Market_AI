from stock_agent import analyze_stock


def get_technical_analysis(symbol: str):
    """Return technical indicators (SMA20/50/200, RSI, MACD, volume stats)
    and their interpretation for the given stock symbol.

    Delegates to stock_agent.analyze_stock() so that the indicator
    calculations used by the CLI script and by the Gemini agent tool stay
    in sync instead of being maintained twice.
    """

    return analyze_stock(symbol)
