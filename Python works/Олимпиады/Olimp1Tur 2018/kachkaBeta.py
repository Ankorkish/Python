a=int(input())
b=int(input())
x=0
if a>b:
    while True:
        x+=a
        if (x+2)%b==0:
            c=x+1
            break
else:
    while True:
        x+=b
        if (x-2)%a==0:
            c=x-1
            break
print(c)
