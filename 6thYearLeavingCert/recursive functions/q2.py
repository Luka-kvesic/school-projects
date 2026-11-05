# Q2

def lengthifyString(string):
    
    if string == "":
        return 0
    else:
        if string[0].isalpha:
            return 1 + lengthifyString(string[1:])
        else:
            return 0 + lengthifyString(string[1:])


string = input("enter a string: ")

lengthString = lengthifyString(string)

print(lengthString)
