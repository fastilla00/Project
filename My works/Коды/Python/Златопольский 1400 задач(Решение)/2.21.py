#Задача 2.21
print('Значения функций')
import math
e=float(input('Введите значение переменной e:'))
f=float(input('Введите значение переменной f:'))
g=float(input('Введите значение переменной g:'))
h=float(input('Введите значение переменной h:'))
a=(e+f/2)/3
b=abs(h**2-g)
c=math.sqrt(abs((g-h)**2-3*math.sin(e)))
print('Значение первой функции:', round(a,2))
print('Значение второй функции:', round(b,2))
print('Значение третьей функции:', round(c,2))
