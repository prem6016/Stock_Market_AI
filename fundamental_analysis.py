def interpret_pe(pe):
    if pe is None:
        return "Unavailable"

    if pe <= 15:
        return "Low valuation"

    elif pe <= 25:
        return "Moderate valuation"

    elif pe <= 40:
        return "High valuation"

    else:
        return "Very high valuation"


def interpret_roe(roe):
    if roe is None:
        return "Unavailable"

    roe_percent = roe * 100

    if roe_percent >= 20:
        return "Strong"

    elif roe_percent >= 12:
        return "Moderate"

    else:
        return "Weak"


def interpret_revenue_growth(growth):
    if growth is None:
        return "Unavailable"

    growth_percent = growth * 100

    if growth_percent >= 15:
        return "Strong growth"

    elif growth_percent >= 5:
        return "Moderate growth"

    elif growth_percent >= 0:
        return "Low growth"

    else:
        return "Declining"


def interpret_debt(debt):
    """Interpret a debt-to-equity ratio.

    NOTE: yfinance's `debtToEquity` field is expressed as a percentage
    (e.g. a value of 45 means a D/E ratio of 0.45), which is what the
    thresholds below assume. If the data source ever changes, these
    thresholds need to be revisited.
    """
    if debt is None:
        return "Unavailable"

    if debt <= 50:
        return "Low leverage"

    elif debt <= 100:
        return "Moderate leverage"

    else:
        return "High leverage"


def analyze_fundamentals(data):

    return {
        "valuation": interpret_pe(
            data.get("pe_ratio")
        ),

        "profitability": interpret_roe(
            data.get("roe")
        ),

        "growth": interpret_revenue_growth(
            data.get("revenue_growth")
        ),

        "leverage": interpret_debt(
            data.get("debt_to_equity")
        )
    }