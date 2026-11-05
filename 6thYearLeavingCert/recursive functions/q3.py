# Q3

def digitSumify(number):
    if number == "":
        return "0"
    else:
        if int(number) < 0:
            return "0"
        else:
            return str(int(number[0]) + int(digitSumify(number[1:])))
        

number = input("enter a number: ")

digitSum = digitSumify(number)

print(digitSum)
