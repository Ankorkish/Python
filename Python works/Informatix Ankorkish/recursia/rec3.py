def q(a,c):
    if c==len(a)-1:
        if a[c]=="1" or a[c]=="2" or a[c]=="3"\
        or a[c]=="4" or a[c]=="5" or a[c]=="6"\
        or a[c]=="7" or a[c]=="8" or a[c]=="9" or a[c]==0:
            return 1
        else:
            return 0
    else:
        b=q(a,c+1)
        if a[c]=="1" or a[c]=="2" or a[c]=="3"\
        or a[c]=="4" or a[c]=="5" or a[c]=="6"\
        or a[c]=="7" or a[c]=="8" or a[c]=="9" or a[c]=="0":
            return int(b)+1
        else:
            return int(b)
        
a=list(input())
c=0
print(q(a,0))
