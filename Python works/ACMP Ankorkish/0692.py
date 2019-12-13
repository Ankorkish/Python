import sys
a=int(input())
k=2
if a==1:
    print("YES")
    sys.exit()
if a<0:
    per=0
    a*=-1
    while a>=k:
        if k==a and per%2==0:
            print("YES")
            break
        k*=2
        per+=1
    else:
        print("NO")
else:
    while a>=k:
        if k==a:
            print("YES")
            break
        k*=2
    else:
        print("NO")
