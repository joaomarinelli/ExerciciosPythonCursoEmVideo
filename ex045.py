import random


print('[1] - PEDRA')
print('[2] - PAPEL')
print('[3] - TESOURA')

opcao = int(input('Escolha uma opção para realizar a jogada: '))

opcao_pc = random.randint(1,3)

print(opcao,opcao_pc)

if opcao == 1 and opcao_pc == 3:
    print('Voce escolheu PEDRA e a maquina escolheu TESOURA. \n Voce ganhou!')
elif opcao == 2 and opcao_pc == 3:
    print('Voce escolheu PAPEL e a maquina escolheu TESOURA. \n Voce perdeu!')
elif opcao == 3 and opcao_pc == 3:
    print('Voce escolheu TESOURA e a máquina também. \n Ninguem ganhou!')
elif opcao == 1 and opcao_pc == 2:
    print('Voce escolheu PEDRA e a maquina escolheu PAPEL. \n Voce perdeu!')
elif opcao == 2 and opcao_pc == 2:
    print('Voce escolheu PAPEL e a máquina também. \n Ninguem ganhou!')
elif opcao == 3 and opcao_pc == 2:
    print('Voce escolheu TESOURA e a maquina escolheu PAPEL. \n Voce ganhou!')
elif opcao == 1 and opcao_pc == 1:
    print('Voce escolheu PEDRA e a máquina também. \n Ninguem ganhou!')
elif opcao == 2 and opcao_pc == 1:
    print('Voce escolheu PAPEL e a maquina escolheu PEDRA. \n Voce ganhou!')
elif opcao == 3 and opcao_pc == 1:
    print('Voce escolheu TESOURA e a maquina escolheu PEDRA. \n Voce perdeu!')