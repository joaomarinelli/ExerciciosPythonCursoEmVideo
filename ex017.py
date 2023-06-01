import math
opo = float(input('Informe o cateto oposto: '))
adj = float(input('Informe o cateto adjacente: '))

hipo = math.hypot(opo, adj)

'''hipo = (opo ** 2 + adj ** 2) ** (1/2)'''

print('A hipotenusa desse triangulo é {:.3f}'.format(hipo))