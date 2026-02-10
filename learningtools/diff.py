import FinanceDataReader as fdr

df= fdr.DataReader('AAPL','2021')

# if nothing is in diff(), it will be 1 inside.

df['close_diff'] = df['Close'].diff()

df['close_diff_2'] = df['Close'].diff(2) # this will be the difference between the current and the previous 2 days.

print(df)