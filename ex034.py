salario = float(input('Digite o salario do funcionário: R$'))

if salario > 1.250:
    aumento = (salario * 0.10) + salario
    print('O salario, apos aumento, será R${:.2f}'.format(aumento))
else:
    aumento = (salario * 0.15) + salario
    print('Apos aumento, o salario ficará R${:.2f}'.format(aumento))