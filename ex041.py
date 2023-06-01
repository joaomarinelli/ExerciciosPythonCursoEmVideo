from datetime import date
ano_nasc = int(input('Informe o ano de nascimento do atleta: '))

ano_atual = date.today().year

calc_idade = ano_atual - ano_nasc

print(calc_idade)

if calc_idade <= 9:
    print('MIRIM')

elif calc_idade <= 14:
    print('INFANTIL')
elif calc_idade <= 19:
    print('JUNIOR')
elif calc_idade <= 20:
    print('SÊNIOR')
else:
    print('MASTER')
