from datetime import date
from datetime import time
from datetime import datetime


today = date.today()
print("Today is ", today)

#print date's individual components
print ("Date's components", today.day, today.month, today.year)

#Week day
print("Today's weekday is ", today.weekday())

days = ["Sun","Mon","Tue","Wed","Thu","Fri","Sat"]
print("Which is " + days[today.weekday()])

today = datetime.now()
print("Date time is " , today)

t =datetime.time(datetime.now())
print("Current time is ", t)

#formatted date time
#%y/%Y - year, %a/%A - weekday, %b/%B - month, %d - day of month
now = datetime.now()
print(now.strftime("%a, %d %B, %y"))
print(now.strftime("Local time is %c"))
print(now.strftime("Local date is %x"))
print(now.strftime("Local date is %X"))

# %I/%H - 12/24 hour, %M - minutes, %S - second, %p - Locale 




