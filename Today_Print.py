
from datetime import date
from datetime import datetime

today = date.today()
time_now = datetime.now()

printable_today = today.strftime("%d/%m/%Y")
printable_time_now = time_now.strftime("%H:%M:%S")

print("Today = ",printable_today)
print("Current Time = ", printable_time_now)
