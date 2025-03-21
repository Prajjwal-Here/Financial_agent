from fetcher import fetch_financials
from analyzer import analyze_financials
from utils import log_message

def main():
    print("Welcome to the Warren Buffet Agent!")
    ticker = input("Enter the stock ticker symbol (e.g., AAPL, GOOGL): ").strip().upper()

    log_message(f"Fetching financial data for {ticker}...")
    financials = fetch_financials(ticker)

    if financials:
        log_message(f"Analyzing financial data for {ticker}...")
        recommendation = analyze_financials(financials)
        print(f"Investment Recommendation for {ticker}: {recommendation}")
    else:
        print(f"Failed to fetch financial data for {ticker}. Please try again.")

if __name__ == "__main__":
    main()