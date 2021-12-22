# The same teacher for challenge 019 wants to raffle the order in which students present their work.
# Make a program that reads the names of the four students and shows the order drawn.
from random import shuffle
first = str(input('First student: '))
second = str(input('Second student: '))
third = str(input('Third student: '))
shuffled_names = [first, second, third]  # this create the list that will be shuffled
shuffle(shuffled_names)  # this tool will to shuffle the names of the students
print(f'The order of the presentation will be {shuffled_names}')
