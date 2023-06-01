r = float(input('Quantos reais voce tem na carteira? R$'))
d = float(input('Qual a cotação do dolar atual? '))

s = r / d

print('Na cotação atual voce pode comprar US${:.2f} dolares '.format(s))