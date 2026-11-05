


def oddify(number):
    
    if number < 0:
        return 0
    else:
        if number%2 == 1:
            return number + oddify(number-1)
        else:
            return 0 + oddify(number-1)





number = int(input("enter a number: "))

oddTotal = oddify(number-1)

print(oddTotal)
