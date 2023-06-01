from time import sleep
vlr_casa = float(input('Informe o valor do imovel: '))
salario = float(input('Informe o seu salário: '))
anos = int(input('Em quantos anos deseja financiar ete imovel? '))

prestacao = vlr_casa / (anos * 12)



print('O valor da prestação ficará: {:.3f}'.format(prestacao))

print('Aguarde. Estamos procurando as melhores opções')

sleep(2)


calculo_renda = salario * 0.3

if prestacao > calculo_renda:
    print('Emprestimo negado! O valor da prestação excedeu 30% da sua renda mensal')
else:
    print('Emprestimo aprovado!')
