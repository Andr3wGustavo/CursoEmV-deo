
# A teacher wants to draw one of his four students to erase the board.
# Make a program that helps him, reading the students's names and writing the name of the chosen one on the screen.
from random import choice  # this will import the tool that will to choice the names
first = str(input("Type the first student's name: "))
second = str(input("Type the second student's name: "))
third = str(input("Type the third student's name: "))
names = [first, second, third]  # this create a list that will be choosen after, by using the choice tool
print(f'The choosen studend was {choice(names)}.')

