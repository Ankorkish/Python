def q(a,b):
    if max(a,b)%min(a,b)==0:
        return min(a,b)
    else:
        return q(min(a,b),max(a,b)%min(a,b))
a,b=map(int,input().split())
print(q(a,b))
