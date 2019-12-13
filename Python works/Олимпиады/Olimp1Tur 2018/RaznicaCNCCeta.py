a=int(input())
b=int(input())
if a%2==0:
    if b%2==0:
        print(((b-a)//2)+a)
    else:
        print((((b-a)//2)+1)*-1)
else:
    if b%2==0:
        print(((b-a)//2)+1)
    else:
        print((((b-a)//2)+a)*-1)
