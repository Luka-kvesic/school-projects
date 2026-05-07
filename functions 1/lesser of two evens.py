number1 = int(input("enter one number: "))
number2 = int(input("enter another number: "))

def lesserOfTwoEvens(uno, dos):
    if (uno%2==0) and (dos%2==0):
        if uno > dos:
            return dos
        elif dos > uno:
            return uno
    else:
        if uno > dos:
            return uno
        elif dos > uno:
            return dos


num = lesserOfTwoEvens(number1, number2)
print(num)
