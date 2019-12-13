qwertyuiop=int(input())
a=list(map(int,input().split()))
for k in a:
    if k<=437:
        print("Crash "+str(a.index(k)+1))
        break
else:
    print("No crash")
                
