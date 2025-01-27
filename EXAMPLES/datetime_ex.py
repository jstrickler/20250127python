from datetime import datetime, date

today = date.today()
print(f"today: {today}")
print(f"type(today): {type(today)}")
print(f"today.month: {today.month}")
print(f"today.day: {today.day}")
print(f"today.year: {today.year}")
print()

now = datetime.now()  # get today's date and time
print(f"now: {now}")
print(f"now.year: {now.year}")
print(f"now.month: {now.month}")
print(f"now.day: {now.day}")
print(f"now.minute: {now.minute}")
print(f"now.second: {now.second}")
print(f"now.microsecond: {now.microsecond}")
print()

d1 = datetime(2018, 6, 13, 4, 55, 27, 8082)  # create a date object
d2 = datetime(2018, 8, 24)
delta = d2 - d1  # date objects can be subtracted from other date objects

print(f"delta: {delta}")  # timedelta has days, seconds, and microseconds
print(f"delta.days: {delta.days}")

