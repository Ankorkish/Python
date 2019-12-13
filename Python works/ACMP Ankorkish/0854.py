a,b=map(int,input().split())
mode=str(input())
if mode=="auto":
    print(b)
if mode=="freeze" and b<=a:
    print(b)
elif mode=="freeze" and b>=a:
    print(a)
if mode=="heat" and b>=a:
    print(b)
elif mode=="heat" and b<=a:
    print(a)
if mode=="fan":
    print(a)
