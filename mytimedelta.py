from datetime import date
from datetime import time
from datetime import timedelta
from datetime import datetime

print(timedelta(days=365, hours=5, minutes=1))

now = datetime.now()
print("Today is " + str(now))

#print today's date one year from now
print("Today's date 1 year from now " + str(now + timedelta(days=365)))
print("Two weeks and 2 days from now " + str(now + timedelta(days=2, weeks=2)))
print("1 month 3 weeks and 2 days before " + str(now - timedelta(days=2,weeks=7)))

today = date.today()
afd = date(today.year,4,1)

if (afd < today):
    print("April fool's day has already went %d days before " % ((today -afd).days))
    afd = afd.replace(year = today.year+1)

#calculate number of days to next April fool's day
time_to_afd = afd-today
print("Next april fool's day is %d days only", time_to_afd.days)


