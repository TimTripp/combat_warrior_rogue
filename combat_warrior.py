#Author: Tim Tripp
#Date: 4/8/2016
#Name: Combat_Warrior
#Date Modified: 1/11/2016
#Imports
import time
import random
#Globals

## startmoney is the amount of in game currency the user starts the game with.
startmoney = 1000000
## gencash is a list which appends the generals cash which can be won by the user in battle
gencash = []
## the appended amount is the cash the user wins the first time he defeats the enemy general
gencash.append(100000)
## money is a list which contains the total amount of in game currency the user wins and losses,
## sum(money) shows current cash value throughout the game...
money = []
## the appended amount is the money the user starts the game with
money.append(startmoney)
## un is a list which stores the username entered by the user
un = []
## ts is the might strength of the TROOPER
ts = 10
## tc is the cost of 1 TROOPER
tc = 15
## hs is the might strength of the HUMVEE
hs = 50
## hc is the cost of 1 HUMVEE
hc = 75
## ks is the might strength of the TANK
ks = 250
## kc is the cost of 1 TANK
kc = 250
## might is a list which stores the combined power of the troops(troopers,humvees,tanks)
might = []
## trps is a list which keeps track of the number of TROOPER the user has
trps = []
## humvs is a list which contains the total number of HUMVEE the user has
humvs = []
## tanks is a list which contains the total number of TANK the user has
tanks = []
## keeps track of money loaned by the bank... money that is placed as the pay off debt value
debts = []
## keeps track of wins
wins = []
## keeps track of losses
losses = []
## keeps track of lost TROOPER
tpslost = []
## keeps track of lost HUMVEE
humvlost = []
## keeps track of lost TANK
tanklost = []
## loan is appended to debt when user purchases more troops than he/she/it has money for
loans = []
## keeps track of lost power
powlost = []
## gent is a list which contains the total number of EG's TROOPER
gent = []
## appended amount is the start number of TROOPER for lv1 EG
gent.append(1000)
## genh is a list which contains the total number of EG's HUMVEE
genh = []
## appended amount is the start number of HUMVEE for lv1 EG
genh.append(750)
## genk is a list which contains the total number of EG's TANK
genk = []
## appended amount is the start number of TANK for lv1 EG
genk.append(500)
## keeps track of number of times user fights enemy general
fightgen = []
## keeps track of number of times user losses to the EG
genlosses = []
## keeps track of number of times user wins to the EG
genwins = []
## intro shows game objectives for the user
def intro():
    cont = "e"
    while cont != "a":
        print("INTRO")
        print("[][][][][][][][][][][][][][][][][][][][][]")
        print("*********WELCOME_TO_COMBAT_WARRIOR********")
        print("------------------------------------------")
        time.sleep(3)
        print("GAME OBJECTIVES:")
        print("1)BUILD ARMY")
        print("2)DESTROY ENEMY")
        print("3)ELIMINATE THE ENEMY GENERAL")
        print("")
        time.sleep(2)
        cont = input("Press (a) to continue: ")
        if cont == "a":
            print("")
            game()
        else:
            print("value is not valid...")
            continue
## game gives the user instructions and gains username
def game():
    
    cont = "e"
    while cont != "a":
        
        print("----GAME CONTINUED---")
        print("")
        print("Welcome to your base...")
        print("You have a total of $",startmoney,"which can be used to build your army")
        print("To gain more money you must win battles")
        print("If you run out of money during the game, \nyou can take a loan from the bank")
        print("")
        unn = input("Enter your player name: ")
        un.append(unn)
        print("")
        cont = input("Press (a) to continue: ")
        if cont == "a":
            print("")
            basemenu()
        else:
            print("value is not valid...")
            continue
## basemenu is the home page for the game with the options to(train,attack,overview,pay debt, fight EG, and quit)
def basemenu():
    cont = 0
    while cont != 5:
        time.sleep(2)
        print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
        print("<<<<<<<<<<<BASE MENU>>>>>>>>>")
        print("1) TRAIN TROOPS")
        print("2) ATTACK ENEMY BASE")
        print("3) SEE OVERVIEW OF MILITARY POWER")
        print("4) Pay OFF DEBT")
        print("5) QUIT GAME")
        print("6) ATTACK ENEMY GENERAL")
        command = int(input("Enter your command (1),(2),(3),(4),(5), or (6): "))
        if command == 1:
            train_troops()
        elif command == 2:
            attack()
        elif command == 3:
            overview()
        elif command == 4:
            payoff()
        elif command == 5:
            break
        elif command == 6:
            enemygeneral()
        else:
            print("value not valid...")
            print("YOU MUST FIGHT ENEMY GENERAL BEFORE YOU LEAVE")
            continue
## allows user to fight general
def enemygeneral():
    while True:
        print("")
        print("============================")
        print("^^^^^^ENEMY GENERAL^^^^^^^^^")
        print("----------------------------")
        time.sleep(2)
        print(un[0],"'s TROOPS")
        print("TROOPERS:",sum(trps),",HUMVEES:",sum(humvs),",TANKS:",sum(tanks))
        print("----------------------------")
        print("ENEMY GENERALS TROOPS")
        print("TROOPERS:",sum(gent),",HUMVEES:",sum(genh),",TANKS:",sum(genk))
        print("GENERALS CASH",sum(gencash))
        comm = int(input("Enter (1) to attack or (2) to return to base: "))
        if comm == 1:
            time.sleep(2)
            attackgen()
            #basemenu()
        elif comm == 2:
            print("")
            print("welcome back to base",un[0])
            print("")
            break
        else:
            print("value not valid...")
## determines who wins (user or EG)
def attackgen():
    fightgen.append(1)
    a = sum(gent)
    b = sum(genh)
    c = sum(genk)
    d = sum(gencash)
    crz = (sum(trps) - a) + (sum(humvs) - b) + (sum(tanks) - c)
    trps.append(-a)
    humvs.append(-b)
    tanks.append(-c)
    print("FIGHTING!...")
    time.sleep(1)
    print("OUCH...")
    time.sleep(3)
    if crz <= 0:
        print("YOU LOST, THE ENEMY GENERAL HAS DEFEATED YOU...")
        losses.append(1)
        genlosses.append(1)
    if crz > 0:
        print("CONGRATULATIONS!!! YOU HAVE DEFEATED THE ENEMY GENERAL...")
        gent.append(1000)
        genh.append(750)
        genk.append(500)
        gencash.append(100000)
        wins.append(1)
        genwins.append(1)
        money.append(d)
    st = sum(trps)
    sh = sum(humvs)
    sk = sum(tanks)
    if st <= 0:
        print("YOU HAVE LOST ALL YOUR TROOPERS IN BATTLE")
        a = 0
        while st <= 0:
            st = st + 1
            a = a + 1
        print(a)
        trps.append(a-1)
        might.append(a*ts)
    if sh <= 0:
        print("YOU HAVE LOST ALL YOUR HUMVEES IN BATTLE")
        a = 0
        while sh <= 0:
            a = a + 1
            sh = sh + 1
        humvs.append(a-1)
        might.append(a*hs)
    if sk <= 0:
        print("YOU HAVE LOST ALL YOUR TANKS IN BATTLE")
        a = 0
        while sk <= 0:
            a = a + 1
            sk = sk + 1
        tanks.append(a-1)
        might.append(a*ks)
    print("done here")
## shows overview of users power, troops, and money
def overview():
    cont = 0
    while cont != 1:
        time.sleep(2)
        print("")
        print("MILITARY OVERVIEW")
        print("# of TROOPERS:",sum(trps))
        print("# of HUMVEES:",sum(humvs))
        print("# of TANKS:",sum(tanks))
        print("# overall POW:",sum(might))
        print("# total cash on hand:",sum(money))
        
        back = int(input("To go back to BASE MENU enter (1): "))
        if back == 1:
            break
        else:
            print("value not valid...")
## allows user to payoff debt
def payoff():
    cont = 0
    while cont != 1:
        a = sum(debts) * -1
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        print("PAY OFF DEBT")
        print("CURRENT CASH:",sum(money))
        print("CUREENT DEBT:$",a)
        pay = int(input("Enter amount to pay debt: "))
        debts.append(pay * -1)
        money.append(pay)
        ask = int(input("Enter (1) to return to BASE MENU: "))
        if ask == 1:
            break
        else:
            print("value not valid...")
## allows user to fight basic enemy
def attack():
    cont = 0
    while cont != 4:
        a = random.randint(1,15)
        b = random.randint(1,5)
        c = random.randint(0,2)
        enemycash = random.randint(100,10000)
        enemytroopers = a
        enemyhumvee = b
        enemytank = c
        time.sleep(1)
        print("")
        print("ARE YOU READY TO FIGHT?!!")
        print("")
        time.sleep(3)
        print(un[0],"'s TROOPS")
        print("TROOPERS:",sum(trps),",HUMVEES:",sum(humvs),",TANKS:",sum(tanks))
        print("ENEMY'S TROOPS")
        print("ENEMY TROOPERS-",a,"ENEMY HUMVEE-",b,"ENEMY TANK-",c)
        print("ENEMY MONEY = $",enemycash)
        attack = int(input("ENTER (1) TO ATTACK, or (4) to return to base: "))
        if attack == 1:
            combat(a,b,c,enemycash)
        elif attack == 4:
            break
        else:
            print("value not valid...")
## determines who wins basic fight
def combat(a,b,c,d):
    time.sleep(1)
    print("FIGHTING BATTLE!!!")
    time.sleep(5)
    print("************BATTLE RESULTS************")
    tpslost.append(a)
    humvlost.append(b)
    tanklost.append(c)
    ra = sum(trps) - a
    rb = sum(humvs) - b
    rc = sum(tanks) - c
    mightlost = (a*ts) + (b*hs) + (c*ks)
    might.append(-mightlost)
    crz = ra + rb + rc
    trps.append(-a)
    humvs.append(-b)
    tanks.append(-c)
    powlost.append(mightlost)
    if crz < 1:
        print("YOU LOST THE BATTLE!")
        print("RETURN TO BASE AND TRAIN MORE TROOPS")
        losses.append(1)
    if crz >= 1:
        print("YOU WON!, keep fighting...")
        print("CASH WON:",d)
        wins.append(1)
        money.append(d)
    st = sum(trps)
    sh = sum(humvs)
    sk = sum(tanks)
    if st <= 0:
        print("YOU HAVE LOST ALL YOUR TROOPERS IN BATTLE")
        a = 0
        while st < 0:
            st = st + 1
            a = a + 1
        print(a)
        trps.append(a)
        might.append(a*ts)
    if sh <= 0:
        print("YOU HAVE LOST ALL YOUR HUMVEES IN BATTLE")
        a = 0
        while sh < 0:
            a = a + 1
            sh = sh + 1
        humvs.append(a)
        might.append(a*hs)
    if sk <= 0:
        print("YOU HAVE LOST ALL YOUR TANKS IN BATTLE")
        a = 0
        while sk < 0:
            a = a + 1
            sk = sk + 1
        tanks.append(a)
        might.append(a*ks)

## allows user to train troops
def train_troops():
    print("|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|")
    print("Troop Menu")
    print("CASH AVAILABLE:",sum(money))
    print("1) Troopers ___",sum(trps),"_ pow =",ts,"____ cost = $",tc)
    print("2) Humvee _",sum(humvs),"_ pow =",hs,"____ cost = $",hc)
    print("3) Tank __",sum(tanks),"__ pow =",ks,"____ cost = $",kc)
    tpr = int(input("Enter # of troopers: "))
    huv = int(input("Enter # of humvees: "))
    tnk = int(input("Enter # of tanks: "))
    addingtroops(tpr,huv,tnk)


## adds troops along with thier power to the users army, loans are also given if money is too little


def addingtroops(a,b,c):
    might.append(ts * a)
    trps.append(a)
    might.append(hs * b)
    humvs.append(b)
    might.append(ks * c)
    tanks.append(c)
    totalcost = (a * tc)+(b * hc) + (c * kc)
    money.append(totalcost * -1)
    if sum(money) < 0:
        time.sleep(2)
        print("You don't have enough money for all the troops you selected")
        print("A loan has been taken out to cover the cost")
        debt = sum(money)
        dollar = -(debt)
        loan = dollar
        debts.append(loan)
        loans.append(loan)
        print("Total cost of loan is $",loan)
    
## displays final stats of the game
def finalstatsheet():
    fought = sum(wins) + sum(losses)
    if fought > 0:
        percentage = (sum(wins)/fought) * 100
        genfought = sum(fightgen)
        genp = (sum(genwins)/genfought) * 100
        print("")
        print("/\/\/\/\/\/\FINAL_STATS/\/\/\/\/\/\/\/")
        print("*",un[0],"'s final stats")
        print("* Military POWER:",sum(might))
        print("* Military POWER Lost:",sum(powlost))
        print("* Money:",sum(money))
        print("* Money Loaned:",sum(loans))
        print("* Current Debt:",sum(debts))
        print("* Troopers:",sum(trps))
        print("* Humvees:",sum(humvs))
        print("* Tanks:",sum(tanks))
        print("* ENEMY TROOPERS DESTROYED:",sum(tpslost))
        print("* ENEMY HUMVEES DESTROYED:",sum(humvlost))
        print("* ENEMY TANKS DESTROYED:",sum(tanklost))
        print(",<>,")
        print("* BATTLES FOUGHT:",fought)
        print("* BATTLES WON:",sum(wins))
        print("* BATTLES LOST:",sum(losses))
        print("* WIN PERCENTAGE:.",percentage,"%")
        print("* BATTLES VS ENEMY GENERAL:",sum(fightgen))
        print("* BATTLES WON VS ENEMY GENERAL:",sum(genwins))
        print("* BATTLES LOST VS ENEMY GENERAL:",sum(genlosses))
        print("* WIN PERCENTAGE VS ENEMY GENERAL:",genp,"%")
        time.sleep(20)

## starting point of the game
def main():
    intro()
    finalstatsheet()
          
main()
