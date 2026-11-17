#write a programs to print month calender
import calendar
month = int(input("enter a month num(1-12):"))
year = int(input("enter year:"))
print(calendar.month(year,month))

# print year calendar
import calendar
year = int(input("enter year:"))
print(calendar.calendar(year))
