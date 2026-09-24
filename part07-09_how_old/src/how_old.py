from datetime import datetime, timedelta

day = int(input("Day:"))
month = int(input("Month:"))
year = int(input("Year:"))

usr_datetime = datetime(year, month, day)
new_millenium = datetime(1999, 12, 31)

diffrence = new_millenium - usr_datetime

if year > 1999:
    print("You weren't born yet on the eve of the new millennium.")
else:
    print(f"You were {diffrence.days} days old on the eve of the new millennium.")