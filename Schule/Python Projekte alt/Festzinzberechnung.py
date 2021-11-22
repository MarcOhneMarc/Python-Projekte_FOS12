print("Geben Sie bitte Ihren Betrag ein:")

money = int(input())

if money < 1000:
    zinssatz = float(1.8)
elif money <= 5000:
    zinssatz = float(2.0)
elif money <= 10000:
    zinssatz = float(2.2)
else:
    zinssatz = float(2.4)

print("Jahr", "Anfang", " Zinsen", "  Ende")

for i in range(1,6,1):
    zins = money/100*zinssatz
    ende = money+zins
    print("%1d" % (i), "%10.2f" % (money), "%2.2f" % (zins), "%10.2f" % (ende))
    money = money + zins


# Aufgabe 2
import random
random.seed()



print ("Dies ist ein Wurfelspiel. Drucke Enter um es zu spielen!")
input()

player1 = 0
player2 = 0

for i in range(1,11,1):
    wurfel1 = random.randint(1,6)
    player1 = player1+wurfel1
    print("Spieler 1:", wurfel1)
    wurfel2 = random.randint(1,6)
    player2 = player2+wurfel2
    print("Spieler 2:", wurfel2)

print("Ergebnis Spieler 1:", player1)
print("Ergebnis Spieler 2:", player2)

if player1 > player2:
    print("Spieler 1 hat gewonnen")
else:
    print("Spieler 2 hat gewonnen")