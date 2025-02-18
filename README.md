# FINANCE101

## Overview
FINANCE101 is a comprehensive **terminal-based** financial analysis tool that provides various valuation models, company profiles, historical price analysis, and a knowledge library for financial terms and ratios. It is designed for users who want **quick, in-depth stock analysis** without relying on external spreadsheets or web applications.

## Features
- **Single Ticker Analysis:** Input a stock ticker to receive a full breakdown of company valuation using multiple models.
- **Multi-Ticker Comparison:** Compare multiple tickers based on key financial metrics.
- **Historical Prices:** Retrieve stock prices over a specific date range or preset periods (e.g., last six months).
- **Knowledge Library:** Built-in explanations of financial ratios and terms in simplified language.
- **Clean Terminal Output:** Data is formatted for readability, including **comma-separated numbers** and **ASCII charts**.
- **Risk Metrics & Sentiment Analysis:** Includes beta, volatility, and analyst ratings.
- **Company Profile Display:** Shows company description, sector, industry, and key ratios.
- **Fully Terminal-Based:** No external files or web-based dependencies.

## Installation
Ensure you have Python installed on your system.

1. Clone the repository:
   ```sh
   git clone https://github.com/wanazhar/finance101.git
   cd finance101
   ```
2. Install dependencies:
   ```sh
   pip install -r requirements.txt
   ```
3. Run the application:
   ```sh
   python finance101.py
   ```

## Usage
Upon running the script, you will see the main menu:
```
███████╗██╗███╗   ██╗ █████╗ ███╗   ██╗ ██████╗███████╗     ██╗ ██████╗  ██╗
██╔════╝██║████╗  ██║██╔══██╗████╗  ██║██╔════╝██╔════╝    ███║██╔═████╗███║
█████╗  ██║██╔██╗ ██║███████║██╔██╗ ██║██║     █████╗      ╚██║██║██╔██║╚██║
██╔══╝  ██║██║╚██╗██║██╔══██║██║╚██╗██║██║     ██╔══╝       ██║████╔╝██║ ██║
██║     ██║██║ ╚████║██║  ██║██║ ╚████║╚██████╗███████╗     ██║╚██████╔╝ ██║
╚═╝     ╚═╝╚═╝  ╚═══╝╚═╝  ╚═╝╚═╝  ╚═══╝ ╚═════╝╚══════╝     ╚═╝ ╚═════╝  ╚═╝

1️⃣ Single Ticker Analysis
2️⃣ Multi-Ticker Comparison
3️⃣ Historical Prices
4️⃣ Knowledge Library
5️⃣ Exit
```

### 1️⃣ Single Ticker Analysis
- Enter a stock ticker (e.g., `AAPL` for Apple Inc.).
- The script retrieves all valuation metrics, sentiment analysis, and company profile details.

### 2️⃣ Multi-Ticker Comparison
- Input multiple tickers (e.g., `AAPL MSFT TSLA`).
- The script compares financials side by side, displaying key indicators.

### 3️⃣ Historical Prices
- Input a ticker and a date range (YYYY-MM-DD format).
- Alternatively, choose from preset periods (e.g., `last 6 months`).

### 4️⃣ Knowledge Library
- Browse definitions and explanations of financial ratios and key investment terms.

### 5️⃣ Exit
- Close the program at any time.

## Example Output
```
Company: Apple Inc. (AAPL)
Sector: Technology | Industry: Consumer Electronics
Market Cap: $2,500,000,000,000
P/E Ratio: 30.45 | EPS: $5.28
Dividend Yield: 0.65% | Payout Ratio: 22%
Beta: 1.12 (Moderate Risk)
Analyst Rating: Strong Buy (84% Positive)
```

## License
**MIT License**

---

For any issues or feature requests, open a GitHub issue or contact me directly.

