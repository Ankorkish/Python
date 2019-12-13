def q(a,c):
    if c==len(a)-1:
        print(a[c])
    else:
        print(str(a[c]),end="")
        if c+1<len(a)/2:
            print("(",end="")
        if c+1>len(a)/2:
            print(")",end="")   
        q(a,c+1)
a=list(input())
q(a,0)
