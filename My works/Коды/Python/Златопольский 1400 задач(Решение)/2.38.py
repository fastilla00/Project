#Задача 2.38
a=int(input('Введите первое число:'))
b=int(input('Введите второе число:'))
s=a+b
p=a*b
r=a-b
d=a/b
sa=(a+b)/2
print('Сумма: {0}+{1}={2}'.format(a,b,s))
print('Разность: {0}-{1}={2}'.format(a,b,r))
print('Произведение: {0}*{1}={2}'.format(a,b,p))
print('Деление: {0}/{1}={2}'.format(a,b,d))
print('Деление: ({0}+{1})/2={2}'.format(a,b,sa))
