secreto = 'mar'
letra_digitada = []
chances = 3

while True:
    if chances == 0:
        print('Você perdeu')
        break

    letra = input('Digite uma letra: ')
    letra = letra.lower()

    if len(letra) > 1:
        print('Ahhh isso não vale, digite apenas uma letra.')
        continue

    if letra in secreto:
        letra_digitada.append(letra)
        print(f'UHUUULL, a letra "{letra}" existe na palavra secreta')
    else:
        print(f'AFFFzzz, a letra "{letra}" NÃO EXISTE  na palavra secreta. ')

    secreto_temporario = ''
    for letra_secreta in secreto:
        if letra_secreta in letra_digitada:
            secreto_temporario += letra_secreta
        else:
            secreto_temporario += '*'

    if secreto_temporario == secreto:
        print(f'Que legal, VOCÊ GANHOU!!! A palavra era "{secreto_temporario.upper()}"')
        break
    else:
        print(f'A palavra secreta está assim: {secreto_temporario}')

    if letra not in secreto:
        chances -= 1

    print(f'Você ainda tem {chances} chances.')
    print()
