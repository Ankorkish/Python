def q(a):
    if len(a)==2 and a[0]!=a[-1]:
        return a
        print(1234)
    if len(a)==2 and a[0]==a[-1]:
        return ""
    if len(a)==1:
        return a
    if a[0]!=a[-1]:
        return a[0]+q(a[1:-1])+a[-1]
    else:
        return q(a[1:-1])
a=str(input())
print(q(a))
