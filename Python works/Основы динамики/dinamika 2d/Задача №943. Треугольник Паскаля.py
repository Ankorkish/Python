a=int(input())
c=1
mas=[]
for k in range(a):
    mas.append([1]+[0]*(a-1))
for k in range(a):
    for k1 in range(1,c):
        mas[k][k1]=mas[k-1][k1-1]+mas[k-1][k1]
    c+=1
c=1
for k in range(a):
    for k1 in range(c):
        print(mas[k][k1],end=" ")
    print()
    c+=1
    
