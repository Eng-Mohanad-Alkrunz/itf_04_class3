import datetime

days = ["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"]
today = datetime.date.today()
print(today.weekday())
print(days[today.weekday()])
print(datetime.date.today())
print(today.month)
print(today.year)
print(today.day)
print(today.strftime("%m---%d---%Y"))
print(datetime.datetime.now().strftime("%d:%m:%Y  -- %H:%M:%S -- %a"))


import time

t = time.localtime()
current_time = time.strftime("%H:%M:%S", t)
print(current_time)
d =  datetime.datetime.strptime(str(current_time)[0:7], "%H:%M:%S")
d = d.strftime("%I:%M %p")
print(d)
