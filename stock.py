import requests
import pandas as pd

# Function to fetch real-time stock data using Alpha Vantage API
def get_stock_data(symbol, api_key):
    url = f"https://www.alphavantage.co/query?function=GLOBAL_QUOTE&symbol={symbol}&apikey={api_key}"
    response = requests.get(url)
    data = response.json()
    return data['Global Quote']

# Function to add a stock to the portfolio
def add_stock(portfolio, symbol, api_key):
    stock_data = get_stock_data(symbol, api_key)
    if stock_data:
        portfolio[symbol] = stock_data
        print(f"{symbol} added to portfolio successfully.")
    else:
        print(f"Failed to add {symbol} to portfolio.")

# Function to remove a stock from the portfolio
def remove_stock(portfolio, symbol):
    if symbol in portfolio:
        del portfolio[symbol]
        print(f"{symbol} removed from portfolio successfully.")
    else:
        print(f"{symbol} not found in portfolio.")

# Function to display the portfolio
def display_portfolio(portfolio):
    if portfolio:
        df = pd.DataFrame.from_dict(portfolio, orient='index')
        print(df)
    else:
        print("Portfolio is empty.")

# Example usage
if __name__ == "__main__":
    api_key = "YOUR_ALPHA_VANTAGE_API_KEY"
    portfolio = {}

    add_stock(portfolio, "AAPL", api_key)
    add_stock(portfolio, "GOOGL", api_key)
    add_stock(portfolio, "MSFT", api_key)

    display_portfolio(portfolio)

    remove_stock(portfolio, "GOOGL")

    display_portfolio(portfolio)
