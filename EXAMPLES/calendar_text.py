from datetime import date
from calendar import TextCalendar

today = date.today()

text_calendar = TextCalendar()  # create a text calendar object
print(text_calendar.formatmonth(today.year, today.month))  # format one month as text

