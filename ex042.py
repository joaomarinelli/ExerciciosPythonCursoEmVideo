r1 = float(input('Digite o comprimento da primeira reta: '))
r2 = float(input('Digite o comprimento da segunda reta: '))
r3 = float(input('Digite o comprimento da segunda reta: '))

if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('PODEM formar triangulo')
    if r1 == r2 == r3:
        print('Tringulo Equilatero')
    elif r1 == r2 or r1 == r3 or r2 == r3:
        print('Tringulo Isoceles')
    else:
        print('Tringulo Escaleno')
else:
    print('NÃO PODEM formar o triangulo')

