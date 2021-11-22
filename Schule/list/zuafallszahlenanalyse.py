import random
import statistics
random.seed()

min = 0
max = 1000
anz = 100

def gen_Zufallszahlen(min,max,anz):
    listzufall = []
    for i in range(0, anz, 1):
        zufall = random.randint(min, max)
        listzufall.append(zufall)
    return listzufall

def mittelwertzufall(zufalllist):
    mean = statistics.mean(zufalllist)
    return mean

    """
def analyseZufallszahlen():
    mittelwert = 0
    min = 1000
    max = 1
    for i in range(1, 101, 1):
        zahl = random.randint(1, 1000)
        print("%5d" % (zahl), end="")

        if (i % 18 == 0):
            print()

        mittelwert = mittelwert + zahl
        if zahl < min:
            min = zahl
        if zahl > max:
            max = zahl

    mittelwert = mittelwert / 108
    return min, max
    """
# main
#min, max = analyseZufallszahlen()
zufalllist = gen_Zufallszahlen(min,max,anz)
mittelwert = mittelwertzufall(zufalllist)

print(zufalllist)
print(mittelwert)
print(min(zufalllist))
