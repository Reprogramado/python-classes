letterOne = input('1st letter: ')
letterTwo = input('1st letter: ')
letterThree = input('1st letter: ')

if letterOne > letterTwo and letterOne > letterThree:
    if letterTwo > letterThree:
        print(f'The letter in the middle is {letterTwo}')
    else:
        print(f'The letter in the middle is {letterThree}')
elif letterTwo > letterOne and letterTwo > letterThree:
    if letterOne > letterThree:
        print(f'The letter in the middle is {letterOne}')
    else:
        print(f'The letter in the middle is {letterThree}')
elif letterThree > letterOne and letterThree > letterTwo:
    if letterOne > letterTwo:
        print(f'The letter in the middle is {letterOne}')
    else:
        print(f'The letter in the middle is {letterTwo}')