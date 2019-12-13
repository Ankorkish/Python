import sys
a=int(input())
if a==1:
    print(0)
    sys.exit()
if a%2==0:
    print(a//2)
else:
    print(a)
