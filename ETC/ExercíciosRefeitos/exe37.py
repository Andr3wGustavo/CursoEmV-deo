# Write a Python program that reads any integer and asks the user to choose the base of conversion:
# 1 for binary, 2 for octal and 3 for hexadecimal.
num = int(input('Type a number: '))
print('''Choose on of the options to covert:
[1] Convert to BINARY
[2] Convert to OCTAL
[3] Convert HEXADECIMAL''')
choice = int(input('Your choice: '))
if choice == 1:
    print(f'{num} to binary is {bin(num)[2:]}')
elif choice == 2:
    print(f'{num} to octal is {oct(num)[2:]}')
elif choice == 3:
    print(f'{num} to hexadecimal is {hex(num)[2:]}')
# this program basically uses the python's resource to convert a number to other numeric base
