import calendar

year = 2022

month = range(1 ,13)

# Get all the name of the month directly from calendar.month_name

for month in range(1, 13):
    month_name = calendar.month_name[month]
    print(month_name , end = " ")
  
for day in calender.day_name:
    print(day , end=" ")

