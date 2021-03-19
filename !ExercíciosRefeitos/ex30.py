# Create a program that reads an integer and shows on the screen whether it is even or odd.
num = int(input('Type a number: '))
if num % 2 == 0:  # if the number tiped give a remainder equal 0, then it's an even
    print(f'{num} is an even!')
else:
    print(f'{num} is an odd!')
