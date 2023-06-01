n1 = float(input('infome primeira nota: '))
n2 = float(input('Informe a segunda nota: '))

media = (n1 + n2) / 2

if media < 5.0:
    print('REPROVADO')
elif media == 5.0 or media < 7.0:
    print('RECUPERAÇÃO')
else:
    print('APROVADO')