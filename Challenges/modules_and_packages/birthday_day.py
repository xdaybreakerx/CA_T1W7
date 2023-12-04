import datetime
import calendar 

day = int(input("enter their birth month (as a number 1 - 12): "))
month = int(input("enter birth date (1 - 31): "))

current_year = datetime.datetime.now().year

birthday_this_year = datetime.datetime(current_year, month, day)

day_of_week = calendar.day_name[birthday_this_year.weekday()]

print(f"Your birthday falls on a {day_of_week} in 2023")