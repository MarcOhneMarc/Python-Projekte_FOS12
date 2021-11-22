import random
random.seed()

a = random.randint(1,10)
b = random.randint(1,10)
c = a + b

for i in range(1,10):
    print("Geben sie bitte das ergebnis von:", a,"+",b," ein")
    inp = int(input())
    if c == inp:
        print("Sie haben es geschaft")
        break