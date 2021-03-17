# Make a program that reads a sentence on the keyboard
# and shows how many times the letter "A" appears
# and what position it appears the first time
# and in what position it appears the last time.

sentence = str(input('Write something: ')).upper().strip()
print(f'The sentece has {sentence.count("A")} letters A')
print(f'The first time that an A appears is at the position {sentence.find("A", 0) +1}')
print(f'The last time that an A appears is at the position {sentence.rfind("A") +1}')
# basically this programm will find and count how many A's there are in a sentence
# using the comands above, i just have to alter the order and sum 1 to the position
