i=int(input())
mas=[1,1,3]+[0]*i
for k in range(3,i+3):
    mas[k]=mas[k-1]*2+mas[k-2]*2
print(mas[i+1])
