import math

def prim(n):
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    else:
        for i in range(2,int(math.sqrt(n))+1):
            if n % i == 0:
                return False
    return True

wert = int(input("Maximalwert eingeben: "))

for i in range(2,wert+1):
    if prim(i) == True:
        print(i)