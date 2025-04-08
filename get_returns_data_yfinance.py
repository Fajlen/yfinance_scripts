import yfinance as yf
import pandas as pd

# Define the ticker symbol
ticker_symbol = "GME"
#Start and end dates
start_date = "2021-01-01"
end_date = "2021-12-31"

# Retrieve historical data
# Corrected the period argument to use a string
data = yf.download(ticker_symbol, start=start_date, end=end_date)[["Open", "Close", "Volume"]]

# Reset index to move Date from index to column
data.reset_index(inplace=True)

# Save the historical data to a CSV file
# Corrected to use the resulting DataFrame
filename = "blablabla.csv"
data.to_csv(filename, index=False)

print(f"stock data from {start_date} to {end_date} saved to {filename}")
