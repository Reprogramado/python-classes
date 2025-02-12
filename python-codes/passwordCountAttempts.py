password = '4321'
tentas = 0
while True:
    trys = input('PIN: ')
    tentas += 1
    if tentas == 1 and trys == password:
        print('Correct! It only took you one single attempt!')
        break
    elif trys != password:
        print('Wrong')
    elif tentas > 1 and trys == password:
        print(f'Correct! It took you {tentas} attempts')
        break
