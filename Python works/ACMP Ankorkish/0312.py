a,b,c=map(int,input().split())
mas=[];mas.append(a);mas.append(b)
per=b-a
for k in range(2,c):
    mas.append(mas[k-1]+per)
print(mas)