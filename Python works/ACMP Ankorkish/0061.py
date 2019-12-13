fir=sec=0
for k in range(4):
    a,b=map(int,input().split())
    fir+=a
    sec+=b
if fir>sec:
    print(1)
elif fir==sec:
    print("DRAW")
else:
    print(2)
