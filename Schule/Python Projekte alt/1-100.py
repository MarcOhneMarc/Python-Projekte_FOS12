import random
random.seed()

zahl = random.randint(1,100)

if zahl < 20:
    print("Die zahl ist kleiner als 20")
elif zahl < 40:
    print("Zufallszahl zwishen 20 und 39")
elif zahl < 60:
    print("Zufallszahl zwischen 40 und 59")
elif zahl < 80:
    print("Zufallszahl zwischen 60 und 79")
elif zahl < 100:
    print("Zufllszahl zwischen 80 und 100")

print(zahl)