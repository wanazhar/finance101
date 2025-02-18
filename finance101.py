import requests
import yfinance as yf
import pandas as pd
import time
import os

# ASCII Art Header
HEADER = """
███████╗██╗███╗   ██╗ █████╗ ███╗   ██╗ ██████╗███████╗     ██╗ ██████╗  ██╗
██╔════╝██║████╗  ██║██╔══██╗████╗  ██║██╔════╝██╔════╝    ███║██╔═████╗███║
█████╗  ██║██╔██╗ ██║███████║██╔██╗ ██║██║     █████╗      ╚██║██║██╔██║╚██║
██╔══╝  ██║██║╚██╗██║██╔══██║██║╚██╗██║██║     ██╔══╝       ██║████╔╝██║ ██║
██║     ██║██║ ╚████║██║  ██║██║ ╚████║╚██████╗███████╗     ██║╚██████╔╝ ██║
╚═╝     ╚═╝╚═╝  ╚═══╝╚═╝  ╚═╝╚═╝  ╚═══╝ ╚═════╝╚══════╝     ╚═╝ ╚═════╝  ╚═╝
"""
CREDITS = "vibecoded by wanazhar. 2025. mit license.\n"

# Knowledge Library
KNOWLEDGE_LIBRARY = {
    "P/E Ratio": "Price-to-Earnings Ratio: Measures how expensive a stock is relative to its earnings.",
    "P/B Ratio": "Price-to-Book Ratio: Compares a company's market value to its book value.",
    "ROE": "Return on Equity: Measures profitability by showing how much profit is generated from shareholders' equity.",
    "EPS": "Earnings Per Share: Profit allocated to each share of stock.",
    "EV/EBITDA": "Enterprise Value to EBITDA: Used to value a company including its debt and cash."
}

# Function to fetch company data
def fetch_company_data(ticker):
    try:
        stock = yf.Ticker(ticker)
        info = stock.info
        return {
            "Company Name": info.get("longName", "N/A"),
            "Sector": info.get("sector", "N/A"),
            "Industry": info.get("industry", "N/A"),
            "Market Cap ($B)": f"{info.get('marketCap', 0) / 1e9:,.2f}B",
            "P/E Ratio": info.get("trailingPE", "N/A"),
            "P/B Ratio": info.get("priceToBook", "N/A"),
            "ROE": f"{info.get('returnOnEquity', 0) * 100:.2f}%" if info.get("returnOnEquity") else "N/A",
            "EPS": info.get("trailingEps", "N/A"),
            "EV/EBITDA": info.get("enterpriseToEbitda", "N/A")
        }
    except Exception as e:
        return {"Error": str(e)}

# Function to display a single stock's details
def single_ticker_analysis():
    ticker = input("Enter stock ticker (e.g., AAPL): ").upper()
    data = fetch_company_data(ticker)
    print("\n--- Company Profile ---")
    for key, value in data.items():
        print(f"{key}: {value}")
    print("\nReturning to Main Menu...\n")
    time.sleep(2)

# Function to compare multiple stocks
def multi_ticker_comparison():
    tickers = input("Enter tickers separated by commas (e.g., AAPL, TSLA, MSFT): ").upper().split(",")
    tickers = [t.strip() for t in tickers]
    
    print("\n--- Multi-Ticker Comparison ---")
    df = pd.DataFrame([fetch_company_data(ticker) for ticker in tickers], index=tickers)
    print(df)
    
    print("\nReturning to Main Menu...\n")
    time.sleep(2)

# Function to fetch historical prices
def historical_prices():
    ticker = input("Enter stock ticker (e.g., AAPL): ").upper()
    print("Choose time range:")
    print("1: Last 6 months")
    print("2: Custom date range")
    
    choice = input("Select an option (1-2): ")
    
    stock = yf.Ticker(ticker)
    
    if choice == "1":
        df = stock.history(period="6mo")
    elif choice == "2":
        start_date = input("Enter start date (YYYY-MM-DD): ")
        end_date = input("Enter end date (YYYY-MM-DD): ")
        df = stock.history(start=start_date, end=end_date)
    else:
        print("Invalid option. Returning to Main Menu.")
        return
    
    print("\n--- Historical Prices ---")
    print(df[['Open', 'High', 'Low', 'Close', 'Volume']].tail(10))
    
    print("\nReturning to Main Menu...\n")
    time.sleep(2)

# Function to display knowledge library
def knowledge_library():
    print("\n--- Knowledge Library ---")
    for term, explanation in KNOWLEDGE_LIBRARY.items():
        print(f"\n{term}: {explanation}")
    
    print("\nReturning to Main Menu...\n")
    time.sleep(3)

# Main Menu
def main_menu():
    while True:
        os.system("clear" if os.name == "posix" else "cls")
        print(HEADER)
        print(CREDITS)
        print("1️⃣ Single Ticker Analysis")
        print("2️⃣ Multi-Ticker Comparison")
        print("3️⃣ Historical Prices")
        print("4️⃣ Knowledge Library")
        print("5️⃣ Exit")
        
        choice = input("\nSelect an option (1-5): ")
        
        if choice == "1":
            single_ticker_analysis()
        elif choice == "2":
            multi_ticker_comparison()
        elif choice == "3":
            historical_prices()
        elif choice == "4":
            knowledge_library()
        elif choice == "5":
            print("Exiting Finance101... Goodbye!")
            break
        else:
            print("Invalid option. Try again.")

# Run Program
if __name__ == "__main__":
    main_menu()
