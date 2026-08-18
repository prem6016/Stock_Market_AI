from google import genai
from google.genai import types

from config import GEMINI_API_KEY, GEMINI_MODEL


def _get_genai_client():
    # Lazily instantiated so importing this module doesn't require a valid
    # API key / network access unless the tool is actually called.
    return genai.Client(api_key=GEMINI_API_KEY)


def get_company_news(symbol: str):
    """Search for and summarize recent (last 7 days) news about an Indian
    listed company using Google Search grounding.

    Args:
        symbol: NSE ticker symbol, e.g. "HFCL.NS".
    """

    client = _get_genai_client()

    prompt = f"""
Find recent and relevant news about the Indian listed company
represented by the NSE symbol {symbol}.

Focus on news from the last 7 days.

Look for:
- Company announcements
- Financial results
- Orders and contracts
- Management changes
- Regulatory developments
- Major business developments
- Important sector developments affecting the company

Do not invent information.

For each relevant article provide:
- headline
- source
- publication date
- short summary

If no meaningful recent news is found, say so.
"""

    response = client.models.generate_content(
        model=GEMINI_MODEL,
        contents=prompt,
        config=types.GenerateContentConfig(
            tools=[
                types.Tool(
                    google_search=types.GoogleSearch()
                )
            ]
        )
    )

    return response.text or "No news response returned."