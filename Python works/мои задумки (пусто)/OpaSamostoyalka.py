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
    def magaz(self,mon):
        p1=random.randint(1,101)
        p2=[0,0,0,0]
        if 1<=p1<10:
            p3 = [2, 2, 1]
            print("У вас " + str(me.mon) + " монет")
            print("Ви натрапили на ринок!")
            print("Вибір товару :")
            print("2 зілля хп  (ціна за штуку 40 монет)")
            print("2 зілля атаки (ціна за штуку 60 монет)")
            print("1 прокачака шаблі (+20% dmg)(ціна за штуку 300 монет)")
            print("Введіть назву товару, що ви хочете взяти, щоб вийти введіть \"вийти\"")
            while True:
                tov=str(input())
                if tov=="зілля хп":
                    if mon<=40:
                        print("Бракує грошей")
                    elif p3[0]==0:
                        print("ви скупили весь товар цього типу")
                    else:
                        mon-=40
                        print("Ви успішно придбали 1 зілля хп! У вас залишилося "+str(mon))
                        p2[0]+=1
                        p3[0]-=1
                        continue
                elif tov=="зілля атаки":
                    if mon<=60:
                        print("Бракує грошей")
                    elif p3[1]==0:
                        print("ви скупили весь товар цього типу")
                    else:
                        mon -= 60
                        print("Ви успішно придбали 1 зілля атаки! У вас залишилося"+str(mon))
                        p2[1]+=1
                        p3[1]-=1
                        continue
                elif tov=="прокачка шаблі":
                    if mon<=300:
                        print("Бракує грошей")
                    elif p3[2]==0:
                        print("ви скупили весь товар цього типу")
                    else:
                        mon -= 300
                        print("Ви успішно прокачали свою шаблю! У вас залишилося"+str(mon))
                        p2[2]+=1
                        p3[2]-=1
                        continue
                elif tov == "вийти":
                    break
                else:
                    print("Помилка при вводі")
            print("До зустрічі!")
            p2[3]=mon
            return p2
        if 10<=p1<30:
            p3 = [1, 2, 0]
            print("У вас " + str(me.mon) + " монет")
            print("Ви натрапили на дім чарівника!")
            print("Вибір товару :")
            print("1 зілля хп  (ціна за штуку 40 монет)")
            print("2 зілля атаки (ціна за штуку 60 монет)")
            print("Введіть назву товару, що ви хочете взяти, щоб вийти введіть \"вийти\"")
            while True:
                tov=str(input())
                if tov=="зілля хп":
                    if mon<=40:
                        print("Бракує грошей")
                    elif p3[0]==0:
                        print("ви скупили весь товар цього типу")
                    else:
                        mon-=40
                        print("Ви успішно придбали 1 зілля хп! У вас залишилося "+str(mon))
                        p2[0]+=1
                        p3[0]-=1
                        continue
                elif tov=="зілля атаки":
                    if mon<=60:
                        print("Бракує грошей")
                    elif p3[1]==0:
                        print("ви скупили весь товар цього типу")
                    else:
                        mon -= 60
                        print("Ви успішно придбали 1 зілля атаки! У вас залишилося"+str(mon))
                        p2[1]+=1
                        p3[1]-=1
                        continue
                elif tov == "вийти":
                    break
                else:
                    print("Помилка при вводі")
            print("До зустрічі!")
            p2[3]=mon
            return p2
        if 30 <= p1 <= 50:
            p3 = [0, 0, 1]
            print("У вас " + str(me.mon) + " монет")
            print("Ви натрапили на дім коваля!")
            print("Вибір товару :")
            print("1 прокачака шаблі (+20% dmg)(ціна за штуку 200 монет)")
            print("Введіть назву товару, що ви хочете взяти, щоб вийти введіть \"вийти\"")
            while True:
                tov = str(input())
                if tov == "прокачка шаблі":
                    if mon <= 300:
                        print("Бракує грошей")
                    elif p3[2] == 0:
                        print("ви скупили весь товар цього типу")
                    else:
                        mon -= 300
                        print("Ви успішно прокачали свою шаблю! У вас залишилося" + str(mon))
                        p2[2] += 1
                        p3[2] -= 1
                        continue
                elif tov == "вийти":
                    break
                else:
                    print("Помилка при вводі")
            print("До зустрічі!")
            p2[3] = mon
            return p2
        else:
            print("В дрозі ви не знайшли жодного продавця товару")
            return [0,0,0,mon]
class har():
    mame="Андрій"
    maxhp=100
    hp=100
    ot=8
    do=16
    dmg=1
    Vubor=1
    zlhp=2
    zlatk=2
    mon=15
me=har();kk=1;num=1
me.mame=input("Введіть своє ім'я ----->> ")
if me.mame=="adm":
    me.ot=100
    me.do=101
enemy=har()
while True:
    enemy.mame=input("виберіть опонента (чорт, коза, огр, баба-яга) -----> ")
    if enemy.mame=="коза":
        enemy.maxhp=75
        enemy.hp=75
        enemy.ot=5
        enemy.do=12
        break
    elif enemy.mame=="чорт":
        enemy.hp=120
        enemy.maxhp = 180
        enemy.ot=10
        enemy.do=15
        break
    elif enemy.mame=="огр":
        enemy.hp=200
        enemy.maxhp = 200
        enemy.ot=0
        enemy.do=20
        me.zlatk+=1
        break
    elif enemy.mame=="баба-яга":
        enemy.hp=180
        enemy.maxhp = 180
        enemy.ot=8
        enemy.do=12
        me.zlatk+=1
        me.zlhp+=2
        break
    else:
        print("Помилка при вводі, такого опонента не існує! перевірте запис і напишіть правильно!")
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
                    ans2=input("У вас "+str(me.zlatk)+" зілля атаки, збільшити атаку на 150%? (так,ні) ----> ")
                    if ans2 == "так":
                        kk = 2.5
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
            if enemy.maxhp-enemy.hp>120 and enemy.mame=="баба-яга":
                rara=random.randint(1,10)
                print(enemy.mame+" випила зілля і востаноила "+str(rara)+" хп!")
                enemy.hp+=rara
            print("________________________________________________________________________________________________________")
    else:
        if me.hp<=0:
            print("Ви програли")
            sys.exit()
        else:
            print(str(enemy.mame)+" був(-ла) знищенний")
            print( "________________________________________________________________________________________________________")
            enemy.maxhp*=1.3
            int(enemy.maxhp)
            enemy.hp=int(nev*1.5)
            enemy.ot*=1.2
            enemy.do *= 1.2
            enemy.ot=int(enemy.ot)
            enemy.do=int(enemy.do)
            me.zlhp+=int(num//2)
            me.zlatk+=int(num//2)
            print("До складу добавлено "+str(int(num/2))+" зілля хп, та "+str(int(num//2))+" зілля атаки!")
            num+=1
            chek=1
            kkk=me.maxhp
            me.maxhp *= 1.2
            me.maxhp=int(me.maxhp)
            me.hp+=me.maxhp-kkk
            me.mon+=10*num
            print("Тепер ваше максимальне хп досягає " +str(me.maxhp))
            if num%3==0:
                me.ot*=int(2)
                me.do *= int(2)
                print("Ваша атака зроса в двічі!")
            print("Добавлено "+str(10*num)+" монет")
            print(
                "________________________________________________________________________________________________________")
            pokupki=ch.magaz(me.mon)
            me.mon = pokupki[3]
            me.zlhp+=pokupki[0]
            me.zlatk+=pokupki[1]
            if pokupki[2]==1:
                me.ot*=1.2
                me.do*=1.2