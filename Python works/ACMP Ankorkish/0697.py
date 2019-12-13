x,y,z=map(int,input().split())
S=(x*z+y*z)*2
if S%16==0:
    print(S//16)
else:
    print(S//16+1)
