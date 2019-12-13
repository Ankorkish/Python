n=int(input())
m=int(input())
sod=int(input())
c=[]
per=4
for k in range(n):
    c.append(["D"]*m)
if ((m*n)-sod<4 and n!=1 and m!=1) or (n==1 and sod!=m) or (m==1 and sod!=n):
    c="IMPOSSIBLE"
    n=0
elif n==1:
    n=0
    c=["D"]*m
elif m==1:
    m=0
    c=["D"]*n
if n!=0 and m!=0:
    c[0][0]="R"
    c[0][1]="D"
    c[1][0]="U"
    c[1][1]="L"
    for k in range(n):
        for k1 in range(m):
            if (k==0 and k1==0) or (k==0 and k1==1) or (k==1 and k1==0) or (k==1 and k1==1):
                continue
            if per<(m*n)-sod and k1!=0:
                c[k][k1]="L"
                sod+=1
                continue
            if per<(m*n)-sod and k1==0:
                c[k][k1]="U"
                sod+=1
                continue
if n!=0 and m!=0:
    for k in range(n):
        for k1 in range(m):
            print(c[k][k1],end="")
        print()
elif c=="IMPOSSIBLE" and n==0:
    print(c)
elif n==0 and c!="IMPOSSIBLE":
    for k in range(m):
        print(c[k],end="")
elif m==0 and c!="IMPOSSIBLE":
    for k in range(n):
        print(c[k])
    
