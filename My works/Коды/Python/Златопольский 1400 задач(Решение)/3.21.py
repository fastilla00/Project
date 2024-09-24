N = int(input())
n2 = int(N/100)
n1 = int((N-n2*100)/10)
n0 = N%10
print("Сотни: ", n2)
print("Десятки: ", n1)
print("Единицы: ", n0)
print("Другое число: ", n0*100 + n1*10 + n2)

