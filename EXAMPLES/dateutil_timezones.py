#
from dateutil import parser

date_string_1 = 'Aug 27 2015 08:09:22-04:00'  # EDT
date_string_2 = 'Aug 27 2015 10:47:19-07:00'  # PDT

date1 = parser.parse(date_string_1)
date2 = parser.parse(date_string_2)

print(date1)
print(date2)

diff = date2 - date1

print(diff)
