a,b,c,d,e,f=map(int,input().split())
em=[a,b,c]
em.sort()
ce=[d,e,f]
ce.sort()
mon=0
for k in range(3):
    mon+=em[k]*ce[k]
print(mon)
    
