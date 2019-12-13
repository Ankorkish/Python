a=int(input())
b=int(input())
x=0
while True:
    x+=a
    if (x+2)%b==0:
        c=x+1
        break
print(c)
