def q(a):
    if len(a)==1:
        return a[0]
    return a[0]+"*"+q(a[1:])
a=input()
print(q(a))

