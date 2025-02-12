frase = ''
now = ''
while True:
    word = input('Please type in a word:')

    if word == 'end' or word == now:
        break
    now = word
    frase += word + ' '

print(frase)

