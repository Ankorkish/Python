def wow(a):
    if len(a)==1 or len(a)==2:
        return a
    return a[0]+"("+wow(a[1:-1])+")"+a[len(a)-1]
a=str(input())
print(wow(a))
#replace()
