# Quant

Quant 프로그램 개발을 위한 저장소입니다.

Repository for developing a Quant program.

---

## 목표 / Goal

이 프로젝트의 최종 목표는 **Quant(퀀트) 프로그램**을 개발하는 것입니다.

The ultimate goal of this project is to develop a **Quant program**.

## 현재 상태 / Current Status

현재는 Quant 프로그램 개발에 필요한 다양한 툴과 라이브러리들을 학습하고 연습하는 단계입니다.

Currently, I am in the learning and practice phase, working with various tools and libraries necessary for developing the Quant program.

## 학습 중인 툴 / Tools Being Learned

- **NumPy**: 수치 계산 및 배열 연산 / Numerical computing and array operations
- **Pandas**: 데이터 분석 및 조작 / Data analysis and manipulation
- **DateTime**: 날짜 및 시간 처리 / Date and time processing
- **yfinance**: Yahoo Finance에서 주식 데이터 가져오기 / Fetching stock data from Yahoo Finance
- **FinanceDataReader**: 한국 주식 데이터 가져오기 / Fetching Korean stock data
- **Matplotlib**: 데이터 시각화 / Data visualization

## 파일 구조 / File Structure

### 기본 연습 파일 / Basic Practice Files
- `numpypractice.py`: NumPy 기본 연산 및 금융 데이터 예제 / NumPy basic operations and financial data examples
- `numpydatetime.py`: NumPy datetime64 및 타임존 처리 연습 / NumPy datetime64 and timezone handling practice
- `daytimepractice.py`: Python datetime 모듈 연습 / Python datetime module practice
- `pandaspractice.py`: Pandas를 이용한 데이터 처리 연습 / Data processing practice using Pandas
- `pandasseries.py`: Pandas Series 연습 / Pandas Series practice
- `pandasdataframe.py`: Pandas DataFrame 연습 및 예제 / Pandas DataFrame practice and examples
- `dataframeindexing.py`: DataFrame 인덱싱 방법 연습 (df[], df.loc[], df.iloc[]) / DataFrame indexing methods practice (df[], df.loc[], df.iloc[])
- `pct_change.py`: 백분율 변화량 계산 연습 (pct_change(), shift()) / Percentage change calculation practice (pct_change(), shift())
- `missingvalues.py`: 결측치 처리 연습 (isna, dropna, fillna, ffill, bfill) / Missing values handling practice (isna, dropna, fillna, ffill, bfill)
- `shiftfunction.py`: 시계열 데이터 shift 함수 연습 (lag, lead) / Time series data shift function practice (lag, lead)

### 금융 데이터 / Financial Data
- `financedatareader.py`: yfinance와 FinanceDataReader를 사용한 주식 데이터 수집 및 시각화 / Stock data collection and visualization using yfinance and FinanceDataReader
- `stocks.txt`: 수집된 주식 데이터 텍스트 파일 / Collected stock data text file
- `1yearstocksexample/`: 주식 가격 그래프 이미지 (AAPL, GOOGL, NVDA, PLTR) / Stock price graph images (AAPL, GOOGL, NVDA, PLTR)

## 개발 환경 / Development Environment

- Python 3.13
- NumPy
- Pandas
- yfinance
- FinanceDataReader
- Matplotlib
