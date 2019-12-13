a,b=map(int,input().split())
mas=[0]*(b+1)
mas[0]=1
for k in range(1,b+1):
    c=0
    for k1 in range (k-a,k):
        if k1<0:
            continue
        c+=mas[k1]
    mas[k]=c
print(mas[len(mas)-1])
