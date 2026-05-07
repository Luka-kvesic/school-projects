number1 = int(input("enter a number: "))
number2 = int(input("enter another number: "))

def makesTwenty(uno, dos):
    if (uno + dos == 20) or (uno == 20) or (dos == 20):
        return True
    else:
        return False

answer = makesTwenty(number1, number2)
print(answer)
