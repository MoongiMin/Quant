# yfinance 라이브러리를 사용해서 데이터 인덱싱 하는 방법
# How to index data using yfinance library
# pandas_datareader의 Yahoo Finance API가 작동하지 않아 yfinance로 변경
# Changed to yfinance because pandas_datareader's Yahoo Finance API doesn't work

import yfinance as yf
from datetime import datetime

# 삼성전자 주가 데이터 가져오기
# Get Samsung Electronics stock price data
df = yf.download('005930.KS', start='2024-01-01', end=datetime.today().strftime('%Y-%m-%d'))

# ========== 3가지 인덱싱 방법 ==========
# ========== 3 Indexing Methods ==========

# ========== 방법 1: df[] - 라벨 인덱싱 ==========
# ========== Method 1: df[] - Label Indexing ==========
print("=" * 50)
print("방법 1: df[] - 라벨 인덱싱")
print("=" * 50)

# 컬럼 선택
# Select column
print("\n1-1. 특정 컬럼 선택 (시가):")
print("1-1. Select specific column (Open):")
print(df['Open'])

# 여러 컬럼 선택
# Select multiple columns
print("\n1-2. 여러 컬럼 선택 (시가, 종가):")
print("1-2. Select multiple columns (Open, Close):")
print(df[['Open', 'Close']])

# 행 슬라이싱 (인덱스 번호로)
# Row slicing (by index number)
print("\n1-3. 행 슬라이싱 (0부터 5까지):")
print("1-3. Row slicing (from 0 to 5):")
print(df[0:5])

# 날짜 범위 슬라이싱
# Date range slicing
print("\n1-4. 날짜 범위 슬라이싱 (2024-01-01부터 2024-01-05까지):")
print("1-4. Date range slicing (from 2024-01-01 to 2024-01-05):")
print(df['2024-01-01':'2024-01-05'])


# ========== 방법 2: df.loc[] - 라벨 인덱싱 (명시적) ==========
# ========== Method 2: df.loc[] - Label Indexing (Explicit) ==========
print("\n" + "=" * 50)
print("방법 2: df.loc[] - 라벨 인덱싱 (명시적)")
print("Method 2: df.loc[] - Label Indexing (Explicit)")
print("=" * 50)

# 특정 날짜의 특정 컬럼
# Specific column of specific date
print("\n2-1. 특정 날짜의 시가 (2024-01-08):")
print("2-1. Open price of specific date (2024-01-08):")
print(df.loc['2024-01-08', 'Open'])

# 특정 날짜의 모든 컬럼
# All columns of specific date
print("\n2-2. 특정 날짜의 모든 데이터 (2024-01-08):")
print("2-2. All data of specific date (2024-01-08):")
print(df.loc['2024-01-08'])

# 날짜 범위와 특정 컬럼
# Date range and specific column
print("\n2-3. 날짜 범위의 시가 (2024-01-01부터 2024-01-05까지):")
print("2-3. Open price of date range (from 2024-01-01 to 2024-01-05):")
print(df.loc['2024-01-01':'2024-01-05', 'Open'])

# 날짜 범위와 여러 컬럼
# Date range and multiple columns
print("\n2-4. 날짜 범위의 여러 컬럼 (시가, 종가):")
print("2-4. Multiple columns of date range (Open, Close):")
print(df.loc['2024-01-01':'2024-01-05', ['Open', 'Close']])


# ========== 방법 3: df.iloc[] - 정수 인덱싱 ==========
# ========== Method 3: df.iloc[] - Integer Indexing ==========
print("\n" + "=" * 50)
print("방법 3: df.iloc[] - 정수 인덱싱")
print("Method 3: df.iloc[] - Integer Indexing")
print("=" * 50)

# 특정 행 선택
# Select specific row
print("\n3-1. 첫 번째 행 (인덱스 0):")
print("3-1. First row (index 0):")
print(df.iloc[0])

# 특정 행과 특정 컬럼
# Specific row and specific column
print("\n3-2. 첫 번째 행의 시가 (인덱스 0, 컬럼 0):")
print("3-2. Open price of first row (index 0, column 0):")
print(df.iloc[0, 0])  # 첫 번째 컬럼이 Open인 경우 / First column is Open

# 행 범위 선택
# Select row range
print("\n3-3. 첫 5개 행 (인덱스 0부터 4까지):")
print("3-3. First 5 rows (index 0 to 4):")
print(df.iloc[0:5])

# 행 범위와 컬럼 범위
# Row range and column range
print("\n3-4. 첫 5개 행의 첫 3개 컬럼:")
print("3-4. First 3 columns of first 5 rows:")
print(df.iloc[0:5, 0:3])

# 특정 행과 여러 컬럼
# Specific row and multiple columns
print("\n3-5. 첫 번째 행의 시가와 종가 (컬럼 0, 3):")
print("3-5. Open and Close of first row (column 0, 3):")
print(df.iloc[0, [0, 3]])  # Open과 Close / Open and Close

