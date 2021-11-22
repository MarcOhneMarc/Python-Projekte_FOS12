import random
random.seed()

print ("######################### Schleife 1 ###########################")
for i in range(0,26,5):
    print (i)

print ("######################### Schleife 2 ###########################")
for i in range(1,9,1):
    print (i*i)

print ("######################### Schleife 3 ###########################")
for i in range(10,1,-2):
    print (i)

print ("######################### Tankstellen Berechner ###########################")


n = float(1.50)
s = float(1.80)
d = float(1.40)

print ("Geben sie die getankte maenge in Liter an")
getankt = float(input())
print ("Geben sie das getankte gut an")
gut = input()

if gut == n:
    print (1.50*getankt)
elif gut == s:
    print (1.80*getankt)
elif gut == d:
   print (1.40*getankt)
else:
    print ("Geben sie ein exestirendes gut an")

print ("######################### Aufgabe 3 Wurfel spiel ###########################")

count1 = 0
count2 = 0
player1 = 0
player2 = 0
b = 0

for i in range(1,11,1):
    if i % 2 != 0:
        b = random.randint(1,6)
        player1 = b
        print("Player 1:", player1)
        count1 += b
    else:
        b = random.randint(1,6)
        player2 = b
        print("Player 2:", player2)
        count2 += b


if count2 < count1:
    print("Player 1 has", count1, "Points and win the game!")
else:
    print("Player 2 has", count2, "Points and win the game!")

print("Player 1 has", count1, "Points")
print("Player 2 has", count2, "Points")
