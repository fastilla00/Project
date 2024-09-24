#Задача 2.6
from math import sqrt
R = 6350
for d in range(1, 11):
    H = sqrt((R+d)**2-R**2)
    print('d =', d, 'км', '  H =', round(H), 'км')
