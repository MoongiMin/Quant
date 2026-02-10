# rolling 이란 함수는 이동 평균을 계산하는 함수입니다.

# 5일의 5일이동평균은 1일부터 5일까지 5일간의 종가의 평균입니다.
# 6일의 5일이동평균은 2일부터 6일까지 5일간의 종가의 평균입니다.
# 이런식으로 묶는걸 rolling 함수 라고합니다.
# window 라는 variable 을 지정해야하는데 이것이 묶는 크기입니다.
# 10일이동평균이면 window = 10 이 됩니다.

import FinanceDataReader as fdr 

df= fdr.DataReader('AAPL','2021')

#window = 3
df['Close_rolling'] = df['Close'].rolling(window=3).mean()

print(df)

