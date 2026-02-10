#CAGR(Compound Annual Growth Rate) 이란 연평균 복리수익률이다.
# ( 최종값 / 최초값)^(1/#년) - 1

import FinanceDataReader as fdr

df= fdr.DataReader('AAPL', '2000')

print(df)
df['daily_return'] = df['Close'].pct_change().fillna(0)  # 첫 행 NaN → 0 (수익률 없음)
df['st_return'] = (1 + df['daily_return']).cumprod()     # 누적수익률: (1+r1)*(1+r2)*...
start_date = '2018-10-08'
end_date = '2022-01-12'

tmp_df = df.loc[start_date:end_date,['st_return']] / df.loc[start_date,['st_return']]
print(tmp_df)

CAGR = tmp_df.loc['2022-01-12','st_return'] ** (252/len(tmp_df.index)) - 1

print(CAGR)