while True:

    preco = float(input('Informe o valor do produto: R$'))

    print('----- OPÇÕES DE PAGAMENTO -----')
    print('[1] - A vista no dinehiro/pix')
    print('[2] - A vista no cartão')
    print('[3] - Até 2x no cartão')
    print('[4] - 3x ou mais no cartão')
    print('[X] - SAIR')
    print('-------------------------------')

    opcao = str(input('Digite a opção desejada '))



    if opcao == 'x' or opcao == 'X':
        print('Saindo...')
        break
    elif opcao == '1' or opcao == '2' or opcao == '3' or opcao == '4':
        if opcao == '1':
            preco = preco - (preco*0.10)
            print('Nessa condição, o produto terá 10% de desconto. Custando R${:.2f}\n'.format(preco))
        elif opcao == '2':
            preco = preco - (preco*0.05)
            print('Nessa condição, o produto terá 5% de desconto. Custará R${:.2f}\n'.format(preco))
        elif opcao == '3':
            print('O produtoi custará R${:.2f} \n'.format(preco))
        elif opcao == '4':
            preco = preco + (preco*0.20)
            print('Nessa condição, será acrescido 20% de juros. Custará R${:.2f} \n'.format(preco))
    else:
        print('Opção inválida\n')