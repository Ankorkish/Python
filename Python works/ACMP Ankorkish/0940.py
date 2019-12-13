a,b=map(str,input().split())
a=int(a)
b=list(b)
b.pop(a-1)
for k in b:
    print(k,end="")
