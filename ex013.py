sal = float(input('Informe o salário: '))
aum = float(input('Agora informe o percentual de aumento: '))

perc = aum / 100
calc = sal+(sal*perc)

print('O novo salário é R${:.2f}'.format(calc))
print('Corresponde a um aumento de R${:.2f}'.format(calc-sal))