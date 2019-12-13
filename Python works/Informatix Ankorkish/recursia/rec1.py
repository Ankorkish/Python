def rec1(b):
    if b>1:
        a=rec1(b-3)
        k=rec1(b-5)
    if b==1:
        return 1
a=int(input())
print(rec1(a))
