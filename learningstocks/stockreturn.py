#수익률 계산방법

import FinanceDataReader as fdr

df= fdr.DataReader('AAPL','2011')

#buy = 600, sell = 1000, return = (sell - buy) / buy = (1000 - 600) / 600 = 0.6666666666666666

# 2021-01-04 buy, 2021-05-06 sell,

df['daily_return'] = df['Close'].pct_change()

#cumprod() 는 누적 곱을 계산하는 함수입니다. 누적곱이란, 1일부터 현재까지의 수익률을 계산하는 함수입니다.
#첫날은 pct_change()가 NaN이므로 fillna(0)으로 0% 수익률 처리
df['stock_return'] = (1 + df['daily_return'].fillna(0)).cumprod()

start_date = '2011-01-04'
end_date = '2021-05-06'

tmp_df = df.loc[start_date:end_date,['stock_return']] / df.loc[start_date,['stock_return']]

print(tmp_df)

import matplotlib.pyplot as plt

tmp_df.plot(figsize=(16,9))
plt.show()