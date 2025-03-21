def analyze_financials(financials):
    """
    Analyzes financial data to determine investment potential.
    
    Args:
        financials (dict): Financial data fetched from fetcher.py.
    
    Returns:
        str: Investment recommendation ('Buy', 'Hold', 'Sell').
    """
    try:
        info = financials.get("info", {})
        pe_ratio = info.get("trailingPE", None)
        debt_to_equity = info.get("debtToEquity", None)
        revenue_growth = info.get("revenueGrowth", None)

        # Example rules for analysis
        if pe_ratio and pe_ratio < 15 and debt_to_equity and debt_to_equity < 1:
            return "Buy"
        elif revenue_growth and revenue_growth > 0.1:
            return "Hold"
        else:
            return "Sell"
    except Exception as e:
        print(f"Error analyzing financials: {e}")
        return "Error"