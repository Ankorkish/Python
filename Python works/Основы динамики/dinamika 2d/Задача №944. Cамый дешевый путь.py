n,m=map(int,input().split());mas=[]
for k in range(n):
    mas.append(list(map(int,input().split())))
for k in range(1,m):
    mas[0][k]=mas[0][k]+mas[0][k-1]
for k in range(1,n):
    mas[k][0]=mas[k][0]+mas[k-1][0]
for k in range(1,n):
    for k1 in range(1,m):
        mas[k][k1]=mas[k][k1]+min(mas[k][k1-1],mas[k-1][k1])
print(mas[n-1][m-1])
    
