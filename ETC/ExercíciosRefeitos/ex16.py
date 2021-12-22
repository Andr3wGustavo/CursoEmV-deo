# Create a program that reads any Real number from the keyboard and shows its entire portion on the screen.
from math import trunc
num = float(input('Type a number: '))
print(f'The value was {num} and its int part is {trunc(num)}.')
# this will show the int part of the num that was typed

