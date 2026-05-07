string = input("enter a two word string: ")
def animalCrackers(stringling):
    for i in range(len(stringling)):
        letter = stringling[i]
        if i == 0:
            firstLetter = letter
        if letter == " ":
            secondLetter = stringling[i + 1]
            if firstLetter == secondLetter:
                return True
            else:
                return False
answer = animalCrackers(string)
print(answer)
