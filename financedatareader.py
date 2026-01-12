# this is for financial data reader study
# in English, the data that can be obtained from stocks, such as stock prices, trading volumes, financial statements, investment indicators, etc.
# There is also a method called crawling, which is one way to obtain stock data.
# We can also use API to get the stock data.
# In this lesson, we will try to get the basic stock price data among the stock data.
# We will be using API to get the stock data in this file.
# We will use API - FinanceDataReader to get the stock data.
# We will also compare pandasDataReader and FinanceDataReader.
# We will also try to download the file directly. This is, for example, csv, xlsx, etc.

# in Korean, 주식에서 얻을 수 있는 데이터는 예를 들어, 주가, 거래량, 재무제표, 투자지표 이런 것들이 있습니다.
# 크롤링이라는것도 있는데, 주식 데이터를 크롤링하는 것은 주식 데이터를 얻는 한 방법입니다.
# 이번엔 저 주식 데이터들중 제일 기본적인 주가 데이터를 얻어볼겁니다.
# 이번엔 API를 사용하여 주식 데이터를 얻어볼겁니다.
# 이번엔 API - FinanceDataReader를 사용하여 주식 데이터를 얻어볼겁니다.
# pandasDataReader vs FinanceDataReader 이 둘의 차이도 알아볼겁니다.
# 파일을 직접 다운받는 방법도 있습니다. 이것은 예를 들어 csv, xlsx, etc. 이런 것들이 있습니다.

import yfinance as yf
from datetime import datetime

# we will get samsung electronics stock price data from yahoo finance for 1 year from today.
# Using yfinance instead of pandas_datareader (Yahoo Finance API changed)
today = datetime.today().strftime('%Y-%m-%d')
samsung_electronics = yf.download('005930.KS', start='2025-01-01', end=today)

print(samsung_electronics)

# now we will try to get the stock price data from google finance, Apple, Nvidia and Palantir.
stocks = ['GOOGL', 'AAPL', 'NVDA', 'PLTR']
for stock in stocks:
    stock_data = yf.download(stock, start='2025-01-01', end=today)
    print(stock_data)
    print(f"--------------------------------")

# for readability, we will store these four stocks in a txt file.
with open('stocks.txt', 'w') as f:
    for stock in stocks:
        stock_data = yf.download(stock, start='2025-01-01', end=today)
        f.write(stock + '\n')
        f.write(stock_data.to_string())
        f.write('\n' + '--------------------------------' + '\n')

# let's try to plot the stock price data.
import matplotlib.pyplot as plt
import os

# Create directory if it doesn't exist
os.makedirs('1yearstocksexample', exist_ok=True)

for stock in stocks:
    stock_data = yf.download(stock, start='2025-01-01', end=today)
    plt.figure(figsize=(12, 6))
    plt.plot(stock_data['Close'], label=stock)
    plt.title(f'{stock} Stock Price (1 Year)')
    plt.xlabel('Date')
    plt.ylabel('Close Price ($)')
    plt.legend()
    plt.grid(True)
    # Save the figure BEFORE showing it
    plt.savefig(f'1yearstocksexample/{stock}_price.png', dpi=300, bbox_inches='tight')
    plt.close()  # Close the figure to free memory


# now we will try finance-datareader to get the stock price data.
import FinanceDataReader as fdr

# we will get 셀트리온

seltirion = fdr.DataReader('068270', start='2025-01-01', end=today)
print("below is the stock price data of 셀트리온" + '\n' + seltirion.to_string())