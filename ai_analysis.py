from google import genai
from config import GEMINI_API_KEY
import json


def _get_genai_client():
    return genai.Client(api_key=GEMINI_API_KEY)


def get_ai_analysis(stock_data):
    client = _get_genai_client()

    prompt = f"""
You are a financial technical-analysis assistant.

Analyze the following calculated stock data.

IMPORTANT:
- Do not invent missing information.
- Use only the supplied data.
- Clearly distinguish facts from interpretation.
- Do not guarantee future price movement.
- This is technical analysis, not personalized investment advice.

STOCK DATA:
{json.dumps(stock_data, indent=2)}

Analyze:
- Overall trend
- Momentum
- RSI
- MACD
- Volume confirmation
- Conflicting signals
- Risk
- Important signals to monitor

Return your analysis as JSON with exactly this structure:

{{
    "summary": "Short summary",
    "bullish_signals": [
        "signal 1",
        "signal 2"
    ],
    "bearish_signals": [
        "signal 1",
        "signal 2"
    ],
    "risk": "Risk assessment",
    "key_signals": [
        "signal to monitor 1",
        "signal to monitor 2"
    ],
    "overall_assessment": "Overall technical assessment",
    "confidence": 0
}}

The confidence must be an integer from 0 to 100.
"""

    response = client.models.generate_content(
        model="gemini-flash-latest",
        contents=prompt,
        config={
            "response_mime_type": "application/json"
        }
    )

    return json.loads(response.text)