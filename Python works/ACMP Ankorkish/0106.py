a=int(input())
g=r=0
for k in range(a):
    b=int(input())
    if b==1:
        g+=1
    else:
        r+=1
print(min(g,r))
        
