idiale_temperatur = 28
minimal = 22
maximal = 32
heizung_an = False

aktuelle_themperatur = int(input("Geben sie ihre idiale Temperatur an: "))

if aktuelle_themperatur == idiale_temperatur:
    print("wohlfühl themperatur!")
    print("So kann es bleiben.")

else:
    print("Temperatur ist nicht idial Nahcregung wird gestartet")
    if aktuelle_themperatur < minimal or aktuelle_themperatur > maximal:
        print("es ist zu kalt")
        heizung_an = True
        print(heizung_an)

   # elif aktuelle_themperatur > maximal:
    #    print("es ist zu warm")
