a=int(input())
mas=[0]*a;per=0
for k in range(a):
    mas[k]=list(map(int,input().split()))
for k in range(a):
    for k1 in range(a):
        if mas[k][k1]==1:
            per+=1
print(per//2)
