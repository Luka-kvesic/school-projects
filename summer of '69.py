listling = eval(input("enter a list of numbers: "))

def summer69(listo):
    adding = True
    total = 0
    for i in range(len(listo)):
        if listo[i] == 6:
            adding = False
        if adding == True:
            total += listo[i]
        if listo[i] == 9:
            adding = True
    return total
            

total = summer69(listling)
print(total)