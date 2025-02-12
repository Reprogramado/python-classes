ano_usuario = int(input("Digite um ano: "))

if (ano_usuario % 4 == 0 and ano_usuario % 100 != 0) or (ano_usuario % 400 == 0):
    proximo_ano = ano_usuario + 1
    while True:
        if (proximo_ano % 4 == 0 and proximo_ano % 100 != 0) or (proximo_ano % 400 == 0):
            print(f"The next leap year after {ano_usuario} is {proximo_ano}")
            break
        proximo_ano += 1
else:
    proximo_ano = ano_usuario + 1
    while True:
        if (proximo_ano % 4 == 0 and proximo_ano % 100 != 0) or (proximo_ano % 400 == 0):
            print(f"The next leap year after {ano_usuario} is {proximo_ano}")
            break
        proximo_ano += 1