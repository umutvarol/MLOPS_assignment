
from datetime import date

today = date.today()

printable_today = today.strftime("%d/%m/%Y")
print("Today = ",printable_today)
