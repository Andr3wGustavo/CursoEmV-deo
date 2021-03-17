# Make a program that reads the length of the opposite side and the adjacent side of a right triangle.
# Calculate and show the length of the hypotenuse.
from math import pow, sqrt  # this will import the tools to calculate
opposite = float(input('Type the opposite side length: '))
adjacent = float(input('Type the adjacent side length: '))
hypotenuse = sqrt(pow(opposite, 2) + pow(adjacent, 2))  # this use the pythagoras theorem to find the hypotenuse length
print(f'The hypotenuse is {hypotenuse:.2f}')

