from fundamentals import get_fundamentals
from fundamental_analysis import analyze_fundamentals


def get_fundamental_analysis(symbol: str):
    """Return raw fundamental metrics (P/E, ROE, revenue growth, debt, etc.)
    and their plain-language interpretation for a stock symbol.

    Args:
        symbol: Ticker symbol, e.g. "HFCL.NS" for an NSE-listed stock.
    """

    try:
        data = get_fundamentals(symbol)
    except ValueError as exc:
        return {"status": "unavailable", "reason": str(exc)}

    interpretation = analyze_fundamentals(data)

    return {
        "fundamentals": data,
        "interpretation": interpretation
    }