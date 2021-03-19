# Make a program that reads three numbers and shows which is the greatest and which is the smallest.
num1 = int(input('Type the first number: '))
num2 = int(input('Type the second number: '))
num3 = int(input('Type the third number: '))
numbers = [num1, num2, num3]  # this allows us create a list where the numbers will be storage
print(f'The greatest number is {max(numbers)}')
print(f'The smallest number is {min(numbers)}')
