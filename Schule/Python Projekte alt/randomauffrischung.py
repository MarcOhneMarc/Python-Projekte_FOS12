import random
random.seed()

print ("#################### Aufgabe 1 #####################")
i = 1

def loop(i):
    while i < 101:
        rnumb = random.randint(60, 80)
        rnumb = rnumb + rnumb
        print ("%.2f" % rnumb)
        i = i + 1
loop(i)
