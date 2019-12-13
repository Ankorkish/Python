a,b=map(int,input().split(":"))
c,d=map(int,input().split())
per=b+d
per2=a+c
if per>=60:
    per%=60
    per2+=1
if per2%24<10:
    print("0"+str(per2%24)+":",end="")
else:
    print(str(per2%24) + ":", end="")
if per<10:
    print("0"+str(per))
else:
    print(str(per))