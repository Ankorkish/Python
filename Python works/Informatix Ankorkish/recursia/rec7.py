def q(a,c,k):
    if c+1==len(a)//2:
        if a[c]==a[len(a)-c-1]:
            return k
        else:
            p=len(k)//2
            p1=p+1
            k.insert(p,a[c])
            k.insert(p1,a[len(a)-c-1])
            return k
    else:
        k=q(a,c+1,k)
        if a[c]==a[len(a)-c-1]:
            return k
        else:
            p=len(k)//2
            p1=p+1
            k.insert(p,a[c])
            k.insert(p1,a[len(a)-c-1])
            return k
a=list(input());k=[]
k=q(a,0,k)
k=k[::-1]
k=k[len(k)//2::]+k[:len(k)//2:]
#if len(a)%2==1:
#    k.insert()
for k1 in k:
    print(k1,end="")
