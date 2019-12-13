a=int(input())
mas=[1]*2+[0]*(a+3)
for k in range(2,a+3):
    mas[k]=mas[k-1]+mas[k-2]
print(mas)
