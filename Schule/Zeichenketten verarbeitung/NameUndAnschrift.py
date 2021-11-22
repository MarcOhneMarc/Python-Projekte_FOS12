print("Vorname;Nachname;Straße;PLZ;Ort")
name = input()
vorname = ""
nachname = ""
strase = ""
plz = ""
ort = ""
token = 1

for i in range(0, len(name), 1):
    if name[i] != ";" and token == 1:
        vorname = vorname + name[i]
    elif name[i] != ";" and token == 2:
        nachname = nachname + name[i]
    elif name[i] != ";" and token == 3:
        strase = strase + name[i]
    elif name[i] != ";" and token == 4:
        plz = plz + name[i]
    elif name[i] != ";" and token == 5:
        ort = ort + name[i]
    elif name[i] == ";":
        token = token + 1

print("\n", "Vorname: ", vorname, "\n", "Nachname: ", nachname, "\n", "Straße", strase, "\n", "Plz: ", plz, "\n", "Ort", ort)
