nome = str(input('Digite seu nome completo: ')).strip()

print(nome.upper())
print(nome.lower())

nome2 = nome.replace(' ','')

print('Seu nome tem {} caracteres'.format(len(nome2)))

separandoNome = nome.split()
primeiroNome = separandoNome[0]
print('Seu primeiro nome tem {} letras'.format(len(primeiroNome)))