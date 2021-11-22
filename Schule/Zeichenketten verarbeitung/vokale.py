print("geben sie bitte eine zteichenkette ein")
text = input()

def umwandlung(text):
    text = text.replace("ä", "ae").replace("ö", "oe").replace("ü", "ue").replace("ß", "ss").replace("Ä", "Ae").replace("Ö", "Oe").replace("Ü", "Ue")
    return text

print (umwandlung(text))