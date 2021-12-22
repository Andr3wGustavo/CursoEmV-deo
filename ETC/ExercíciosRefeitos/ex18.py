# Make a program that reads any angle and shows the value of the sine, cosine and tangent of that angle on the screen.
from math import sin, cos, tan, radians
degree = float(input('Type the degree that you wish: '))
print(f'{degree}º has the SINE equal {sin(radians(degree)):.2f}')
print(f'{degree}º has the COSINE equal {cos(radians(degree)):.2f}')
print(f'{degree}º has te TANGENT equal {tan(radians(degree)):.2f}')
# Using the math library, this program shows the value of sin, cos and tan (after converts to radians) in the terminal
