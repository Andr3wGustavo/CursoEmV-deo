# Create a program that reads a person's full name and shows:
# - The name with all upper and lower case letters.
# - How many letters in all (without considering spaces).
# - How many letters has the first name.
name = str(input('Type your full name: ')).strip()
print('Analyzing your name...')
print(f'Your capital name is {name.upper()}.')  # it will capitalize the name
print(f'Your lower case name is {name.lower()}.') # it will make the name in lower case
print(f"Your name has {len(''.join(name.split()))} letters.")
# this will split the name and the will join the name with an empty space
print(f'Your first name is {name.split()[0]} and it has {len(name.split()[0])} letters.')
# this will select the first name and it will shows the length of it
