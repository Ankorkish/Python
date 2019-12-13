te=open("INPUT.TXT")
mas=int(te.readline(4))
ma=['G','C','V']
mas=mas%3
for k in range(mas):
    ma.insert(0,ma[2])
    ma.pop(3)
for k in range(3):
    print(ma[k],end="")
