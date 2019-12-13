import sys
ch={'1','2','3','4','5','6','7','8'}
bk={'A','B','C','D','E','F','G','H'}
sl={"A":1,'B':2,'C':3,'D':4,'E':5,'F':6,'G':7,'H':8}
b=input()
c=list(b)
if len(c)!=5:
    print("ERROR")
    sys.exit()
if c[0] not in bk or c[3] not in bk or c[1] not in ch or c[4] not in ch or c[2]!="-":
    print("ERROR")
    sys.exit()
a,b=map(str,b.split('-'))
a=list(a)
b=list(b)
x1=int(sl[a[0]])
y1=int(a[1])
x2=int(sl[b[0]])
y2=int(b[1])
if x1+2==x2 and y1+1==y2:
    print('YES')
elif x1+2==x2 and y1-1==y2:
    print('YES')
elif y1+2==y2 and x1+1==x2:
    print('YES')
elif y1+2==y2 and x1-1==x2:
    print('YES')
elif y1-2==y2 and x1+1==x2:
    print('YES')
elif y1-2==y2 and x1-1==x2:
    print('YES')
elif y1-1==y2 and x1-2==x2:
    print('YES')
elif y1+1==y2 and x1-2==x2:
    print('YES')
else:
    print('NO')
