# Create a program that reads a person's name and tells them if they have "SILVA" in their name
name = str(input('Write your name here: ')).upper()
if 'SILVA' in name:  # this verify if there is 'silva' in a person's name
    print("Yes, there's 'SILVA' in the person's name!")
else:
    print("No, there's no 'SILVA' in the person's name!")
