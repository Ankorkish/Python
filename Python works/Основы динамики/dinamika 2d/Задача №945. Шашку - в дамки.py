y,x=map(int,input().split());mas=[];c=0
for k in range(8):
    mas.append([0]*8)
mas[y-1][x-1]=1
for k in range(7,0,-1):
    for k1 in range(8):
        if mas[k][k1]!=0:
            if k1==7:
                mas[k-1][k1-1]+= mas[k][k1]
                continue
            if k1==0:
                mas[k-1][k1+1]+= mas[k][k1]
                continue
            if 0<k<7:
                mas[k-1][k1-1]+= mas[k][k1]
                mas[k-1][k1+1]+= mas[k][k1]
for k in range(8):
    c+=mas[0][k]
print(c)
