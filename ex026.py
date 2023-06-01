frase = input('Digite uma frase: ').strip().upper()

print('A frase contem {} vezes a letra A'.format(frase.count('A')))

print('A letra A aparece pela primeira vez na posição {}'.format(frase.find('A')+1))
print('A letra A aparece pela ultima vez na posição {}'.format(frase.rfind('A')+1))
