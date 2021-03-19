# Create a program that read two notes from one person and calculated their mean
# showing a non-final message, according to the mean:
# Average below 5.0: REPROVED
# Medium between 5.0 and 6.9: RECOVERY
# Medium 7.0 or higher: APPROVED
grade1 = float(input('Type the first grade: '))
grade2 = float(input('Type the second grade: '))
grade3 = float(input('Type the third grade: '))
print(f'The average is {(grade1 + grade2 + grade3) / 3}')
if (grade1 + grade2 + grade3) / 3 < 5.0:
    print('The stundent is REPROVED')
elif 5.0 > (grade1 + grade2 + grade3) / 3 < 6.9:
    print(f'The studend will be in RECOVERY')
else:
    print(f'The studed is APPROVED ')
