n=int(input())
if n<=99 and n>=10:
    w= n%10
    e=n//10
    r=w+e
    print(r, 'сумма цифр')
else:
    print('нет такого числа')

