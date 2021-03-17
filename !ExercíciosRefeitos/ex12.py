# Make an algorithm that reads the price of a product and shows its new price, with 5% discount.

price = float(input('Type the product price: '))
print(f'With 5% off, this product will cost {price - (price*5)/100:.2f} now.')
# this program right here verify the new price by subtracting the 5% of the price
