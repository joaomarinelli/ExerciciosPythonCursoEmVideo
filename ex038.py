n1 = int(input('Digite o primeiro numero: '))
n2 = int(input('Digite o segundo numero: '))

if n1 > n2:
    print('O numero {} é maior que {}'.format(n1,n2))
elif n1 == n2:
    print('Não existe valor maior. Os dois numeros são iguais')
else:
    print('O numero {} é maior que {}'.format(n2,n1))