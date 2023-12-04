import datetime

birthday = input("Enter date of birth (in DD/MM/YYYY): ")

date_of_birth = datetime.datetime.strptime(birthday,"%d/%m/%Y").date()

todays_date = datetime.date.today()

difference = todays_date - date_of_birth

print(difference.days)