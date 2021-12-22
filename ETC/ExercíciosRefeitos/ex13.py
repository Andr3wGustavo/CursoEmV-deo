# Make an algorithm that reads an employee's salary and shows his new wage, with a 15% increase.

wage = int(input("Type the employee's wage: "))
print(f"The employe's new wage is ${wage + (wage*15)/100:.2f}")
# basicaly this sum the 15% increase.
