# Write a program that makes the computer "think" of an integer between 0 and 5
# and ask the user to try to find out which number was chosen by the computer.
# The program should write on the screen if the user won or lost.

from random import randint
from time import sleep
computer = randint(0, 5)
print('-='*36)
print('Im gonna think in a number between 0 and 5, try guess what number is it!')
print('-='*36)
user = int(input("Try find out the computer's choice: "))
print('PROCESSING...')
sleep(2)
if user == computer:  # if the user's number are equal the computer's number, then you won
    print(f'You won, the number was really {computer}!')
else:  # if the user's number are different the computer's number, then you lost
    print(f'You lost, the number was {computer} instead {user}!')