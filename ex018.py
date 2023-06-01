import math
angulo = float(input('Digite o angulo: '))

sen = math.sin(math.radians(angulo))
cos = math.cos(math.radians(angulo))
tan = math.tan(math.radians(angulo))

print('O seno de {} é {:.2f} \ncoseno de {} é {:.2f} \ntangente de {} é {:.2f}'.format(angulo, sen, angulo, cos, angulo, tan))