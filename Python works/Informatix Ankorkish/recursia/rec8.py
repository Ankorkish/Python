def schet(mas,k):
    p=0
    for k1 in range(2,len(mas),2):
        if k==mas[k1]:
            p+=schet(mas,mas[k1-1])
    return  p+1
mas=["start"]
for k in range(int(input())):
    a,m=map(int,input().split())
    mas.append(a)
    mas.append(m)
k=int(input())
print(schet(mas,k))
