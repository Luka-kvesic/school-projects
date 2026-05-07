listoliser9000 = eval(input("enter a list of numbers: "))

def spyGame(listo):
    code = ""
    for i in range(len(listo)):
        if listo[i] == 0:
            code += "0"
        elif listo[i] == 7:
            code += "7"
    for i in range(len(code)):
        if code[i] == "0":
            if code[i+1] == "0":
                if code[i+2] =="7":
                    return True
        else:
            return False
    
        
        

answer = spyGame(listoliser9000)
print(answer)
