a=int(input())
b=list(str(a))
per=0
if len(b)!=4:
    per=4-len(b) 
for k in range(per):
    b.insert(0,0)
c=str()
for k in b:
    c+=str(k)
if ((a%4 == 0 and a%100 != 0) or (a%400 == 0)):
  print("12/09/"+c)
else:
  print("13/09/"+c)
