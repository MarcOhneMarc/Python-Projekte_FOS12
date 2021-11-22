# coding=utf-8
import PrettyTable
import random


random.seed()

# PreDefinurung der Variablen für die while schleife
i = 0
srain = 0
templist = []
baddays = 0

# PreDefining der Tabelen
temprain = PrettyTable()
rechnungtab = PrettyTable()
temprain.field_names = ["Tag", "Teamparetaur", "Niederschlag"]
rechnungtab.field_names = ["Rechnungs Ergebnise", "Erg"]

# Initialisirung der While Schleife
while i < 10:

    i = i + 1
    temp = random.randint(0, 21)
    rain = random.randint(0, 11)

    templist.append(temp)
    temprain.add_row([i, temp, rain])

    srain = srain + rain

    if temp < 10 and rain > 5:
        baddays = baddays + 1


# Funktion die, die Mittelwert rechnug durchführen soll und die Rechnungerg Tabele befüllen soll


def rechnung():
    mrain = srain / 10
    rechnungtab.add_row(["Mittlerer Niderschlagswert", mrain])
    rechnungtab.add_row(["Nidrigste Teamperatur", min(templist)])
    rechnungtab.add_row(["Schlecht Wetter Tage", baddays])
    print (rechnungtab)


# Die ausgabe der beiden Tabelen


print (temprain)
rechnung()
