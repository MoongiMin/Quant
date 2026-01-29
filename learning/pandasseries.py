import pandas as pd

# for pandas series study
# there is something called series in pandas.
# series is composed of index and values.

# this is an example
# value should be covered with []

example1 =pd.Series([80000, 83900, 200000, 120000]) # it will be like this: 0    80000, 1    83900, 2    200000, 3    120000

print(example1) # when we print, dtype will be int64. which means it is integer.
print(example1[2]) # this will print the value of the index 2.
print(example1[1:3]) # this will print the value of the index 1 to 3.

example2 =pd.Series([80000, 83900, 200000, 120000], index=['삼성전자', 'LG전자', 'SK하이닉스', 'NAVER']) 
# as you can see above, you can assign the name to the index.
print(example2)
print(example2['삼성전자']) # this will print the value of the index '삼성전자'.
print(example2[['삼성전자', 'NAVER']]) # this will print the value of the index '삼성전자' and 'NAVER'.

# now we will try to only print the elements that are below 100000.
print("below is all the elements that are below 100000.")
print(example2[example2 < 100000]) # this boolean expression will print the value of the index that is below 100000.


