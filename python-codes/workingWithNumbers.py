sum = 0
counter = 0
countPositive = 0
countNegative = 0

while True:
    print('Please type in integer numbers. Type in 0 to finish.')
    number = int(input('Number: '))
    counter += 1
    if number == 0:
        counter -= 1
        break
    if number > 0:
        countPositive += 1
    elif number < 0:
        countNegative += 1
    sum += number

mean = sum / counter

print(f'Numbers typed in {counter}')
print(f'The sum of the numbers is {sum}')
print(f'The mean of the numbers is {mean}')
print(f'Positive numbers {countPositive}')
print(f'Negative numbers {countNegative}')