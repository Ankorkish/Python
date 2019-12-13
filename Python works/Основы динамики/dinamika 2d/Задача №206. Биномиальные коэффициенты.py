a,b=map(int,input().split())
mas=[]
for k in range(a):
    mas.append([1]*b)
for k in range(1,a):
    for k1 in range(1,b):
        mas[k][k1]=mas[k][k1-1]+mas[k-1][k1]
print(mas[a-1][b-1])
