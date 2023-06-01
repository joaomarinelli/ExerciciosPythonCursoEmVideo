cidade = input('Digite o nome da cidade: ').strip()

cidade = cidade.upper()
cidadeSepara = cidade.split()


print(cidade)

if(cidadeSepara[0] == 'SANTO'):
    print('Começa com Santo')
else:
    print('Nao começa com SANTO')