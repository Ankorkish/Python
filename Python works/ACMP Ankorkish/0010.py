a,b,c,d=map(int,input().split())
mas=[]
for k in range(-100,100+1):
    if a*k**3+b*k**2+c*k+d==0:
        mas.append(k)
for k in mas:
    print(k,end=" ")
