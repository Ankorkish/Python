k=int(input())
b=list(map(int,input().split()))
b=b[::-1]
print(" ".join(str(k) for k in b))
