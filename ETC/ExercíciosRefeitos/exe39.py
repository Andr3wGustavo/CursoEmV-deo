# Make a program that reads the year of birth of a young person and informs them, according to their age
# if they are still going to enlist in the military, if it is an exact time to enlist
# or if it is past the enlistment time. Your program should also show how much time is left or past the deadline.
from datetime import date
birth = int(input('Type your birth year: '))
current_year = date.today().year
if current_year - birth == 18:
    print("It's time for you enlist in the military. You're 18 yo.")
elif current_year - birth > 18:
    print(f"It's not time for enlist in the military, you has passed.It was {(current_year - birth) - 18} years ago.")
elif current_year - birth < 18:
    print(f"It's not time for enlist in the military, It will be in {18 - (current_year - birth)}.")
