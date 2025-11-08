#print the calendar for specific month from specified year
import calendar
y=int(input("Enter the year:"))
m=int(input("Enter the month:"))
print(calendar.month(y,m))