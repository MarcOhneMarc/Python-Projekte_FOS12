print("Zahl 1:", end="")
zahl1 = float(input())
print("Zahl 2:", end="")
zahl2 = float(input())

print("geben sie bitte einen operator ein: ", end="")
ope = input()


def rechnung(zahl1, zahl2, ope):

    global ergenbnis
    if ope == "+":
        ergenbnis = zahl1 + zahl2
    elif ope == "-":
        ergenbnis = zahl1 - zahl2
    elif ope == "*":
        ergenbnis = zahl1 * zahl2
    elif ope == "/":
        ergenbnis = zahl1 / zahl2
    elif ope == "%":
        ergenbnis = zahl1 % zahl2

    return ergenbnis


print(rechnung(zahl1, zahl2, ope))