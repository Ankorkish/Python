te=open("INPUT.TXT")
p=list(pol.strip().split() for pol in te)
p=p[0]
a=int(p[0]);b=int(p[1]);c=int(p[2]);t=int(p[3])
if a<t:
    print(a*b+(t-a)*c)  
else:
    print(t*b)
    
