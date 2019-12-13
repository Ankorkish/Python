te=open("INPUT.TXT")
mas=list((line.strip().split() for line in te))
mas=mas[0]
a=int(mas[0]);b=int(mas[1]);c=int(mas[2])
if a+b<=c or a+c<=b or b+c<=a:
    print("NO")
else:
    print("YES")
