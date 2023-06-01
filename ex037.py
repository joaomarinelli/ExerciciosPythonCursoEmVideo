while True:
    numero = int(input('Digite um numero para converter: '))

    print('-------'*5)
    print('[1] - Binário')
    print('[2] - Octal')
    print('[3] - Hexadecimal')
    print('[x] - Sair')

    opcao = str(input('Digite a opção que deseja converter: '))
    if opcao == 'x' or opcao == 'X':
        print('Saindo...')
        break

    elif opcao == '1' or opcao == '2' or opcao == '3':
        if opcao == '1':
            bin = str(bin(numero))
            print(bin)
        elif opcao == '2':
            oct = str(oct(numero))
            print(oct)
        elif opcao == '3':
            hexa = str(hex(numero))
            print(hexa)

    else:
        print('Opção invalida')


