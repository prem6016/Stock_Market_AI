from google import genai
from google.genai import types

from config import GEMINI_API_KEY


client = genai.Client(
    api_key=GEMINI_API_KEY
)


def get_company_news(symbol: str):

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
        model="gemini-flash-latest",
        contents=prompt,
        config=types.GenerateContentConfig(
            tools=[
                types.Tool(
                    google_search=types.GoogleSearch()
                )
            ]
        )
    )

    return response.text