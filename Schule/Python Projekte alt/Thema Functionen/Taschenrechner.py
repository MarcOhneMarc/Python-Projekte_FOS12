print("Willkommen, Gebe bitte an mit welchen Operator du rechnen willst (+,-,*,/)")
op = input()

print ("geben sie bitte beide zahlen an")
numb1 = int(input())
numb2 = int(input())


class main:

     def adition():
        ans = numb1 + numb2
        return ans
        
    def subtration():
        ans = numb1 - numb2
        return ans

    def multiplytion():
        ans = numb1 * numb2
        return ans
        
    def devisition():
        ans = numb1 / numb2
        return ans 

   
    if op == "+":
        ans = adition()
        print(ans)
    elif op == "-":
        ans = subtration()
        print(ans)
    elif op == "*":
        ans = multiplytion()
        print(ans)
    elif op == "/":
        ans = devisition()
        print(ans)

