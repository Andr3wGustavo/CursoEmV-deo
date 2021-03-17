# Create a program that reads the name of a city
# and says whether or not it begins with the name "SANTO".]
city = str(input("Which city was you born? ")).upper().split()

if 'SANTO' in city:  # this verify if there is 'santo' in the city's name
    print("Yes, there's'SANTO' in the city's name!")
else:
    print("No, there's no 'SANTO' in the city's name!")
