import math
class per1():
    def obSh(self,r):
        print("Об'єм шару")
        print(4/3*3.14*r**3)
    def plTr(self,s1,s2,s3):
        poly=(s1+s2+s3)/2
        print("полща трикутника")
        print(math.sqrt(poly*(poly-s1)*(poly-s2)*(poly-s3)))
metods=per1()
rad=int(input("Введіть радіус шару ----> "))
st1,st2,st3=map(int,input("Введіть 3 сторони трикутника у 1 рядок ----> " ).split())
metods.obSh(rad)
metods.plTr(st1,st2,st3)