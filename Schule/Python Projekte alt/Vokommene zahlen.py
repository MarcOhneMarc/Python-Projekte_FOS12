zahl = int(input("Geben sie bitte die Zahl an"))
zahlen_liste = []

for i in range(0, zahl, 1):
    if zahl % i == 0:
        zahlen_liste.append(i)

print(zahl)
print(zahlen_liste)