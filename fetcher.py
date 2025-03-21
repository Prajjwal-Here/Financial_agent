import yfinance as yf

def fetch_financials(ticker):
    """
    Fetches financial data for a given company ticker.
    
    Args:
        ticker (str): Stock ticker symbol (e.g., 'AAPL').
    
    Returns:
        dict: A dictionary containing financial data.
    """
    try:
        stock = yf.Ticker(ticker)
        financials = {
            "balance_sheet": stock.balance_sheet,
            "income_statement": stock.financials,
            "cashflow": stock.cashflow,
            "info": stock.info
        }
        return financials
    except Exception as e:
        print(f"Error fetching data for {ticker}: {e}")
        return None