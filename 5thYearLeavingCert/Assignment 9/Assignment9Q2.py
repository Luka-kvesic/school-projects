#author: Luka kvesic
#date: 17 october 2025
#description: ask for name and surname and display the length of it

name = input("what is your name: ")
surname = input("whats your surname: ")
combinedName = (name +" "+ surname)
lengthOfFullName = len(combinedName)
print(combinedName)

print('the length of your full name is',lengthOfFullName)

