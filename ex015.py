km = float(input('Quantos KM o veiculo percorreu? '))
dias = int(input('Por quantos dias o veiculo foi alugado? '))

preço = (60 * dias) + 0.15 * km

print('O preço do total do aluguel foi: R${:.2f}'.format(preço))