a=str(input())
b=list(a)
c=0;ht=0;oppo=0
while True:
    for k in range(len(b)//2):
        if b[k]!=b[len(b)-1-k]:
            if b[len(b)-2-k]==b[k]:
                c=len(b)-k
                break
            else:
                c=k
                ht=1
                oppo=1
                break
    else:
        c=0
        break
    
    b=b[k:len(b)-k-1]
    if len(b)%2==1:
        ch=1
    else:
        ch=0
    f1=b[0+ht:len(b)//2+ch+ht]
    f2=b[len(b)//2:len(b)]       
    if ht==0:
        f2=f2[::-1]
    if f1!=f2:
        c=0
        oppo=0
        break
    break
print(c+oppo)
