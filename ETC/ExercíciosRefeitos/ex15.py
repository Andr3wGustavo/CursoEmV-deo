# Write a program that asks the number of kilometers a car has driven
# and the number of days it has been rented. Calculate the price to pay
# knowing that the car costs  $60 per day and $ 0.15 per km driven.

rental_days = float(input('How many rental days: '))
kilometers = float(input('How many kilometers driven: '))
print(f'The total to pay is ${rental_days*60 + kilometers*0.15:.2f}')
# this program will sum, and shows the total to pay
