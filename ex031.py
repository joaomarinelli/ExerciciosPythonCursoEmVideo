d = int(input('Digite a distancia da viagem: '))

if d <= 200:
    print('O preço da tarifa é R$0,50. Para essa viagem, o total da tarifa será: R${:.2f}'.format(d * 0.50))
else:
    print('O preço da tarifa é R$0,45. Para essa viagem, a total da tarifa será: R${:.2f}'.format(d * 0.45))