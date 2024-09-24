n=int(input())
if n<=99 and n>=10:
    w= n%10
    e=n//10
    print(w,'единиц,', e,'десятков')
else:
    print('нет такого номера')

