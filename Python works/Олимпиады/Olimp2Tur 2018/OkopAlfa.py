a=int(input())
megaKoor=[]
for k in range(a):
    x1,y1,x2,y2=map(int,input().split())
    for k1 in range(len(megaKoor)):
        if x1==megaKoor[k1][0] and y1==megaKoor[k1][1]:
            megaKoor[k1].append([x2,y2])
            break
    else:
        megaKoor.append([x1,y1,[x2,y2]])
print(megaKoor)
    
