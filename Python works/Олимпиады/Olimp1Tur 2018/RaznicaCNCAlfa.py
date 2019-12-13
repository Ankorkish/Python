a=int(input())
b=int(input())
B=b;A=a
if a%2==0:
    A=a-1
else:
    A=a-2
if b%2==0:
    B=b-1
a1=((A+1)//2)**2
b1=((B+1)//2)**2
c=b1-a1
d=int((((1+b)/2)*b)-((a)/2)*(a-1))
k=d-c
print(k-c)
