velocidade = float(input('Digite a velocidade do veículo: '))

if (velocidade > 80):
    print('Motorista multado por trafegar na velocidade acima de 80km/h')
    multa = (velocidade - 80) * 7
    print('Voce devera pagar multa no valor de {:.2f}'.format(multa))
print('Tenha um bom dia e dirija com segurança!')