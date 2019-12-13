n=int(input())
res=1
for k in range(2,1000):
    p=k
    while n%k==0:
        n//=k
        p*=k
    res*=(p-1)//(k-1)
print(res)
