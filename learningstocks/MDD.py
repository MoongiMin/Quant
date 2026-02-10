#MDD(Maximum Drawdown) 이란 최대 낙폭지수이다
#최대낙폭지수는, 최고점에서 최저점까지의 낙폭을 계산하는 지수이다.
# 최대낙폭지수 = (최저-최고) / 최고 = 최저/최고 - 1

from importlib import import_module
import FinanceDataReader as fdr

df= fdr.DataReader('AAPL', '2000')

start_date = '2021-02-04'
end_date = '2022-02-03'
tmp_df= df.loc[start_date:end_date]
historical_max = tmp_df['Close'].cummax()
print(historical_max)

daily_MDD = tmp_df['Close'] / historical_max - 1
print(daily_MDD)

import matplotlib.pyplot as plt
mdd = daily_MDD.cummin()
mdd.plot(figsize=(16,9))
plt.show()
