import datetime


day = datetime.date(2025,5,15)
today = datetime.date.today()
time = datetime.datetime.now().time()
week = datetime.timedelta(weeks=1)

print(day),print(today),print(time),print(week)
week *= 2
print(f"after 2x: {week}")

print("\n=== Parse string to datetime ===")
datetime_dt = datetime.datetime.strptime("2023-04-01 12:00:00", "%Y-%m-%d %H:%M:%S")
print(f"datetime_dt: {datetime_dt}")

print("\n=== Add 2 weeks to datetime ===")
datetime_dt+= week
print(f"datetime_dt after adding 2 weeks: {datetime_dt}")

print("\n=== Format datetime to string ===")
datetime_str = datetime_dt.strftime("%Y-%m-%d %H:%M:%S")
print(f"datetime_str: {datetime_str}")