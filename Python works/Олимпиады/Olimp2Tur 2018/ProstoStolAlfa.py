m,n=map(int,input().split())
kv=[];MaxkolGost=0;CHECK=0
for k in range(m):
    kv.append(list(input()))
for k in range(m):
    for k1 in range(n):
        gl=0;sh=0;maxgl=0
        y=k;x=k1
        while x<=n-1 and kv[y][x]!="X":
            sh+=1
            while y!=m and kv[y][x]!="X":
                gl+=1
                y+=1
                if sh==1:
                    maxgl=gl
            if gl>maxgl:
                gl=maxgl
            elif gl<maxgl:
                maxgl=gl
            result=(gl+sh)*2
            if MaxkolGost<result:
                MaxkolGost=result
            x+=1;gl=0;y=k
print(MaxkolGost-1)        
        
    
