temperatur = [27.9, 30.1, 89.2]

print("geben sie bitte die prozent zahl an")
prozent_erhöhung = float(input())


def zehnprozent(temperatur, prozent_erhöhung):
    for i in range(0, len(temperatur), 1):
        temperatur[i] = temperatur[i] * prozent_erhöhung
    return temperatur


zehnprozent(temperatur, prozent_erhöhung)
temperatur = zehnprozent(temperatur,prozent_erhöhung)
print(temperatur)

def temparaturerte():
    for temp in temperatur:
        temp1 = (temp)
    
    print(".")
    
    for i in range (0, len(temperatur), 1):
        temp2 = temperatur[i]
        if (i == 0):
            temperatur[0] = 0.0
    
    print()
    
    for i  in range(0, len(temperatur), 1):
        temp3 = temperatur[i]

    return temp1, temp2, temp3

