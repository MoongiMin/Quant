import pandas as pd
import numpy as np
import FinanceDataReader as fdr
# we will use shift function to shift the values of the dataframe

df = fdr.DataReader('AAPL', '2021', '2022')

print("AAPL data:")
print(df)

print("--------------------------------")

# this will shift the values of the Close column by 1 day
df['Close_lag1'] = df['Close'].shift(1)
print(df)

# this will shift the values of the Close column by 3 days
print("--------------------------------")
df['Close_lag3'] = df['Close'].shift(3)
print(df)

# this will shift the values of the Close column by -1 day
print("--------------------------------")
df['Close_lag_-1'] = df['Close'].shift(-1)
print(df)