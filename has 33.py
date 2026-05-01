listington = eval(input("enter a list of numbers: "))

def has33(listling):
    for i in range(len(listling)):
        if listling[i] == 3:
            if listling[i + 1] == 3:
                return True
    else:
        return False

answer = has33(listington)
print(answer)