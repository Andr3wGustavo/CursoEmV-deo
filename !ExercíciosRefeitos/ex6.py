
# Create an algorithm that reads a number and shows its double, triple and square root.
from math import sqrt  # this import a library that make it easy extract the square root
num = int(input('Type a number: '))

print(f'Double {num} is {num*2}.')  # this shows the double number
print(f'Triple {num} is {num*3}.')  # this shows the triple number
print(f'The square root of {num} is {sqrt(num)}.')  # this extract the square root
