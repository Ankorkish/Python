def q(a):
    if a<10:
        return a
    else:
        return max(a%10,q(a//10))    
a=int(input())
print(q(a))

