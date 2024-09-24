n=int(input())
if n<=999 and n>=100:
    n1= n//100
    n2=n//10%10
    n3=n%10
    print(f'{n1}, {n2}, {n3}')
else:
    print('нет такого числа')

