import random
import sys
class chans():
    def prov(self,p1):
        perem = random.randint(1, 100)
        while True:
            if p1=="голова":
                if perem<=25:
                    print("Удар шаблею влучив у голову!")
                    return 3
                else:
                    print("Шабля пролетіла мимо!")
                    return 0.5
            if p1=="тулуб":
                if perem<=90:
                    print("в нього не було шансів, шабля влучила у тіло")
                    return 1
                else:
                    print("Відхилившись назад, опонент залишився з маленькою царапинкою")
                    return 0.3
            if p1=="ноги":
                if perem<=50:
                    print("Ноги опонента підкосилися")
                    return 1.2
                else:
                    print("Ви лиш трохи зачипили опонента")
                    return 0.5
            else:
                p1=input("Ви помилились при вводі, введіть ще раз ----> ")
class har():
    mame="Андрій"
    maxhp=100
    hp=100
    ot=8
    do=16
    dmg="none"
    Vubor="None"
    zlhp=2
    zlatk=2
me=har();kk=1;num=1
me.mame=input("Введіть своє ім'я ----->> ")
if me.mame=="adm":
    me.ot=100
    me.do=101
enemy=har()
enemy.mame=input("виберіть опонента (чорт, коза, огр) -----> ")
if enemy.mame=="коза":
    enemy.hp=75
    enemy.ot=3
    enemy.do=12
elif enemy.mame=="чорт":
    enemy.hp=120
    enemy.ot=10
    enemy.do=12
elif enemy.mame=="огр":
    enemy.hp=200
    enemy.ot=0
    enemy.do=31
    me.zlatk+=1
ch=chans()
chek=1
print("Гра почалась!")
while True:
    nev=enemy.hp
    print("________________________________________________________________________________________________________")
    print("                           ви атакуєте опонента під номером   "+str(num))
    print("________________________________________________________________________________________________________")
    while me.hp>0 and enemy.hp>0:
        if chek==1:
            print("У вас "+str(me.hp)+" хп! У "+enemy.mame+" "+str(enemy.hp)+" хп")
            if me.zlatk<0:
                me.zlatk=0
            if me.zlhp<0:
                me.zlhp=0
            if me.zlhp+me.zlatk>0:
                ans=input("У вас є "+str(me.zlhp)+" зілля хп, "+str(me.zlatk)+" зілля атаки, чи хочете ви їх використати?    (так, ні) ----> ")
            if ans=="так":
                if me.zlhp!=0:
                    ans2=input("У вас "+str(me.zlhp)+" зілля хп, відрегенувати від 30 до 40 хп? максимум ваших хп "+str(me.maxhp)+"!  (так,ні) ----> ")
                    if ans2=="так":
                        pp=random.randint(30,40)
                        oh=me.hp
                        me.hp += pp
                        if me.hp>me.maxhp:
                            me.hp=me.maxhp
                            pp=me.maxhp-oh
                        print("Ви збільшили значення свого здоров'я на "+str(pp)+" хп!")
                        me.zlhp-=1
                if me.zlatk!=0:
                    ans2=input("У вас "+str(me.zlatk)+" зілля атаки, збільшити атаку на 50%? (так,ні) ----> ")
                    if ans2 == "так":
                        kk = 1.5
                        me.zlatk-=1
            me.dmg=random.randint(me.ot,me.do)
            me.Vubor=str(input("Куди атакувати "+str(enemy.mame)+"-a?     (голова, тулуб, ноги) -----> "))
            n=ch.prov(me.Vubor)
            enemy.hp-=int(me.dmg*n*kk)
            if me.dmg==me.do:
                print("Гравець "+me.mame+" атакує зі всієї сили!")
            print(me.mame+" атакує "+enemy.mame+" на "+str(int(me.dmg*n*kk))+" урону!")
            kk = 1
            chek=0
        elif chek == 0:
            enemy.dmg = random.randint(enemy.ot, enemy.do)
            me.hp -= enemy.dmg
            if me.dmg == 12:
                print("Оппонент "+enemy.mame+" не знає втоми!")
            print(enemy.mame + " атакує " + me.mame + " на " + str(enemy.dmg) + " урону!")
            chek = 1
            print("________________________________________________________________________________________________________")
    else:
        if me.hp<=0:
            print("Ви програли")
            sys.exit()
        else:
            print(str(enemy.mame)+" був(-ла) знищенний")
            enemy.hp=int(nev*1.5)
            me.zlhp+=int(1*num)
            me.zlatk+=int(1*num)
            print("До складу добавлено "+str(int(1*num))+" зілля хп, та "+str(int(1*num))+" зілля атаки!")
            num+=1
            chek=1
            me.maxhp *= 1.2
            me.maxhp=int(me.maxhp)
            print("Тепер ваше максимальне хп досягає " +str(me.maxhp))
            if num%3==0:
                me.ot*=int(2)
                me.do *= int(2)
                print("Ваша атака зроса в двічі!")


