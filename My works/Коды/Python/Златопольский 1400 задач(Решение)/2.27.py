#Задача 2.27
import math
print('Даны основания и высота равнобедренной трапеции. Найти периметр трапеции.')
a=float(input('Введите первое основание:'))
b=float(input('Введите второе основание:'))
h=float(input('Введите высоту:'))
p=a+b+2*math.sqrt(h**2+((a-b)**2)/4)
print('Периметр трапеции равен',round(p,2))
