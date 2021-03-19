#  Write a program that asks for an employee's salary and calculates the amount of your increase.
#  For salaries over $ 1250.00, calculating an increase of 10%.
#  For those who are less than or equal, the increase is 15%.
wage = float(input('Type the wage amount: '))
if wage >= 1250:
    increase = wage + (wage*10/100)
else:
    increase = wage + (wage*15/100)
print(f'The new wage is R${increase:.2f}')
