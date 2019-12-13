n=int(input())
m=int(input())
sod=int(input())
d=[]
c=[]
per=4
for k in range(n):
    d.append([0]*m)
for k in range(n):
    c.append(["D"]*m)
if ((m*n)-sod<4 and sod!=0) or n==1 or m==1:
    c="IMPOSSIBLE"
    n=0
else:
    d[0][0]=1
    d[0][1]=1
    d[1][0]=1
    d[1][1]=1
    c[0][0]="R"
    c[0][1]="D"
    c[1][0]="U"
    c[1][1]="L"
for k in range(n):
    for k1 in range(m):
        if d[k][k1]!=1:
            if per<(m*n)-sod:
                d[k][k1]=1
                sod+=1
for k in range(n):
    for k1 in range(m):
        if (k==0 and k1==0) or (k==0 and k1==1) or (k==1 and k1==0) or (k==1 and k1==1):
            continue
        if d[k][k1]==1 and k1!=0:
            c[k][k1]="L"
            continue
        if d[k][k1]==1 and k1==0:
            c[k][k1]="U"
            continue
if n!=0:
    for k in range(n):
        for k1 in range(m):
            print(c[k][k1],end=" ")
        print()
else:
    print(c)
