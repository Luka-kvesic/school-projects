num1 = int(input("enter a number: "))
num2 = int(input("enter another number: "))
num3 = int(input("enter another number: "))


def blackjack(uno, dos, tres):
    total = 0
    if uno == 11:
        total -= 10
    if dos == 11:
        total -= 10
    if tres == 11:
        total -= 10
    total += uno + dos + tres
    if total >= 21:
        return "BUST"
    else:
        return total
 
response = blackjack(num1,num2,num3)
print(response)