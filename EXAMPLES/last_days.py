from datetime import date
from dateutil.relativedelta import relativedelta

def get_last_days(year):
    last_days = []
    for month in range(1,13):
        first_day = date(year, month, 1)
        last_day = first_day + relativedelta(day=1, months=1, days=-1)
        last_days.append(last_day)
    return last_days

if __name__ == '__main__':

    last_days = get_last_days(2023)

    for last_day in last_days:
        lwd = last_day.strftime("%A")  # format date object as weekday name
        print(f"{lwd:9s} {last_day}")

