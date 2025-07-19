#Python Code — 'sma_backtest.py'

import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt

# Fetch historical data
ticker = "AAPL"
data = yf.download(ticker, start="2024-01-01", end="2025-01-01")

# Calculate Moving Averages
data['SMA20'] = data['Close'].rolling(window=20).mean()
data['SMA50'] = data['Close'].rolling(window=50).mean()

# Define Signals: 1 for Buy, -1 for Sell
data['Signal'] = 0
data.loc[data['SMA20'] > data['SMA50'], 'Signal'] = 1
data.loc[data['SMA20'] < data['SMA50'], 'Signal'] = -1

# Plotting
plt.figure(figsize=(12,6))
plt.plot(data['Close'], label='Close Price', color='blue')
plt.plot(data['SMA20'], label='SMA20', color='green')
plt.plot(data['SMA50'], label='SMA50', color='red')
plt.title(f'{ticker} SMA Crossover Backtesting')
plt.xlabel('Date')
plt.ylabel('Price (USD)')
plt.legend()

plt.show()

# Show last few signals
print(data[['Close', 'SMA20', 'SMA50', 'Signal']].tail())
