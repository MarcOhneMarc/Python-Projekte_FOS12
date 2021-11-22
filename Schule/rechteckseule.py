print(''.join(reversed('Hallo!')))

name = input("geben sie bitte einen namen an")
rname = "".join(reversed(name))

if name == rname:
    print("name ist ein hoan")
else:
    print("Kein huan")