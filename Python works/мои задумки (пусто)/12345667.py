a=int(input())
for k in range(1,a):
    for k1 in range(2,k):
        if k%k1==0:
            break
    else:
        print("elif a=="+str(k)+":")
        print("    print(b)")
