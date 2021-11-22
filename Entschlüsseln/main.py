menü = int(input("1) Einlesen\n2) Programmende"))
print("Ihre Eingabe", menü)

a = 0
e = 0
p = 0
o = 0
u = 0
ä = 0
ö = 0
ü = 0
leer = 0

datei = open('text.txt', 'r')
text = datei.read()
print(text)

for i in range(1, len(text), 1):
    if text[i] == "a" and text[i] == "A":
        a = a + 1
    elif text[i] == "e" and text[i] == "E":
        e = e + 1
    elif text[i] == "i" and text[i] == "I":
        p = p + 1
    elif text[i] == "o" and text[i] == "O":
        o = o + 1
    elif text[i] == "u" and text[i] == "U":
        u = u + 1
    elif text[i] == "ä" and text[i] == "Ä":
        ä = ä + 1
    elif text[i] == "ö" and text[i] == "Ö":
        ö = ö + 1
    elif text[i] == "ü" and text[i] == "Ü":
        ü = ü + 1
    elif text[i] == " ":
        leer = leer + 1
    elif text[i] == ".":
        leer = leer + 1

print(len(text) - leer)

rechnung = a / len(text) * 100
print(rechnung)
rechnung1 = e / len(text) * 100
print(rechnung1)
rechnung2 = p / len(text) * 100
print(rechnung2)
rechnung3 = o / len(text) * 100
print(rechnung3)
rechnung4 = u / len(text) * 100
print(rechnung4)
rechnung5 = ä / len(text) * 100
print(rechnung5)
rechnung6 = ö / len(text) * 100
print(rechnung6)
rechnung7 = ü / len(text) * 100
print(rechnung7)