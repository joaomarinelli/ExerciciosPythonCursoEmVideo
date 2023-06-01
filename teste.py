
descicao_produto = str(input('Descrição do produto: '))
qtde = int(input('Informe a Quantidade: '))
valor_produto = float(input('Informe o valor do produto: R$'))

total = qtde * valor_produto


print('O valor total é de {:.2f}'.format(qtde * valor_produto))

if qtde <= 5:
    total_pagar = total-(total*0.02)
    print('Comprando {} unidades, voce ganha 2% de desconto e o total a pagar será de R${:.2f}'.format(qtde, total_pagar))
elif qtde > 5 and qtde <=10:
    total_pagar = total - (total * 0.03)
    print('Comprando {} unidades, voce ganha 3% de desconto e o total a pagar será de R${:.2f}'.format(qtde, total_pagar))
    desconto = 0.03
else:
    total_pagar = total - (total * 0.05)
    print('Comprando {} unidades, voce ganha 5% de desconto e o total a pagar será de R${:.2f}'.format(qtde, total_pagar))
