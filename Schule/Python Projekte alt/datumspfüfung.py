import random
random.seed()

for i in range(1,11):
    jahr = random.randint(2000, 2020)
    if jahr % 4 == 0 and jahr % 100 != 0 and jahr % 400 != 0:
        print(jahr, "es ist kein schalt jahr ")
else:
    print(jahr, "Es ist ein schalt jahr")
