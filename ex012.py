p = float(input('Qual o preço do produto? R$'))
d = float(input('Qual o valor do desconto em porcentagem? '))

dp = d / 100
dr = p-(p*dp)

print('O produto que tem valor original de R${:.2f}, com desconto de {:.1f}% ficará com valor de R${:.2f}'. format(p, d, dr))
print('Um desconto de R${:.2f}'.format(p-dr))