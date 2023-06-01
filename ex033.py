n1 = int(input('Digite o primeiro numero: '))
n2 = int(input('Digite o segundo numero: '))
n3 = int(input('Digite o terceirop numero: '))

if (n1 > n2) & (n1 > n3):
    print('O maior numero é {}'.format(n1))

elif (n2 > n1) & (n2 > n3):
    print('O maior numero é {}'.format(n2))

else:
    print('O maior numero é {}'.format(n3))

if (n1 < n2) & (n1 < n3):
    print('O menor numero é {}'.format(n1))
elif (n2 < n1) & (n2 < n3):
    print('O menor numero é {}'.format(n2))
else:
    print('O menor numero é {}'.format(n3))