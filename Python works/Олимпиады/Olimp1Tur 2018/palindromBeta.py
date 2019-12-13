import sys
b=list(input());c=0
for k in range(len(b)//2):
    if b[k]!=b[len(b)-k-1]:
        if b[len(b)-2-k]==b[k]:
            c=len(b)-k
            b.pop(len(b)-k)
            for k1 in range(k,len(b)//2):
                if b[k1]!=b[len(b)-k1-1]:
                    print(0)
                    sys.exit(0)
            else:
                print(c)
                sys.exit(0)            
        else:
            c=k
            b.pop(k)
            for k1 in range(k,len(b)//2):
                if b[k1]!=b[len(b)-k1-1]:
                    print(0)
                    sys.exit(0)
            else:
                print(c)
                sys.exit(0)
else:
    print(0)
print(len(b))

