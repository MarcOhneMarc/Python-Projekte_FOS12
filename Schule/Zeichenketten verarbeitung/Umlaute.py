print("Geben sie bitte eine Zeichenkette mit umlauten ein")
name = input()
anzahl = 0
umlaute = "äöüÄÖÜ"

for i in range(0, len(name), 1):
    if name[i] in umlaute:
        anzahl = anzahl + 1
print("Sie haben: ", anzahl, " Umlaute in ihrer zeichenkette")
