# Create a program that reads how much money a person has in their wallet
# and shows how many dollars they can buy.

num = float(input('How much money do you have? [R$]  '))
print(f'With R${num} you can buy ${num/5.48:.2f}.')
# this converts real to dollars by dividing the real for dollars
