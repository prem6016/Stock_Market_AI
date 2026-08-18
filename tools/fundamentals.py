from fundamentals import get_fundamentals
from fundamental_analysis import analyze_fundamentals


def get_fundamental_analysis(symbol: str):

    data = get_fundamentals(symbol)

    interpretation = analyze_fundamentals(data)

    return {
        "fundamentals": data,
        "interpretation": interpretation
    }