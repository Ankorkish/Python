import math
a=int(input())
megaKoor=[];pam=[]
for k in range(a):
    x1,y1,x2,y2=map(int,input().split())
    pam.append([x1,y1,x2,y2])
    for k1 in range(len(megaKoor)):
        if x1==megaKoor[k1][0] and y1==megaKoor[k1][1]:
            megaKoor[k1].append([x2,y2])
            break
    else:
        megaKoor.append([x1,y1,[x2,y2]])
    for k1 in range(len(megaKoor)):
        if x2==megaKoor[k1][0] and y2==megaKoor[k1][1]:
            megaKoor[k1].append([x1,y1])
            break
    else:
        megaKoor.append([x2,y2,[x1,y1]])
for k in range(a):
    if pam[k][0]>pam[k][2]:
        per=pam[k][0]
        pam[k][0]=pam[k][2]
        pam[k][2]=per
        per=pam[k][1]
        pam[k][1]=pam[k][3]
        pam[k][3]=per    
perecech=[]
for k in range(a):
    for k1 in range(k+1,a):
        x1_1,y1_1=pam[k][0],pam[k][1]
        x1_2,y1_2=pam[k][2],pam[k][3]
        x2_1,y2_1=pam[k1][0],pam[k1][1]
        x2_2,y2_2=pam[k1][2],pam[k1][3]
        if x1_1==x2_1 and y1_1==y2_1 or\
           x1_1==x2_2 and y1_1==y2_2 or\
           x1_2==x2_1 and y1_2==y2_1 or\
           x1_2==x2_2 and y1_2==y2_2:
            continue
        A1=y1_1-y1_2
        B1=x1_2-x1_1
        C1=x1_1*y1_2-x1_2*y1_1
        A2=y2_1-y2_2
        B2=x2_2-x2_1
        C2=x2_1*y2_2-x2_2*y2_1
        if A2==0:
            A2=0
        if B1*A2-B2*A1!=0:
            y = (C2*A1 - C1*A2) / (B1*A2 - B2*A1)
            if A1==0:
                x=1
            else:
                x=(-C1-B1*y)/A1
            if min(x1_1,x1_2)<=x<=max(x1_1,x1_2)and\
            min(y1_1, y1_2)<=y<=max(y1_1, y1_2):
                perecech.append(x);perecech.append(y)
                perecech.append([x1_1,y1_1])
                perecech.append([x1_2,y1_2])
                perecech.append([x2_1,y2_1])
                perecech.append([x2_2,y2_2])
                sd=perecech.copy()
                megaKoor.append(sd)
                perecech.clear()
        else:
            continue
ura=0
blacklist=[]
for k in range(len(megaKoor)):
    x1=megaKoor[k][0]
    y1=megaKoor[k][1]
    for k1 in range(2,len(megaKoor[k])):
        x11=megaKoor[k][k1][0]
        y11=megaKoor[k][k1][1]
        for k11 in range(len(megaKoor)):
            if megaKoor[k11][0]==x11\
               and megaKoor[k11][1]==y11:
                for k111 in megaKoor[k11][2::]:
                    if k111 in megaKoor[k][2::]:
                        blacklist.append([[x1,y1],[x11,y11],k111])
toctodel=[]
for k in blacklist:
    A=(k[0][0]-k[1][0])**2+(k[0][1]-k[1][1])
    if A<0:
        A*=-1
    A=math.sqrt(A)
    B=(k[0][0]-k[2][0])**2+(k[0][1]-k[2][1])
    if B<0:
        B*=-1
    B=math.sqrt(B)
    C=(k[1][0]-k[2][0])**2+(k[1][1]-k[2][1])
    if C<0:
        C*=-1
    C=math.sqrt(C)
    if A+B==C or A+C==B or C+B==A:
        print(k)
        toctodel.append(blacklist.index(k))
for k in reversed(toctodel):
    blacklist.pop(k)
    '''
for k in blacklist:
    print(k)
    '''
suma=len(blacklist)
for k in blacklist:
    for k2 in range(blacklist.index(k)+1,len(blacklist)):
        for k3 in blacklist[k2]:
            xx1=k3[0];yy1=k3[1]
            if k3 in k:
                ura+=1
        if ura==3:
            suma-=1
            break
        ura=0 
print(suma)        
        

