# Write a program to approve the bank loan for the purchase of a home. Ask the price of the house, the buyer's salary
# and how many years he will pay. The monthly installment cannot exceed 30% of the salary or the loan will be denied.
price = float(input("House's price: R$"))
wage = float(input("Buyer's wage: R$"))
years = int(input('How many years will you pay? '))
if (years * 12) >= (wage * 30) / 100:
    print(f'''To pay a house that costs {price} in {years}years, you will pay R${price / years * 12:.2f} monthly. 
So the loan CAN be ACCEPTED!''')
else:
    # this is the formular that is using in the program
    print(f'''To pay a house that costs {price} in {years}years, you will pay R${price / years * 12:.2f} monthly. 
So the loan CANNOT be ACCEPTED!''')
