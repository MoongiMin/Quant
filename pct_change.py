# pct_change 란 백분율 변화량을 일컫는 용어입니다.

# 1월 1일에 8000원이었던 주가를 매수를 했습니다.
# 1월 2일에 10000원으로 상승해서 매도를 했습니다.
# 이 경우 하루에 2000원의 이익을 얻었습니다.
# 수익률은, 2000원을 원금 8000원으로 나눈 값이 됩니다.
# 저 수익률이 단순 수익률이 됩니다.
# (최종 - 최초) / 최초, 이 식을 shift 연산을 이용하여 계산 합니다.

import FinanceDataReader as fdr

df = fdr.DataReader('AAPL','2021')

print(df)

df['pct_change'] = df['Close'].pct_change() # << pct_change() 함수 안에 variable 은 integer 입니다. default 는 1 입니다.
print(df)

#alternative
df['alternative'] = (df['Close'] - df['Close'].shift(1)) / df['Close'].shift(1)
print(df)
