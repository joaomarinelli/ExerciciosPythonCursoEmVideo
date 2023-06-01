saldo = float(1000)


ValorRetirada = float(input('Quanto voce deseja retirar da conta? R$'))

#print('Sacado R${.:2f} com sucesso! \n Seu saldo atual é de R${:.2f}'.format(ValorRetirada) if ValorRetirada < saldo else 'Saldo insulficiente')

if (ValorRetirada < saldo):
    print('Sacado R${:.2f} com sucesso!'.format(ValorRetirada))
    print('Seu saldo atual é de R${:.2f}'.format(saldo-ValorRetirada))

else:
    print('Saldo insulficiente!')
