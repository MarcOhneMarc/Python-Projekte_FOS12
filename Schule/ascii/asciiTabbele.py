acsiiwert = 0

for i in range(0, 257, 1):
    acsiiwert = i

    if acsiiwert > 63 and acsiiwert < 128 or acsiiwert > 191 and acsiiwert < 257:
        print("Zahl:", "%-10s" % acsiiwert, "Acsii Wert: ", chr(acsiiwert))