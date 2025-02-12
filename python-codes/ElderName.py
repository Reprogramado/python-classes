print('Person 1:')
firstName = input('Name: ')
firstAge = int(input('Age: '))
print('Person 2: ')
secondName = input('Name: ')
secondAge = int(input('Age: '))

if firstAge > secondAge:
    print(f'The elder is {firstName}')
elif firstAge < secondAge:
    print(f'The elder is {secondName}')
else:
    print(f'{firstName} and {secondName} are the same age')