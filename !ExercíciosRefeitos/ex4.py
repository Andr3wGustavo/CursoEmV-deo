
# Make a program that reads something on the keyboard and shows on the screen its primitive type
# and all possible information about it.

something = input('Type something here: ')
print(f'The primitive types is {type(something)}') # this shows the variable primitve type
print(f'does it only have spaces? {something.isspace()}')  # this shows if the variable only has spaces
print(f'Is it a number? {something.isalnum()}')  # this shows if the variable is a number
print(f'Is it an alphabetical? {something.isalpha()}')  # this shows if the variable is an alphabetical
print(f'Is it an alphanumber? {something.isalnum()}')  # this shows if the variable is an alphanumber
print(f'Is it upper? {something.isupper()}')  # this shows if the variable is upper
print(f'Is it lower? {something.islower()}')  # this shows if the variable is lower
print(f'Is it capitalized? {something.istitle()}')  # this shows if the variable is capitalized
