a=int(input());c=0
b=list(map(int,input().split()))
for k in b:
    if k>0:
        c+=k
print(c,end=" ")
c=1
if b.index(min(b))<b.index(max(b)):
    for k in range(b.index(min(b))+1,b.index(max(b))):
        c*=b[k]
else:
    for k in range(b.index(max(b))+1,b.index(min(b))):
        c*=b[k]
print(c)
