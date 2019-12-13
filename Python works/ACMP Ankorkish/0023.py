te=open("INPUT.TXT")
m=int(te.read(4))
c=0
for k in range(1,m+1):
    if m%k==0:
        c+=k
print(c)
