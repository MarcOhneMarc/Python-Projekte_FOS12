import random
random.seed()

nround = bool(1)


def runde():
    zahl = random.randint(1,100)
    ans = int(input())
    vers = 0
    while ans != zahl:
        if ans < zahl:
            print ("Deine Zahl ist zu Klein")
            ans = input()
            vers = vers + 1
        elif ans > zahl:
            print ("Deine Zahl ist zu gros")
            ans = input()
            vers = vers + 1
        elif zahl == ans:
            print ("Deine zahl ist richtig")
            break
    return vers


runde()
