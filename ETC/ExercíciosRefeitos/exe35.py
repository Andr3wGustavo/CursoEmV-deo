#  Develop a program that reads the length of three lines
#  and tells the user whether or not they can form a triangle.
length1 = float(input('Type the first length: '))
length2 = float(input('Type the second length: '))
length3 = float(input('Type the third length: '))

if length1 < length2 + length3 and length2 < length3 + length1 and length3 < length1 + length2:
    # this is the criteries to form a triangle
    print('The triangle CAN be formed!')
else:
    print('The triangle CANNOT be formed!')
