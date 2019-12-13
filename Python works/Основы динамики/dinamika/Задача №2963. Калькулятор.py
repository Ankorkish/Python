a=int(input())
c=0
while a!=1:
    if a%3==0:
        a//=3
        c+=1
        continue
    if a%2==0:
        a//=2
        c+=1
        continue
    a-=1
    c+=1
print(c)

    
