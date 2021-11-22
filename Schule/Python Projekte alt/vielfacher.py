print("Geben sie eine zahl an:")
zahl = input()

rechnung = zahl / 7

if rechnung * 7 == zahl:
    print("Es ist ein ganzes vielfaches")
else:
    print("es ist kein ganzes vielfaches")