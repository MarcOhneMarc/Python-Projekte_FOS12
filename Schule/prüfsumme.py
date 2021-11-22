print("Geben Sie eine Zahl ein:")
eingabe = input()


def calc_checksum(eingabe):
    summe = 0
    for i in range(1,len(eingabe),1):
        zwischensumme = int(eingabe[i])*i
        print(summe)
        summe += zwischensumme
    ergebnis = summe % 10
    print(ergebnis)


calc_checksum(eingabe)