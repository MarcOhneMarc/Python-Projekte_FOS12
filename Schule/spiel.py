import random
random.seed()


def spiel():
    lvl = 1
    laufzeit = True
    antw = False

    while laufzeit == True:
        menu = input("Menu:\n(N)eues Spiel\n(L)evel festlegen\n(B)eenden")
        print("Deine wahl: ", menu)
        tryes = 0

        if menü == "n":
            if lvl == 1:
                randzahl = random.randint(1, 10)
            elif lvl == 2:
                randzahl = random.randint(1, 20)
            while antw == False:
                eingabe = int(input("Dein versuch(0 um aufzugeben):"))
                if eingabe == randzahl:
                    print("GLückwunsch")
                    print("Versuche: ", tryes)
                    break
                elif eingabe > randzahl:
                    print("Deine Zahl ist größer")
                elif eingabe < randzahl:
                    print("Deine Zahl ist kleiner")
                elif eingabe > 0:
                    break

                tryes = tryes + 1
        if menü == "l":
            print("Deine wahl: ", menü)
            lvl = int(input("Geben sie bitte die LVL Zahl ein:"))
            print(lvl)
        if menü == "b":
            break

spiel()
