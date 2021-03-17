
# Make a program that reads the width and height of a wall in meters, calculate its area
# and the amount of paint needed to paint it
# knowing that each liter of paint paints an area of 2 meters.

width = float(input('Type the wall width: '))
height = float(input('Type the wall height: '))
print(f'The wall has {width*height:.2f} as area and you will need {(width*height)/2:.2f} liters to paint it.')
# this program will to calculate how many liters of paint you'll need to paint the wall
