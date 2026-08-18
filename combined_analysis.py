import sys
import json

from stock_agent import analyze_stock
from fundamentals import get_fundamentals
from fundamental_analysis import analyze_fundamentals
from config import DEFAULT_SYMBOL


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


def main():
    symbol = sys.argv[1].upper() if len(sys.argv) > 1 else DEFAULT_SYMBOL

    try:
        result = analyze_company(symbol)
    except ValueError as exc:
        print(f"Error: {exc}")
        sys.exit(1)

    print("\n===================================")
    print("        COMBINED ANALYSIS")
    print("===================================\n")

    print(json.dumps(result, indent=2, default=str))


if __name__ == "__main__":
    main()