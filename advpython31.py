#prgm to print current date with seperator as \
from datetime import date
d=date.today()
print("year=",d.year)
print("month=",d.month)
print("day=",d.day)
print(d.year,"/",d.month,"/",d.day)