#volatility 란, 변동성이다.

import FinanceDataReader as fdr
import numpy as np

df = fdr.DataReader('AAPL', '2000')

start_date = '2021-06-13'
end_date = '2022-02-03'
tmp_df = df.loc[start_date:end_date].copy()
tmp_df['daily_return'] = tmp_df['Close'].pct_change().dropna()

VOL = np.std(tmp_df['daily_return']) * np.sqrt(252)  # 연율화 변동성
print(VOL)