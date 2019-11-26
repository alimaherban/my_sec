from datetime import date
today = date.today()
print("Today's date:", today)


from datetime import datetime
now = datetime.now()
year = now.strftime("%Y")
print("year:", year)
month = now.strftime("%m")
print("month:", month)
day = now.strftime("%d")
print("day:", day)
time = now.strftime("%H:%M:%S")
print("time:", time)
date_time = now.strftime("%m/%d/%Y, %H:%M:%S")
print("date and time:",date_time)


# Figure out your age
import datetime
currentDate = datetime.datetime.now()

deadline= input ('Plz  ali enter your date of birth (mm/dd/yyyy) ')
deadlineDate= datetime.datetime.strptime(deadline,'%m/%d/%Y')
print (deadlineDate)
daysLeft = deadlineDate - currentDate
print(daysLeft)
#
years = ((daysLeft.total_seconds())/(365*24*3600))
yearsInt=int(years)

print(years)
#
months=(years-yearsInt)*12
monthsInt=int(months)
print(months)


days=(months-monthsInt)*(365/12)
daysInt=int(days)
print(days)

#

#
# from datetime import *
# import calendar
#
# N = 7
#
# date_N_days_after = datetime.now() + timedelta(days=N)
# date_N_month_after = datetime.now() + timedelta(months=+6)
# date_N_year_after = datetime.now() + timedelta(years=N)
#
# print(datetime.now())
# print(date_N_days_after)
# print(date_N_month_after)
# print(date_N_year_after)

