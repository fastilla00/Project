import math
r1=float(input('Введите внешний радиус:'))
r2=float(input('Введите внутренний радиус:'))
s=(r1**2-r2**2)* math.pi
print('Площадь кольца:',math.ceil(s))
