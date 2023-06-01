import datetime
nasc = int(input('Informe ano de nascimento: '))

ano_atual = datetime.date.today()

#print(ano_atual.year)

calc_idade = ano_atual.year - nasc

print('Sua idade é {}'.format(calc_idade))

if calc_idade < 18:
    print('Voce ainda deverá se alistar em {} ano(s)'.format(18-calc_idade))
elif calc_idade == 18:
    print('Voce deve se alistar esse ano')
else:
    print('Sua idade de laistamento foi ha {} anos'.format(calc_idade-18))

