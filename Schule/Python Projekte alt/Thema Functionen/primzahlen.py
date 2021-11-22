zahl1 = int(input())
zahl2 = int(input())
print = ("Zahl 1:", zahl1, "Zahl 2:", zahl2)

def zahlentausch(zahl1, zahl2):
    zahl1 = zahl2
    zahl2 =zahl1
    return zahl1,zahl2


zahlentausch()
zahl1, zahl2 = zahlentausch(zahl1, zahl2)
print = ("Zahl 1:", zahl1, "Zahl 2:", zahl2)
