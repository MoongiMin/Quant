import numpy as np
from datetime import datetime, timezone, timedelta

today = np.datetime64('today')
print(f"Date only: {today}")

now = np.datetime64('now')
print(f"Date and time (UTC): {now}")

# Specific datetime
specific = np.datetime64('2025-05-15T14:30:00')
print(f"Specific datetime: {specific}")

# ========== Indiana Time (EST/EDT) ==========
print("\n=== Indiana Time ===")

# Indiana는 UTC-5 (또는 daylight saving time 동안 UTC-4)
indiana_tz = timezone(timedelta(hours=-5))

# 현재 시간을 인디애나 기준으로
now_utc = datetime.now(timezone.utc)
now_indiana = now_utc.astimezone(indiana_tz)
print(f"Current time in Indiana: {now_indiana}")

# 특정 시간을 인디애나 기준으로
specific_dt = datetime(2025, 5, 15, 14, 30, 0, tzinfo=indiana_tz)
print(f"Specific time in Indiana: {specific_dt}")

# ========== NumPy DateTime Arithmetic ==========
print("\n=== DateTime Arithmetic ===")
add_days = np.timedelta64(1000, 'D')  # timedelta64 사용
print(f"Date after 1000 days: {today + add_days}")