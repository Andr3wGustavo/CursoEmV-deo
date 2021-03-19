# Make a program that reads any year and shows if it is leap.
from datetime import date
year = int(input('Type a year, or type 0 to current year:  '))
if year == 0:
    year = date.today().year  # if this take the current year from computer
if year%4 == 0 and year%100 != 0 or year%400 == 0:  # that is the criteries for a year be a leap year
    print(f'{year} IS a leap year.')
else:
    print(f'{year} ISNT a leap year.')