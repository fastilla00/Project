n = input()
n1 = int(n) % 10
n2 = int(n) // 10 % 10
n3 = int(n[0]) + int(n[1]) + int(n[2])
n4 = int(n[0]) * int(n[1]) * int(n[2])
print('Число единиц:', n1)
print('Число десятков:', n2)
print('Сумма цифр в числе:', n3)
print('Произведение цифр в числе:', n4)

