#Задача 2.36
print('Конвертация температуры из Цельсия в Фаренгейт и в Кельвин')
C=float(input())
F=C*1.8+32
K=C+273.15
print('{0} градусов по Цельсию равно {1} градусов по Фаренгейту'.format(C, round(F,2)))
print('{0} градусов по Цельсию равно {1} градусов по Кельвину'.format(C, round(K,2)))
