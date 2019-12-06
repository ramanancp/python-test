from datetime import date
from datetime import time
from datetime import datetime

def main():
    today = date.today()
    print ("Today is ", today)

#print date's individual components
    print ("Date's individual components", today.day, today.month, today.year)

#print today's weekday
    print("Today's weekday is ", today.weekday())
    days = ["Mon","Tue","Wed","Thu","Fri","Sat","Sun"]
    print("whic is ", days[today.weekday()])

#print today's date time
    now = datetime.now()
    print("Today's date time is ", now)
    print(now.strftime("Formatted date is %a, %d %B, %y"))
    
#Locale's date and time
# %c - locale date and time, %x locale's date, %X - locale's time
    print(now.strftime("Locale's date and time %c"))
    print(now.strftime("Locale's date %x"))
    print(now.strftime("Locale's time %X"))

## date formatting ##
#%y/%Y - Year, %a/%A - weekday, %b/%B - month , %d - day of month


if __name__ == "__main__":
    main()