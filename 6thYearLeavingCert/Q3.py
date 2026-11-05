# Q3

def digitSumify(number, operation):
    print(number)
    if number == "":
        return 0, "string"
    else:
        if int(number) < 0:
            return 0 , "string"
        else:
            if operation == "number":
                return int(number[0]) + digitSumify(number[1:], "number"), "string"
            elif operation == "string":
                return number[0] + digitSumify(number[1:], "string"), "string"
        

number = input("enter a number: ")

digitSum, forget = digitSumify(number, "number")

print(digitSum)