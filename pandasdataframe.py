import pandas as pd

# this is for pandas dataframe study

# dataframe is composed of series.
# and it is like a table.
# Which means, it is a two-dimensional array which has rows and columns.

# table example
# 종목명 가격 거래량 PER
# 삼성전자 80000 100000 1.2
# LG전자 100000 100000 1.7
# SK하이닉스 120000 100000 0.7
# NAVER 140000 100000 1.1

example1 = pd.DataFrame({"가격": [80000, 100000, 120000, 140000], "거래량": [100000, 100000, 100000, 100000], "PER": [1.2, 1.7, 0.7, 1.1]})

# 출력 포맷 설정
pd.set_option('display.unicode.east_asian_width', True)
pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)
pd.set_option('display.max_colwidth', None)

print(example1)

print("below is the information of the dataframe")
print(example1.info)
