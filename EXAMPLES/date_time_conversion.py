from datetime import date, time, datetime
import time as Time  # aliased to avoid conflict with datetime.time

my_time = time(10, 42, 51)   # create instance of datetime.time
my_date = date(1996, 1, 31)  # create instance of datetime.date
my_datetime = datetime(1996, 1, 31, 10, 42, 51)  # create instance of datetime.datetime
my_timestamp = my_datetime.timestamp()  # create timestamp (Unix epoch time)
my_timetuple = my_datetime.timetuple()  # create time tuple (namedtuple struct_tm)

print("my_time:", my_time)
print("my_date:", my_date)
print("my_datetime:", my_datetime)
print("my_timestamp:", my_timestamp)
print("my_timetuple:", my_timetuple)
print()

d = my_datetime.date() # convert datetime.datetime to datetime.date
print("datetime -> date:", d)

t = my_datetime.time() # convert datetime.datetime to datetime.time
print("datetime -> time:", t)

ts = my_datetime.timestamp() # convert datetime.datetime to timestamp
print("datetime -> timestamp:", ts)

tt = my_datetime.timetuple() # convert datetime.datetime to time tuple
print("datetime -> timetuple:", tt)
print()

dt = datetime.fromordinal(my_date.toordinal())  # convert datetime.date to datetime.datetime
print("date -> datetime:", dt)

t = datetime.fromordinal(my_date.toordinal()).time() # convert datetime.date to datetime.time
print("date -> time:", t)

ts = datetime.fromordinal(my_date.toordinal()).timestamp()  # convert datetime.date to timestamp
print("date -> timestamp:", ts)

tt = my_date.timetuple() # convert datetime.date to time tuple
print("date -> timetuple:", tt)
print()

dt = my_datetime.fromtimestamp(my_timestamp)  # convert timestamp to datetime.datetime
print("timestamp -> datetime:", dt)

d = my_datetime.fromtimestamp(my_timestamp).date()  # convert timestamp to datetime.date
print("timestamp -> date:", d)

t = my_datetime.fromtimestamp(my_timestamp).time()  # convert timestamp to datetime.time
print("timestamp -> datetime:", t)

tt = Time.localtime(my_timestamp)
print("timestamp -> timetuple:", tt)  # convert timestamp to time tuple
print()

dt = datetime.fromtimestamp(Time.mktime(my_timetuple))  # convert time tuple to datetime.datetime
print("timetuple -> datetime:", dt)

d = datetime.fromtimestamp(Time.mktime(my_timetuple)).date() # convert time tuple to datetime.date
print("timetuple -> date:", d)

dt = datetime.fromtimestamp(Time.mktime(my_timetuple))  # convert time tuple to datetime.time
print("timetuple -> time:", t)

ts = Time.mktime(my_timetuple)  # convert time tuple to timestamp
print("timetuple -> timestamp:", ts)
