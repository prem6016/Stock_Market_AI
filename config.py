from dotenv import load_dotenv
import os

load_dotenv()

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
if not GEMINI_API_KEY:
    raise ValueError(
        "GEMINI_API_KEY is not set. Add GEMINI_API_KEY to your environment or .env file."
    )

# Model used for all Gemini calls across the project. Centralized here so it
# only needs to change in one place.
GEMINI_MODEL = os.getenv("GEMINI_MODEL", "gemini-flash-latest")

# Fallback ticker used by CLI scripts when no symbol is passed on the
# command line. Centralized here instead of being duplicated (and risking
# drifting out of sync) across agent.py, stock_agent.py, fundamentals.py,
# and combined_analysis.py.
DEFAULT_SYMBOL = os.getenv("DEFAULT_SYMBOL", "HFCL.NS")

# Minimum number of trading days of history required before indicators
# like SMA200 are considered meaningful.
MIN_HISTORY_DAYS_FOR_SMA200 = 200