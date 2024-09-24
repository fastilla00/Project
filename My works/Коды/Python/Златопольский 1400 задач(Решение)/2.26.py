x1,y1= map(float,input('Введите первые координаты:').split())
x2,y2= map(float,input('Введите вторые координаты:').split())
r=((x2-x1)**2+(y2-y1)**2)**0.5
print('Расстояние:',round(r,2))
