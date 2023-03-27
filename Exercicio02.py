def multiplo(*n):

    n1 = int(input('Digite o primeiro número: '))
    n2 = int(input('Digite o segundo número: '))

    if n2 % n1 == 0:
        print(f'{n2} é multiplo de {n1}')

    else:
        print(f'{n1} não é multiplo de {n2}')


multiplo()
