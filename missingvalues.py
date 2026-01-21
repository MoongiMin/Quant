import pandas as pd
import numpy as np

# Nan means data is empty

s1 = pd.Series([np.nan, 2, 3, 4, 5])
s2 = pd.Series([1, 2, np.nan, np.nan, 5])
s3 = pd.Series([1, 2, 3, 4, 5])
df = pd.DataFrame({'s1':s1, 's2':s2, 's3':s3})

# we will make column s1 s2 s3 and there will be 5 values each row

print(df)
print("--------------------------------")
# assume we can't find missing values, but we want to find them
# there is function called isna() to find missing values (isnull is the same as isna because python does not differentiate between isna and isnull)
print("isna() function is used to find missing values")
print(df['s1'].isna())
print(df['s2'].isna())
print(df['s3'].isna())

# if we want to count missing values, we can use sum() function
print("sum() function is used to count missing values")
print(df.isna().sum())

# isin() function is used to check if a value is in a list
print("isin() function is used to check if a value is in a list")
df.isin([np.nan, np.inf, -np.inf])

# we can do dropna() function to drop missing values
# before dropping we will make a copy of the dataframe
df_copy = df.copy()
print("dropna() function is used to drop missing values")
df_copy.dropna()
print(df_copy)

# we can also use fillna() function to fill missing values
# before filling we will make a copy of the dataframe
df_copy = df.copy()
print("fillna() function is used to fill missing values")

# we will fill missing values with the value in front of it (forward fill)
# method='pad' is deprecated, use ffill() instead
df_copy = df_copy.ffill()  # or df_copy.fillna(method='ffill', inplace=True)
print(df_copy)

df_copy = df.copy()
df_copy = df_copy.bfill()  # or df_copy.fillna(method='bfill', inplace=True)
print(df_copy)
