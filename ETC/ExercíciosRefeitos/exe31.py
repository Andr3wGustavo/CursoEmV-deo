# Develop a program that asks the distance of a trip in Km.
# Calculate the price of the ticket, charging R$ 0.50 per Km for trips of up to 200Km
# and R$ 0.45 for longer trips.
distance = float(input('Type the trip distance: [Km] '))
if distance <= 200:
    price = distance * 0.5
else:
    price = distance * 0.45
print(f'The price will be R${price:2f}')

