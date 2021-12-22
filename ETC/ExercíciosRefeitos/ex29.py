# Write a program that reads the speed of a car. If he exceeds 80 km/h
# show a message saying that he was fined.
# The fine will cost R $ 7.00 for each Km above the limit.
velocity = int(input("Type the car's velocity:[Km/h]  "))
if velocity > 80:  # if the velocity are greater than 80km the driver will be fined
    print("You were fined, it'll cost {:2f}R$".format(7 * (velocity - 80)))
else:
    print("Great, you're within the speed limit")
