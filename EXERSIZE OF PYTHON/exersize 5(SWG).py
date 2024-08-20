import random

print("     Welcome to snake water game")

a = int(input("if you have SNAKE enter 1\nif you have WATER enter 2\n"
"if you have GUN enter 3 \n"))
if (a<1 )or(a>3):
    raise ValueError('INCORRECT ARGUMENT')

elif(a==1) or (a==2) or (a==3):
    if a==1:
        print(f"your choice is 1.SNAKE" )
    elif a==2:
        print(f"your choice is 2.WATER")
    else :
        print(f"your choice is 3.GUN")

    list = [1,2,3]
    r = random.choice(list)

    if r==1:
        print(f"COMPUTER'S choice is 1.SNAKE" )
    elif r==2:
        print(f"COMPUTER'S choice is 2.WATER")
    else :
        print(f"COMPUTER'S choice is 3.GUN")

    if (a==r):
        print("your match is tie")
        print("try one more time")
    elif(a!=r):
        if a==1 and r==2:
            print("congrass you are winner\nSNAKE dirnked WATER")
        elif a==2 and r==3:
            print("congrass you are winner\nWATER damaged GUN")
        elif a==3 and r==1:
            print("congrass you are winner\nGUN killed SNAKE dont worry!")
        elif a==1 and r==3:
            print("GAME OVER\nGUN killed SNAKE")
        elif a==2 and r==1:
            print("GAME OVER\nSNAKE dirnked WATER")
        else :
            print("GAME OVER\nWATER damaged GUN")






















