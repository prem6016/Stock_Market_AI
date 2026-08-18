# 📈 Stock Market AI

> An AI-powered stock market analysis agent for Indian equities using Google Gemini, Yahoo Finance, technical indicators, fundamental analysis, market context, and recent company news.

[![Python](https://img.shields.io/badge/Python-3.x-blue.svg)](https://www.python.org/)
[![Google Gemini](https://img.shields.io/badge/AI-Google%20Gemini-4285F4.svg)](https://ai.google.dev/)
[![Yahoo Finance](https://img.shields.io/badge/Data-Yahoo%20Finance-6001D2.svg)](https://finance.yahoo.com/)
[![Market](https://img.shields.io/badge/Market-NSE%20%2F%20India-orange.svg)](https://www.nseindia.com/)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

---

## 🚀 Overview

**Stock Market AI** is a Python-based AI stock analysis agent designed primarily for the Indian stock market.

Instead of relying on a single indicator, the project combines multiple sources of information:

* 📊 Current stock price and volume
* 📈 Technical indicators
* 💰 Fundamental financial metrics
* 🇮🇳 Indian market context
* 📰 Recent company news
* 🤖 AI-powered interpretation using Google Gemini

The goal is to provide a concise but comprehensive daily analysis of a stock while clearly separating **market facts from AI interpretation**.

The main AI agent collects the required information through tools and asks Gemini to synthesize the results into a daily stock report.

---

## ✨ Key Features

### 🤖 AI-Powered Stock Analysis

The project uses **Google Gemini** to interpret market information and generate a structured analysis.

The AI is instructed to:

* Use current information from available tools
* Avoid inventing missing information
* Distinguish facts from interpretation
* Avoid unsupported claims
* Avoid guaranteeing future price movements
* Treat the output as analytical research rather than personalized investment advice

---

### 📊 Technical Analysis

The technical-analysis engine uses approximately one year of historical market data and calculates:

* SMA 20
* SMA 50
* SMA 200
* RSI 14
* MACD
* MACD Signal
* Daily Return
* Volume Change
* 20-day Average Volume
* Current Volume vs Average Volume

The project then interprets the indicators to determine the broader technical trend.

For example:

```text
Price > SMA20 > SMA50 > SMA200
        ↓
   Strong Uptrend
```

The RSI interpretation includes:

|         RSI | Interpretation |
| ----------: | -------------- |
|       >= 70 | Overbought     |
|    50–69.99 | Bullish        |
| 30.01–49.99 | Bearish        |
|       <= 30 | Oversold       |

MACD is interpreted by comparing the MACD line with the signal line.

---

### 💰 Fundamental Analysis

The project retrieves fundamental information using Yahoo Finance.

Currently supported metrics include:

* Market Capitalization
* P/E Ratio
* Forward P/E
* EPS
* Revenue
* Revenue Growth
* Net Income
* Profit Margin
* ROE
* Debt-to-Equity
* Free Cash Flow
* Dividend Yield

The fundamental-analysis layer provides simple interpretations for:

* Valuation
* Profitability
* Revenue Growth
* Leverage

Example:

```text
P/E <= 15       → Low valuation
P/E <= 25       → Moderate valuation
P/E <= 40       → High valuation
P/E > 40        → Very high valuation
```

---

### 🇮🇳 Indian Market Context

The AI agent also checks the broader Indian market using:

* **NIFTY 50**
* **Bank NIFTY**

For each index, the system retrieves:

* Current price
* Previous close

This gives the AI additional market context before generating the stock analysis.

---

### 📰 Recent Company News

The project uses Google Search through Gemini to research recent company-specific news.

The news analysis focuses on the previous **7 days** and looks for:

* Company announcements
* Financial results
* Orders and contracts
* Management changes
* Regulatory developments
* Major business developments
* Important sector developments

The AI is explicitly instructed not to invent news and to report when no meaningful recent news is found.

---

## 🧠 Architecture

The project follows a tool-based AI-agent architecture.

```text
                         ┌──────────────────────┐
                         │       User           │
                         │  Stock Symbol Input  │
                         └──────────┬───────────┘
                                    │
                                    ▼
                         ┌──────────────────────┐
                         │     agent.py         │
                         │   Gemini AI Agent    │
                         └──────────┬───────────┘
                                    │
                ┌───────────────────┼───────────────────┐
                │                   │                   │
                ▼                   ▼                   ▼
       ┌────────────────┐  ┌────────────────┐  ┌────────────────┐
       │ Stock Price    │  │ Market Context │  │ Technical      │
       │ Tool           │  │ Tool           │  │ Analysis Tool  │
       └───────┬────────┘  └───────┬────────┘  └───────┬────────┘
               │                   │                   │
               ▼                   ▼                   ▼
          Yahoo Finance        NIFTY 50             SMA / RSI
                              Bank NIFTY              MACD
                                                        │
                                                        ▼
                                              ┌────────────────┐
                                              │ Fundamental    │
                                              │ Analysis       │
                                              └───────┬────────┘
                                                      │
                                                      ▼
                                              ┌────────────────┐
                                              │ Company News   │
                                              │ Google Search  │
                                              └───────┬────────┘
                                                      │
                                                      ▼
                                           ┌────────────────────┐
                                           │   Google Gemini    │
                                           │ AI Synthesis       │
                                           └─────────┬──────────┘
                                                     │
                                                     ▼
                                           ┌────────────────────┐
                                           │ Daily Stock Report │
                                           └────────────────────┘
```

---

## 📁 Project Structure

```text
Stock_Market_AI/
│
├── agent.py
│
├── ai_analysis.py
├── analysis.py
├── combined_analysis.py
│
├── config.py
│
├── fundamental_analysis.py
├── fundamentals.py
├── stock_agent.py
│
├── tools/
│   ├── stock.py
│   ├── market.py
│   ├── technical.py
│   ├── fundamentals.py
│   └── news.py
│
├── .gitignore
│
└── README.md
```

### File Responsibilities

| File                      | Purpose                                              |
| ------------------------- | ---------------------------------------------------- |
| `agent.py`                | Main Gemini-powered stock analysis agent             |
| `config.py`               | Loads environment variables and Gemini API key       |
| `stock_agent.py`          | Historical data retrieval and technical calculations |
| `analysis.py`             | Technical indicator interpretation                   |
| `ai_analysis.py`          | Gemini-based technical analysis                      |
| `fundamentals.py`         | Retrieves company fundamentals                       |
| `fundamental_analysis.py` | Interprets fundamental metrics                       |
| `combined_analysis.py`    | Combines technical and fundamental analysis          |
| `tools/stock.py`          | Current stock price and volume tool                  |
| `tools/market.py`         | NIFTY and Bank NIFTY market context                  |
| `tools/technical.py`      | Technical-analysis tool exposed to Gemini            |
| `tools/fundamentals.py`   | Fundamental-analysis tool exposed to Gemini          |
| `tools/news.py`           | Recent company-news research tool                    |

---

# 🛠️ Technology Stack

| Technology       | Purpose                            |
| ---------------- | ---------------------------------- |
| Python           | Core programming language          |
| Google Gemini    | AI reasoning and report generation |
| Google GenAI SDK | Gemini API integration             |
| Yahoo Finance    | Stock and market data              |
| yfinance         | Python interface to Yahoo Finance  |
| Pandas           | Data processing                    |
| `ta`             | Technical indicators               |
| Google Search    | Recent company-news research       |
| python-dotenv    | Environment variable management    |

---

# 📋 Requirements

Before running the project, make sure you have:

* Python 3.x
* Internet connectivity
* A Google Gemini API key
* `pip`
* Access to Yahoo Finance data

---

# ⚙️ Installation

## 1. Clone the Repository

```bash
git clone https://github.com/prem6016/Stock_Market_AI.git
```

Move into the project directory:

```bash
cd Stock_Market_AI
```

---

## 2. Create a Virtual Environment

### Linux / macOS

```bash
python3 -m venv venv
source venv/bin/activate
```

### Windows

```powershell
python -m venv venv
venv\Scripts\activate
```

---

## 3. Install Dependencies

Install the required Python packages:

```bash
pip install google-genai yfinance pandas ta python-dotenv
```

You can also create a `requirements.txt` file:

```text
google-genai
yfinance
pandas
ta
python-dotenv
```

Then install them with:

```bash
pip install -r requirements.txt
```

---

# 🔐 API Configuration

The project uses the Gemini API.

Create a `.env` file in the project root:

```env
GEMINI_API_KEY=your_gemini_api_key_here
```

Example:

```text
Stock_Market_AI/
├── .env
├── agent.py
├── config.py
└── ...
```

The project loads the API key using `python-dotenv`.

The configuration module checks that the API key exists before starting the application.

---

## 🔒 Protect Your API Key

**Never commit `.env` to GitHub.**

Add this to `.gitignore`:

```gitignore
.env
venv/
__pycache__/
*.pyc
```

If you accidentally expose an API key publicly, revoke it immediately and generate a new one.

---

# ▶️ Running the Project

The primary entry point is:

```bash
python agent.py
```

If no symbol is provided, the current implementation uses:

```text
HFCL.NS
```

as the default symbol.

---

## 🔎 Analyze a Specific Stock

Pass an NSE ticker as a command-line argument:

```bash
python agent.py HINDCOPPER.NS
```

Other examples:

```bash
python agent.py RELIANCE.NS
```

```bash
python agent.py TCS.NS
```

```bash
python agent.py INFY.NS
```

```bash
python agent.py SBIN.NS
```

```bash
python agent.py HDFCBANK.NS
```

For NSE-listed stocks, use the `.NS` suffix.

Example:

```text
RELIANCE.NS
TCS.NS
INFY.NS
HDFCBANK.NS
```

---

# 📊 Example Workflow

When you run:

```bash
python agent.py HINDCOPPER.NS
```

the agent performs the following workflow:

### Step 1 — Identify the Stock

The command-line argument is converted to uppercase.

```text
HINDCOPPER.NS
```

---

### Step 2 — Retrieve Current Market Data

The stock tool retrieves recent Yahoo Finance data and extracts:

```text
Price
Volume
Date
```

---

### Step 3 — Analyze Technical Indicators

Historical data is retrieved for approximately one year.

The system calculates:

```text
SMA20
SMA50
SMA200
RSI
MACD
MACD Signal
Daily Return
Volume Change
Average Volume
Volume vs Average
```

---

### Step 4 — Analyze Fundamentals

The system retrieves available company financial information.

For example:

```text
Market Cap
P/E
Forward P/E
EPS
Revenue
Revenue Growth
Profit
Profit Margin
ROE
Debt-to-Equity
Free Cash Flow
Dividend Yield
```

---

### Step 5 — Check Indian Market Conditions

The system checks:

```text
NIFTY 50
Bank NIFTY
```

and compares the latest price with the previous close.

---

### Step 6 — Research Recent News

Gemini uses Google Search to identify relevant company news from approximately the previous seven days.

---

### Step 7 — AI Synthesis

Gemini combines the available information and produces a daily analysis.

The final report is designed to cover:

```text
Current Price
Technical Indicators
Fundamental Health
Indian Market Context
Recent Company News
Risk
Overall Assessment
```

---

# 🤖 AI Technical Analysis Output

The standalone AI technical-analysis module returns structured JSON containing:

```json
{
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
    "signal to monitor"
  ],
  "overall_assessment": "Overall technical assessment",
  "confidence": 75
}
```

The confidence score is constrained to:

```text
0 - 100
```

---

# 📈 Technical Indicators

## SMA

Simple Moving Averages are calculated for:

```text
SMA20
SMA50
SMA200
```

The project uses their relationship with the current price to classify the trend.

### Strong Uptrend

```text
Price > SMA20 > SMA50 > SMA200
```

### Strong Downtrend

```text
Price < SMA20 < SMA50 < SMA200
```

### Long-Term Bullish

```text
Price > SMA200
```

Otherwise:

```text
Weak/Mixed
```

---

## RSI

The project uses a 14-period RSI.

```text
RSI >= 70       → Overbought
RSI 50–69.99    → Bullish
RSI 30.01–49.99 → Bearish
RSI <= 30       → Oversold
```

---

## MACD

The project compares:

```text
MACD
MACD Signal
```

Interpretation:

```text
MACD > Signal → Bullish

MACD < Signal → Bearish

MACD = Signal → Neutral
```

---

# 💰 Fundamental Metrics

The project currently retrieves the following metrics where Yahoo Finance provides them:

```text
Market Capitalization
Trailing P/E
Forward P/E
EPS
Revenue
Revenue Growth
Net Income
Profit Margin
ROE
Debt-to-Equity
Free Cash Flow
Dividend Yield
```

The fundamental interpretation layer categorizes:

### Valuation

```text
P/E <= 15 → Low valuation
P/E <= 25 → Moderate valuation
P/E <= 40 → High valuation
P/E > 40  → Very high valuation
```

### ROE

```text
ROE >= 20% → Strong
ROE >= 12% → Moderate
ROE < 12%  → Weak
```

### Revenue Growth

```text
>= 15% → Strong growth
>= 5%  → Moderate growth
>= 0%  → Low growth
< 0%   → Declining
```

### Debt-to-Equity

```text
<= 50  → Low leverage
<= 100 → Moderate leverage
> 100  → High leverage
```

These are simplified classification rules intended for research and should not be interpreted as complete financial-health assessments.

---

# 📰 News Analysis

The news tool asks Gemini to search for recent information related to the selected NSE company.

The search focuses on approximately the last seven days.

Relevant categories include:

* Company announcements
* Earnings/results
* Orders
* Contracts
* Management changes
* Regulatory developments
* Business developments
* Sector developments

The system is instructed to avoid fabricated information.

---

# 🧩 Gemini Tool Architecture

The main agent exposes multiple Python functions to Gemini.

```python
tools = [
    get_stock_price,
    get_market_context,
    get_technical_analysis,
    get_fundamental_analysis,
    get_company_news
]
```

Gemini can therefore decide which information it needs to complete the analysis.

Conceptually:

```text
                    Gemini
                       │
        ┌──────────────┼───────────────┐
        │              │               │
        ▼              ▼               ▼
   Stock Price      Technical      Fundamentals
        │              │               │
        └──────────────┼───────────────┘
                       │
                       ▼
                Market Context
                       │
                       ▼
                  Company News
                       │
                       ▼
                Final Analysis
```

---

# 🧪 Running Individual Components

## Technical Analysis

You can run the technical-analysis module directly:

```bash
python stock_agent.py
```

The module retrieves approximately one year of data and calculates the configured technical indicators.

---

## Fundamental Analysis

Run:

```bash
python fundamentals.py
```

This retrieves the configured fundamental metrics and prints their interpretations.

---

## Combined Analysis

Run:

```bash
python combined_analysis.py
```

The combined-analysis module brings together:

```text
Technical Analysis
+
Fundamentals
+
Fundamental Interpretation
```

---

# 🛡️ Analysis Principles

The AI agent follows several safeguards.

### No fabricated data

The model is instructed not to invent missing information.

### Facts vs interpretation

Market data should be treated as facts, while conclusions are interpretations.

### No unsupported institutional-flow claims

High volume alone should not be interpreted as proof of institutional buying or selling.

### No single-metric solvency claims

A single debt-related ratio should not be treated as definitive proof of financial strength or weakness.

### No guaranteed predictions

The system does not guarantee future stock-price movements.

### Recent-news validation

News should be relevant to the selected company and recent enough to matter.

---

# ⚠️ Limitations

This project is a research and educational tool.

Important limitations include:

* Yahoo Finance data availability can vary.
* Some fundamental fields may be unavailable or `None`.
* Market data can be delayed depending on the underlying data source.
* Technical indicators are based on historical price/volume data.
* AI-generated interpretations can contain errors.
* News retrieval depends on available search results.
* Fundamental classification rules are simplified.
* The system does not perform complete professional equity research.
* The system does not guarantee profitable trading decisions.
* Historical patterns do not guarantee future performance.

---

# 🔮 Future Improvements

The project can be extended significantly.

## 📊 More Technical Indicators

Potential additions:

* EMA
* Bollinger Bands
* ATR
* Stochastic RSI
* ADX
* OBV
* VWAP
* Fibonacci levels

---

## 💰 More Fundamental Analysis

Possible additions:

* PEG ratio
* ROIC
* Current ratio
* Quick ratio
* Operating margin
* EBITDA margin
* Earnings growth
* Cash-flow trends
* Promoter holding
* Institutional ownership
* Quarterly results
* Balance-sheet trends

---

## 📰 Advanced News Intelligence

Future versions could add:

* News sentiment scoring
* Positive/negative/neutral classification
* News impact scoring
* Earnings-event detection
* Regulatory-event detection
* Sector sentiment
* Duplicate-news filtering

---

## 🧠 Multi-Agent Architecture

The current project can evolve into a true multi-agent financial research system.

For example:

```text
                 ┌─────────────────┐
                 │ Orchestrator AI │
                 └────────┬────────┘
                          │
        ┌─────────────────┼──────────────────┐
        │                 │                  │
        ▼                 ▼                  ▼
 ┌─────────────┐   ┌─────────────┐   ┌─────────────┐
 │ Technical   │   │ Fundamental │   │ News        │
 │ Agent       │   │ Agent       │   │ Agent       │
 └──────┬──────┘   └──────┬──────┘   └──────┬──────┘
        │                 │                  │
        └─────────────────┼──────────────────┘
                          ▼
                 ┌─────────────────┐
                 │ Risk Agent      │
                 └────────┬────────┘
                          ▼
                 ┌─────────────────┐
                 │ Report Agent    │
                 └─────────────────┘
```

---

## 📈 Backtesting

A future version could evaluate the strategy against historical data.

Potential metrics:

* CAGR
* Total Return
* Sharpe Ratio
* Sortino Ratio
* Maximum Drawdown
* Win Rate
* Profit Factor
* Number of Trades

---

## 📋 Stock Screening

A market scanner could analyze multiple NSE stocks:

```text
NIFTY 50
NIFTY 100
NIFTY 500
Sector indices
Custom watchlists
```

Example:

```bash
python scanner.py --index nifty50
```

---

## 📄 Automated Reports

Future versions could generate:

```text
Daily Markdown Report
PDF Report
HTML Dashboard
Email Report
Telegram Alert
WhatsApp Notification
```

---

## 📊 Web Dashboard

A Streamlit or Flask dashboard could provide:

```text
┌──────────────────────────────────────────────┐
│             STOCK MARKET AI                  │
├──────────────────────────────────────────────┤
│ Symbol: HINDCOPPER.NS                        │
│                                              │
│ Price          ₹XXX                          │
│ Trend          Strong Uptrend                │
│ RSI            XX                            │
│ MACD           Bullish                       │
│                                              │
│ Fundamental Health                           │
│ ███████████████░░░                           │
│                                              │
│ AI Assessment                                │
│ Bullish / Bearish / Mixed                    │
└──────────────────────────────────────────────┘
```

---

# 🐳 Docker Deployment

The project can also be containerized in a future deployment.

Example architecture:

```text
                   Internet
                       │
                       ▼
                ┌─────────────┐
                │ API / UI    │
                └──────┬──────┘
                       │
                       ▼
                ┌─────────────┐
                │ Stock AI    │
                │ Agent       │
                └──────┬──────┘
                       │
          ┌────────────┼─────────────┐
          ▼            ▼             ▼
      Yahoo Finance  Gemini       News Search
```

A production deployment could use:

* Docker
* Docker Compose
* AWS ECS
* AWS Fargate
* CloudWatch
* Grafana
* Prometheus
* GitHub Actions

---

# 🔐 Security Recommendations

Never hard-code API keys.

Bad:

```python
GEMINI_API_KEY = "AIza..."
```

Good:

```python
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
```

Use:

```text
.env
```

for local development and environment/secret management services for production.

For AWS deployments, consider:

* AWS Secrets Manager
* AWS Systems Manager Parameter Store
* IAM roles
* ECS task secrets

---

# 🧑‍💻 Development

Create a branch:

```bash
git checkout -b feature/new-analysis
```

Make your changes:

```bash
git add .
git commit -m "Add new analysis feature"
```

Push:

```bash
git push origin feature/new-analysis
```

Then open a Pull Request.

---

# 🤝 Contributing

Contributions are welcome.

Possible areas for contribution:

* New technical indicators
* Better fundamental scoring
* Improved news analysis
* Backtesting
* Portfolio analysis
* Risk management
* Web dashboard
* Docker deployment
* AWS deployment
* Automated reporting
* Testing
* Performance improvements
Before submitting a Pull Request:

1. Test your changes.
2. Keep API keys and secrets out of commits.
3. Update the documentation when necessary.
4. Explain the purpose of the change.
5. Keep changes focused.

---

# 🐛 Issues

If you encounter a bug, please open a GitHub Issue and include:

```text
Python version
Operating system
Command executed
Stock symbol
Error message
Relevant logs
```

Do not include:

```text
API keys
Passwords
Access tokens
Private credentials
```

---

# 📜 Disclaimer

> **IMPORTANT: This project is for educational and research purposes only.**

Stock market analysis generated by this project should **not** be considered financial, investment, trading, or professional advice.

The project uses historical market data, financial information, technical indicators, news information, and AI-generated interpretations.

AI-generated analysis may be inaccurate, incomplete, delayed, or incorrect.

Past performance does not guarantee future results.

Do your own research and, where appropriate, consult a qualified financial professional before making investment decisions.

**Never invest money you cannot afford to lose.**

The author and contributors are not responsible for financial losses resulting from the use of this software.

---

# ⭐ Support the Project

If you find this project useful:

* ⭐ Star the repository
* 🍴 Fork the repository
* 🐛 Report bugs
* 💡 Suggest improvements
* 🔧 Submit Pull Requests

Repository:

https://github.com/prem6016/Stock_Market_AI

---

# 🙏 Acknowledgements

This project makes use of several excellent open-source and public technologies:

* [Google Gemini](https://ai.google.dev/)
* [Google GenAI SDK](https://github.com/googleapis/python-genai)
* [Yahoo Finance](https://finance.yahoo.com/)
* [yfinance](https://github.com/ranaroussi/yfinance)
* [Pandas](https://pandas.pydata.org/)
* [Technical Analysis Library](https://github.com/bukosabino/ta)
* [Python](https://www.python.org/)

---

# 👨‍💻 Author

## Prem Sarkar

Cloud & DevOps Engineer | AWS | Docker | Linux | Python | AI

GitHub:

https://github.com/prem6016

Project:

https://github.com/prem6016/Stock_Market_AI

---

## 📌 Project Status

**Current Status:** 🚧 Active Development

The current version provides an AI-powered command-line stock analysis workflow combining:

```text
Yahoo Finance
      +
Technical Analysis
      +
Fundamental Analysis
      +
Indian Market Context
      +
Recent Company News
      +
Google Gemini
      ↓
AI Stock Analysis
```

Future releases can expand this into a complete AI-powered Indian equity research and market-intelligence platform.

---

## ⭐ If You Like This Project

Give the repository a ⭐ and follow the project for future improvements.

**Built with Python 🐍 + AI 🤖 + Market Data 📈**
