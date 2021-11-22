betrag = float(input("Bitte geben sie denn zu schuldeneden betrag ein"))
gezahlt = float(0)
differenz = float(0)

def zahlung(betrag,gezahlt,differenz):

    while betrag > gezahlt:
        differenz = betrag - gezahlt
        if differenz != 0 or differenz > 0:
            gezahlt = gezahlt + float(input("Zahlen sie bitte"))
            differenz = betrag - gezahlt
            print("Sie schulden noch: ", differenz)
            #gezahlt = gezahlt + float(input("Zahlen sie bitte nach"))
        elif differenz == 0:
            print("Vielen Dank für ihren einkauf")
            break

zahlung(betrag, gezahlt, differenz)