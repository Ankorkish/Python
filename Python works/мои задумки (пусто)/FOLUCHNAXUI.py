import random
class har():
    hp=100
    atk=random.randint()
    position=4
    name="Andriy"
class bitva():
    def attacEnemy(self,me,enemy):
        me.position=int(input())
        enemy.position=random.randint()
        if me.position==enemy.position:
            n=3
        else:
            n=0,5
        me.atk=random.randint(5,10)*n
        enemy.hp-=me.atk
    def SprobaYvernytsa(self,p1hp,p2hp,p2pos):
diya=bitva();me=har();enemy=har();enemy.name="Чорт"
while me.hp!=0 and enemy.hp!=0:
    diya.attacEnemy(me,enemy)
