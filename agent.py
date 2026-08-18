import sys

from google import genai
from config import GEMINI_API_KEY, GEMINI_MODEL, DEFAULT_SYMBOL

from tools.stock import get_stock_price
from tools.market import get_market_context
from tools.technical import get_technical_analysis
from tools.fundamentals import get_fundamental_analysis
from tools.news import get_company_news


def build_prompt(symbol: str) -> str:
    return f"""
Perform a complete daily analysis of {symbol}.

Collect the information you need using the available tools.

Analyze:

1. Current price
2. Technical indicators
3. Fundamental health
4. Indian market context
5. Recent company news

Important rules:

- Use current data from the tools.
- Do not invent missing information.
- Clearly distinguish facts from interpretation.
- Do not claim institutional buying or selling based only on volume.
- Do not claim that a particular debt ratio proves low or high solvency risk by itself.
- Treat news as relevant only when it is recent and actually related to {symbol}.
- Do not guarantee future price movement.
- This is an analytical report, not personalized investment advice.

Provide a concise but detailed daily report.
"""


def run_daily_analysis(symbol: str) -> str:
    client = genai.Client(api_key=GEMINI_API_KEY)

    tools = [
        get_stock_price,
        get_market_context,
        get_technical_analysis,
        get_fundamental_analysis,
        get_company_news
    ]

    response = client.models.generate_content(
        model=GEMINI_MODEL,
        contents=build_prompt(symbol),
        config={
            "tools": tools
        }
    )

    return response.text


def main():
    symbol = sys.argv[1].upper() if len(sys.argv) > 1 else DEFAULT_SYMBOL

    try:
        report = run_daily_analysis(symbol)
    except Exception as exc:
        print(f"Error generating analysis for {symbol}: {exc}")
        sys.exit(1)

    print(report)


if __name__ == "__main__":
    main()
