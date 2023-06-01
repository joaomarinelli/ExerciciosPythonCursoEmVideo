import random
from time import sleep
num = random.randint(0,5)

NumeroEscolhido = int(input('Qual foi o numero entre 0 e 5 escolhido pelo computador? '))
print('PROCESSANDO...')
sleep(2)

if (NumeroEscolhido == num):
    print('\033[4mParabéns\033[m, Voce acertou! O número escolhido foi {}'.format(num))
else:
    print('\033[4mVoce errou!\033[m tente novamente')

