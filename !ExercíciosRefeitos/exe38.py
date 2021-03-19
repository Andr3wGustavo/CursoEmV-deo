# Write a program that reads two whole numbers and compares them. Showing a message on the screen:
# The first value is greater
# The second value is higher
# There is no greater value, the two are equal
num1 = int(input('Type a number: '))
num2 = int(input('Type a number: '))
if num1 > num2:
    maior = num1
    print(f'{maior} is greater than {num2}!')
elif num2 > num1:
    maior = num2
    print(f'{maior} is greater than {num1}!')
else:
    print("There's no a greater number.")
