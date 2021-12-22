# Make a program that reads a person's full name, then shows the first and last name specified.
name = str(input('Write your name here: ')).split()  # this will divide the full name in parts
print('Nice to meet you!')
print(f'Your first name is: {name[0].capitalize()}')  # this take the first name, using the position
print(f'Your last name is: {name[-1].capitalize()}')  # this take the last name, using the position
