name = input("enter a name: ")
def oldMacdonald(name):
    updatedName = ""
    for i in range(len(name)):
        letter = name[i]
        if (i == 0) or (i == 3):
            letter = letter.upper()
        updatedName += letter
    return updatedName
string = oldMacdonald(name)

print(string)
    
