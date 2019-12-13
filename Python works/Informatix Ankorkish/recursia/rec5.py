def q(a,c):
    if c==len(a)-1:
        print(a[c],end="")
    else:
        print(str(a[c]),end="")
        q(a,c+1)
    if a[c]=="(":
        print(")",end="")
    else:
        print(a[c],end="")
a=list(input())
q(a,0)
