import FinanceDataReader as fdr

df= fdr.DataReader('AAPL','2021')

print(df)

#샘플의 빈도수를 연간, 월간, 주간 으로 바꿀수 있습니다.

#주간, 월간, 연간으로 커지면서 빈도수가 감소하는걸 downsampling 이라고 합니다.
#반대로 일간을 시간당으로 바꾸면 그걸 upsampling 이라고 합니다.
#upsampling 은 보통 잘 안씁니다.
week = df.resample(rule='W').mean() # this will be the mean of the weekly data.
print(week)

month = df.resample(rule='M').mean() # this will be the mean of the monthly data.
print(month)

year = df.resample(rule='Y').mean() # this will be the mean of the yearly data.
print(year)
#현재 프린트가 말일로 나오는데, 초일로 바꾸고 싶으면
week = df.resample(rule='W-MON').mean()
print(week)

month = df.resample(rule='MS').mean()
print(month)

year = df.resample(rule='YS').mean()
print(year)



