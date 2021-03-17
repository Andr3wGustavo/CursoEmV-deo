# Make a program that reads a number from 0 to 9999
# and shows each of the separate digits on the screen.
num = str(input('Type a number here: '))
divi = ' '.join(num).split(num)  # this will divide the number and join it with a space
print(f'Unidade: {num[3]} ')
print(f'Dezena: {num[2]}')
print(f'Centena: {num[1]}')
print(f'Milhar: {num[0]}')
