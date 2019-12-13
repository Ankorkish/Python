a=int(input())
mas=[1,1]+[0]*(a)
mas[2]==2
for k in range(2,a+1):
    mas[k]=mas[k-1]+mas[k-2]+mas[k-3]
print(mas)
print(mas[a])
