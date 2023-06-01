nome = input('Digite seu nome: ').strip()

nome = nome.upper()
#nome = nome.split()

print(nome)

if("SILVA" in nome):
    print('Tem SILVA no nome')
else:
    print('Nao tem SILVA no nome')