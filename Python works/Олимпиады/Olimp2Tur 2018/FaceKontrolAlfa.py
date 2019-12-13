import sys
x,a,b=map(int,input().split())
mas=set(str(input()))
schet=0
if 5 not in mas and 0 not in mas and x==5:
    print(0)
    sys.exit(0)
if a%x!=0:
    a+=(((a//x)+1)*x)-a
if b%x!=0:
    b-=b-(b//x)*x   
for k in range(a,b+1,x):
    for k1 in list(str(k)):
        if k1 not in mas:
            break
    else:
        schet+=1
print(schet)
