from stock_agent import analyze_stock
from fundamentals import get_fundamentals
from fundamental_analysis import analyze_fundamentals


def analyze_company(symbol):

    technical = analyze_stock(symbol)

    fundamentals = get_fundamentals(symbol)

    fundamental_interpretation = analyze_fundamentals(
        fundamentals
    )

    return {
        "symbol": symbol,

        "technical": technical,

        "fundamentals": fundamentals,

        "fundamental_analysis":
            fundamental_interpretation
    }


if __name__ == "__main__":

    symbol = "HFCL.NS"

    result = analyze_company(symbol)

    print("\n===================================")
    print("        COMBINED ANALYSIS")
    print("===================================\n")

    print(result)