import yfinance as yf
from fundamental_analysis import analyze_fundamentals

def get_fundamentals(symbol):

    stock = yf.Ticker(symbol)

    info = stock.info

    fundamentals = {
        "symbol": symbol,

        "market_cap": info.get("marketCap"),
        "pe_ratio": info.get("trailingPE"),
        "forward_pe": info.get("forwardPE"),

        "eps": info.get("trailingEps"),

        "revenue": info.get("totalRevenue"),
        "revenue_growth": info.get("revenueGrowth"),

        "profit": info.get("netIncomeToCommon"),

        "profit_margin": info.get("profitMargins"),

        "roe": info.get("returnOnEquity"),

        "debt_to_equity": info.get("debtToEquity"),

        "free_cash_flow": info.get("freeCashflow"),

        "dividend_yield": info.get("dividendYield"),
    }

    return fundamentals


if __name__ == "__main__":

    symbol = "HFCL.NS"

    data = get_fundamentals(symbol)

    print("\n========== FUNDAMENTALS ==========\n")

    for key, value in data.items():
        print(f"{key}: {value}")

    analysis = analyze_fundamentals(data)

    print("\n========== FUNDAMENTAL ANALYSIS ==========\n")

    for key, value in analysis.items():
        print(f"{key}: {value}")