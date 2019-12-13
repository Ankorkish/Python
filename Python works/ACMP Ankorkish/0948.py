k,n=map(int,input().split())
per=n//k
per2=n-(per*k)
if per2==0:
    per-=1
    per2=k
print(per+1,per2)
