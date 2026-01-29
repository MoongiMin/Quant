import pandas as pd
import time

a = pd.Timestamp('2025-04-01 12:00:00')

print(a)
monthrange = pd.date_range('2025-04-01', '2027-04-01', freq='MS')
print(monthrange)
start_time = time.time()
while(time.time() - start_time < 30) :
    print(pd.Timestamp.now())
    time.sleep(3)
