b=list(input())
per=peri=0
for k in b[0:3:]:
    per+=int(k)
for k in b[3:7:]:
    peri+=int(k)
if per==peri:
    print("YES")
else:
    print("NO")
