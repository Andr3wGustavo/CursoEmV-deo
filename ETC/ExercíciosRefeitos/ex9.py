# Make a program that reads any integer number and shows your multiplication table on the screen.
num = int(input('Type a number: '))
for x in range(1, 11):  # this make the program to repeat the same print ten times
    print(f'{num}x{x} = {num*x}')
